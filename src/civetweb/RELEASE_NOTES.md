Release Notes v1.6 (Under Development)
===
### Objectives: *???*

Changes
-------

- Win32: Replace dll.def file by export macros in civetweb.h (CSTAJ)
- Base64 encode and decode functions for Lua (bel)
- Support pre-loaded files for the Lua environment (bel)
- Server should check the nonce for http digest access authentication (bel)
- Hide read-only flag in file dialogs opened by the Edit Settings dialog for the Windows executable (bel)
- Add all functions to dll.def, that are in the header (bel)
- Added Lua extensions: send_file, get_var, get_mime_type, get_cookie, url_decode, url_encode (bel)
- mg_set_request_handler() mod to use pattern (bel, Patch from Toni Wilk)
- Solved, tested and documented SSL support for Windows (bel)
- Fixed: select for Linux needs the nfds parameter set correctly  (bel) 
- Add methods for returning the ports civetweb is listening on (keithel)
- Fixes for Lua Server Pages, as described within the google groups thread. (bel)
- Added support for plain Lua Scripts, and an example script. (bel)
- A completely new, and more illustrative websocket example for C. (bel)
- An implementation of "Websocket for Lua", which allows to configure an optional websocket_root directory, incl. URL rewriting. Added an example. The Lua interface may change if the threading model changes.  (bel)
- Update of SQLite3 to 3.8.1. (bel)
- Add "date" header field to replies, according to the requirements of RFC 2616 (the HTTP standard), Section 14.18 (bel)
- Fix websocket long pull (celeron55)
- Updated API documentation (Alex Kozlov)
- Fixed Posix locking functions for Windows (bel2125)
- Updated version number

Release Notes v1.5
===
### Objectives: *Bug fixes and updates, repository restoration*

Changes
-------

- Corrected bad mask flag/opcode passing to websocket callback (William Greathouse)
- Moved CEVITWEB_VERSION define into civetweb.h
- Added new simple zip deployment build for Windows. 
- Removed windows install package build.
- Fixes page violation in mod_lua.inl (apkbox)
- Use C style comments to enable compiling most of civetweb with -ansi. (F-Secure Corporation)
- Allow directories with non ASCII characters in Windows in UTF-8 encoded (bel2125)
- Added Lua File System support (bel2125)
- Added mongoose history back in repository thanks to (Paul Sokolovsky)
- Fixed keep alive (bel2125)
- Updated of MIME types (bel2125)
- Updated lsqlite (bel2125)
- Fixed master thread priority (bel2125)
- Fixed IPV6 defines under Windowe (grenclave)
- Fixed potential dead lock in connection_close() (Morgan McGuire)
- Added WebSocket example using asynchronous server messages (William Greathouse)
- Fixed the getcwd() warning (William Greathouse)
- Implemented the connection_close() callback (William Greathouse)
- Fixed support URL's in civetweb.c (Daniel Oaks)
- Allow port number to be zero to use a random free port (F-Secure Corporation)
- Wait for threads to finish when stopping for a clean shutdown (F-Secure Corporation)
- More static analysis fixes against Coverity tool (F-Secure Corporation)
- Travis automated build testing support added (Daniel Oaks)
- Updated version numbers.
- Added contributor credits file.

Release Notes v1.4
===
### Objectives: *New URI handler interface, feature enhancements, C++ extensions*
The main idea behind this release is to bring about API consistency. All changes
are backward compatible and have been kept to a minimum.

Changes
-------

- Added mg_set_request_handler() which provides a URI mapping for callbacks.
   This is a new alternative to overriding callbacks.begin_request.
- Externalized mg_url_encode()
- Externalized mg_strncasecmp() for utiliy
- Added CivetServer::getParam methods
- Added CivetServer::urlDecode methods
- Added CivetServer::urlEncode methods
- Dealt with compiler warnings and some static analysis hits.
- Added mg_get_var2() to parse repeated query variables
- Externalized logging function cry() as mg_cry()
- Added CivetServer::getCookie method (Hariprasad Kamath)
- Added CivetServer::getHeader method (Hariprasad Kamath)
- Added new basic C embedding example
- Conformed source files to UNIX line endings for consistency.
- Unified the coding style to improve reability.

Release Notes v1.3 
===
### Objectives: *Buildroot Integration*

Changes
-------

- Made option to put initial HTMLDIR in a different place
- Validated build without SQLITE3 large file support
- Updated documentation
- Updated Buildroot config example

Release Notes v1.2 
===
### Objectives: *Installation Improvements, buildroot, cross compile support*
The objective of this release is to make installation seamless.

Changes
-------

- Create an installation guide
- Created both 32 and 64 bit windows installations
- Added install for windows distribution
- Added 64 bit build profiles for VS 2012.
- Created a buildroot patch
- Updated makefile to better support buildroot
- Made doc root and ports configurable during the make install.
- Updated Linux Install
- Updated OS X Package
- Improved install scheme with welcome web page

Known Issues
-----

- The prebuilt Window's version requires [Visual C++ Redistributable for Visual Studio 2012](http://www.microsoft.com/en-us/download/details.aspx?id=30679)

Release Notes v1.1 
===
### Objectives: *Build, Documentation, License Improvements*
The objective of this release is to establish a maintable code base, ensure MIT license rights and improve usability and documentation.

Changes
-------

- Reorangized build directories to make them more intuitive
- Added new build rules for lib and slib with option to include C++ class
- Upgraded Lua from 5.2.1 to 5.2.2
- Added fallback configuration file path for Linux systems.
    + Good for having a system wide default configuration /usr/local/etc/civetweb.conf
- Added new C++ abstraction class CivetServer
- Added thread safety for and fixed websocket defects (Morgan McGuire)
- Created PKGBUILD to use Arch distribution (Daniel Oaks)
- Created new documentation on Embeddeding, Building and yaSSL (see docs/).
- Updated License file to include all licenses.
- Replaced MD5 implementation due to questionable license.
     + This requires new source file md5.inl
- Changed UNIX/OSX build to conform to common practices.
     + Supports build, install and clean rules.
     + Supports cross compiling
     + Features can be chosen in make options
- Moved Cocoa/OSX build and packaging to a separate file.
     + This actually a second build variant for OSX.
     + Removed yaSSL from the OSX build, not needed.
- Added new Visual Studio projects for Windows builds.
     + Removed Windows support from Makefiles
     + Provided additional, examples with Lua, and another with yaSSL. 
- Changed Zombie Reaping policy to not ignore SIGCHLD.
     + The previous method caused trouble in applciations that spawn children.

Known Issues
-----

- Build support for VS6 and some other has been deprecated.
    + This does not impact embedded programs, just the stand-alone build.
    + The old Makefile was renamed to Makefile.deprecated.
    + This is partcially do to lack fo testing. 
    + Need to find out what is actually in demand.
- Build changes may impact current users.
    + As with any change of this type, changes may impact some users.

Release Notes v1.0
===

### Objectives: *MIT License Preservation, Rebranding*
The objective of this release is to establish a version of the Mongoose software distribution that still retains the MIT license.

Changes
-------

- Renamed Mongoose to Civetweb in the code and documentation.
- Replaced copyrighted images with new images
- Created a new code respository at https://github.com/sunsetbrew/civetweb
- Created a distribution site at https://sourceforge.net/projects/civetweb/
- Basic build testing