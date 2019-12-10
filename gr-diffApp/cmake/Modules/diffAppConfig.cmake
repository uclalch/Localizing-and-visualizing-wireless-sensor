INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DIFFAPP diffApp)

FIND_PATH(
    DIFFAPP_INCLUDE_DIRS
    NAMES diffApp/api.h
    HINTS $ENV{DIFFAPP_DIR}/include
        ${PC_DIFFAPP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DIFFAPP_LIBRARIES
    NAMES gnuradio-diffApp
    HINTS $ENV{DIFFAPP_DIR}/lib
        ${PC_DIFFAPP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DIFFAPP DEFAULT_MSG DIFFAPP_LIBRARIES DIFFAPP_INCLUDE_DIRS)
MARK_AS_ADVANCED(DIFFAPP_LIBRARIES DIFFAPP_INCLUDE_DIRS)

