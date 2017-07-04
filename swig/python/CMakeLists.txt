cmake_minimum_required(VERSION 3.1)

find_package(PythonLibs REQUIRED)
find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

include_directories(
	${PYTHON_INCLUDE_DIRS}
	${CMAKE_CURRENT_SOURCE_DIR}/..
	${CMAKE_SOURCE_DIR}/src
)

set_property(SOURCE ${CMAKE_SOURCE_DIR}/swig/python/libyangpyc.i PROPERTY SWIG_FLAGS "-I${CMAKE_BINARY_DIR}/src")

set_source_files_properties(${CMAKE_SOURCE_DIR}/swig/python/libyangpyc.i PROPERTIES CPLUSPLUS ON)

swig_add_module(libyangpyc python ${CMAKE_SOURCE_DIR}/swig/python/libyangpyc.i ${libsrc} ${PCRE_INCLUDE_DIRS} )

# link math
swig_link_libraries(libyangpyc m)

# find pthreads
swig_link_libraries(libyangpyc ${CMAKE_THREAD_LIBS_INIT})

# find PCRE library
swig_link_libraries(libyangpyc ${PCRE_LIBRARIES})

set(SWIG_DEST "python")
file(COPY "${CMAKE_SOURCE_DIR}/src" DESTINATION ${SWIG_DEST})
file(COPY "${CMAKE_SOURCE_DIR}/models" DESTINATION ${SWIG_DEST})
file(COPY "${CMAKE_SOURCE_DIR}/swig/python/files" DESTINATION "${SWIG_DEST}")
file(COPY "${CMAKE_SOURCE_DIR}/swig/python/libyang" DESTINATION "${SWIG_DEST}")
configure_file("${CMAKE_SOURCE_DIR}/swig/python/test.py" "${SWIG_DEST}/test.py" ESCAPE_QUOTES @ONLY)
configure_file("${CMAKE_SOURCE_DIR}/swig/python/setup.py" "${SWIG_DEST}/setup.py" ESCAPE_QUOTES @ONLY)

add_custom_target(pythonpkg ALL
	COMMENT "start building python package"
	COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_BINARY_DIR}/libyangpycPYTHON_wrap.cxx "${SWIG_DEST}/src/"
	COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_BINARY_DIR}/libyangpyc.py "${SWIG_DEST}/libyang/")
add_dependencies (pythonpkg _libyangpyc)
