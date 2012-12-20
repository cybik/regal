/* NOTE: Do not edit this file, it is generated by a script:
   Export.py --api gl 4.2 --api wgl 4.0 --api glx 4.0 --api cgl 1.4 --api egl 1.0 --outdir src/regal
*/

/*
  Copyright (c) 2011 NVIDIA Corporation
  Copyright (c) 2011-2012 Cass Everitt
  Copyright (c) 2012 Scott Nations
  Copyright (c) 2012 Mathias Schott
  Copyright (c) 2012 Nigel Stewart
  Copyright (c) 2012 Google Inc.
  All rights reserved.

  Redistribution and use in source and binary forms, with or without modification,
  are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

    Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
  IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
  INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
  OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
  OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/*
  Intended formatting conventions:
  $ astyle --style=allman --indent=spaces=2 --indent-switches
*/

#ifndef __REGAL_SYSTEM_H__
#define __REGAL_SYSTEM_H__

#if _WIN32
# if defined(PPAPI)
#  ifndef REGAL_SYS_PPAPI
#   define REGAL_SYS_PPAPI 1
#  endif
# else
#  ifndef REGAL_SYS_WGL
#   define REGAL_SYS_WGL 1
#  endif
# endif
#elif __APPLE__
# include <TargetConditionals.h>
# if TARGET_OS_IPHONE
#  ifndef REGAL_SYS_IOS
#   define REGAL_SYS_IOS 1
#  endif
# else
#  ifndef REGAL_SYS_OSX
#   define REGAL_SYS_OSX 1
#  endif
# endif
#elif defined(__native_client__)
# ifndef REGAL_SYS_PPAPI
#  define REGAL_SYS_PPAPI 1
# endif
#elif defined(__ANDROID__)
# ifndef REGAL_SYS_ANDROID
#  define REGAL_SYS_ANDROID 1
# endif
# ifndef REGAL_SYS_EGL
#  define REGAL_SYS_EGL 1
# endif
#elif !defined(_WIN32) && !defined(__APPLE__) && !REGAL_SYS_PPAPI
# ifndef REGAL_SYS_GLX
#  define REGAL_SYS_GLX 1
# endif
#endif

#ifndef REGAL_SYS_WGL
# define REGAL_SYS_WGL 0
#endif

#ifndef REGAL_SYS_IOS
# define REGAL_SYS_IOS 0
#endif

#ifndef REGAL_SYS_OSX
# define REGAL_SYS_OSX 0
#endif

#ifndef REGAL_SYS_PPAPI
# define REGAL_SYS_PPAPI 0
#endif

#ifndef REGAL_SYS_ANDROID
# define REGAL_SYS_ANDROID 0
#endif

#ifndef REGAL_SYS_EGL
# define REGAL_SYS_EGL 0
#endif

#ifndef REGAL_SYS_GLX
# define REGAL_SYS_GLX 0
#endif

#endif // __REGAL_SYSTEM_H__
