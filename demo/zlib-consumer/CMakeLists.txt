cmake_minimum_required(VERSION 3.12)
project(conandemo)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(conandemo zlibapp.c)
target_link_libraries(conandemo ${CONAN_LIBS})
