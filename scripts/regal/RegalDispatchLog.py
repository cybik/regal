#!/usr/bin/python -B

from string import Template, upper, replace

from ApiCodeGen   import *
from ApiUtil      import outputCode
from ApiUtil      import typeIsVoid
from ApiRegal     import logFunction

from RegalContextInfo import cond

from RegalDispatchShared import apiDispatchFuncInitCode
from RegalDispatchShared import apiDispatchGlobalFuncInitCode

# CodeGen for dispatch table init.

dispatchLogTemplate = Template('''${AUTOGENERATED}
${LICENSE}

#include "pch.h" /* For MS precompiled header support */

#include "RegalUtil.h"

#if REGAL_LOG

REGAL_GLOBAL_BEGIN

#include "RegalLog.h"
#include "RegalPush.h"
#include "RegalToken.h"
#include "RegalHelper.h"
#include "RegalContext.h"
#include "RegalDispatch.h"
#include "RegalDispatcherGL.h"
#include "RegalDispatcherGlobal.h"

using namespace ::REGAL_NAMESPACE_INTERNAL::Logging;
using namespace ::REGAL_NAMESPACE_INTERNAL::Token;

REGAL_GLOBAL_END

REGAL_NAMESPACE_BEGIN

${API_FUNC_DEFINE}

void InitDispatchTableLog(DispatchTableGL &tbl)
{
${API_GL_DISPATCH_INIT}
}

${API_GLOBAL_DISPATCH_INIT}

REGAL_NAMESPACE_END

#endif
''')


def generateDispatchLog(apis, args):

  # CodeGen for API functions.

  code = ''
  categoryPrev = None

  for api in apis:

    code += '\n'
    if api.name in cond:
      code += '#if %s\n' % cond[api.name]

    for function in api.functions:

      if getattr(function,'regalOnly',False)==True:
        continue

      name   = function.name
      params = paramsDefaultCode(function.parameters, True)
      callParams = paramsNameCode(function.parameters)
      rType  = typeCode(function.ret.type)
      category  = getattr(function, 'category', None)
      version   = getattr(function, 'version', None)

      if category:
        category = category.replace('_DEPRECATED', '')
      elif version:
        category = version.replace('.', '_')
        category = 'GL_VERSION_' + category

      # Close prev category block.
      if categoryPrev and not (category == categoryPrev):
        code += '\n'

      # Begin new category block.
      if category and not (category == categoryPrev):
        code += '// %s\n\n' % category

      categoryPrev = category

      code += 'static %sREGAL_CALL %s%s(%s) \n{\n' % (rType, 'log_', name, params)
#     code += '    %s\n' % logFunction( function, 'Driver', True, False )

      if function.needsContext:
        code += '    RegalContext *_context = REGAL_GET_CONTEXT();\n'
        code += '    RegalAssert(_context);\n'

      # Temporarily adjust the context begin/end depth for proper indentation
      # of the glBegin call

      if name=='glBegin':
        code += '    RegalAssert(_context->depthBeginEnd>0);\n'
        code += '    Push<size_t> pushDepth(_context->depthBeginEnd);\n'
        code += '    _context->depthBeginEnd--;\n'

      # Temporarily adjust the context push/pop matrix depth for proper indentation
      # of the glPushMatrix call

      if name=='glPushMatrix':
        code += '    RegalAssert(_context->depthPushMatrix>0);\n'
        code += '    Push<size_t> pushDepth(_context->depthPushMatrix);\n'
        code += '    _context->depthPushMatrix--;\n'

      # Temporarily adjust the depth for proper indentation
      # of the glNewList call

      if name=='glNewList':
        code += '    RegalAssert(_context->depthNewList>0);\n'
        code += '    Push<size_t> pushDepth(_context->depthNewList);\n'
        code += '    _context->depthNewList--;\n'

      if function.needsContext:
        code += '    DispatchTableGL *_next = _context->dispatcher.logging.next();\n'
      else:
        code += '    DispatchTableGlobal *_next = dispatcherGlobal.logging.next();\n'

      code += '    RegalAssert(_next);\n'
      code += '    '
      if not typeIsVoid(rType):
        code += '%s ret = '%(rType)
      code += '_next->%s(%s);\n' % ( name, callParams )

      if typeIsVoid(rType):
        code += '    %s\n' % logFunction( function, 'Driver', True, True )
      else:
        code += '    %s\n' % logFunction( function, 'Driver', True, True, True )

      # Special handling for glUseProgram - log the attached shaders.

      if name=='glUseProgram':
        code += '    #if !REGAL_SYS_PPAPI\n'
        code += '    if (Logging::enableDriver && program && log_glIsProgram(program))\n'
        code += '    {\n'
        code += '      GLuint  _shaders[16];\n'
        code += '      GLsizei _count;\n'
        code += '      log_glGetAttachedShaders(program,16,&_count,_shaders);\n'
        code += '    }\n'
        code += '    #endif // REGAL_SYS_PPAPI\n'

      if not typeIsVoid(rType):
        code += '    return ret;\n'
      code += '}\n\n'

    if api.name in cond:
      code += '#endif // %s\n' % cond[api.name]
    code += '\n'

  # Close pending if block.
  if categoryPrev:
    code += '\n'

  # Output

  substitute = {}
  substitute['LICENSE']         = args.license
  substitute['AUTOGENERATED']   = args.generated
  substitute['COPYRIGHT']       = args.copyright
  substitute['API_FUNC_DEFINE'] = code
  substitute['API_GL_DISPATCH_INIT']     = apiDispatchFuncInitCode( apis, args, 'log' )
  substitute['API_GLOBAL_DISPATCH_INIT'] = apiDispatchGlobalFuncInitCode( apis, args, 'log' )

  outputCode( '%s/RegalDispatchLog.cpp' % args.srcdir, dispatchLogTemplate.substitute(substitute))
