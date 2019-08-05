cmake_minimum_required(VERSION 2.8.12)
project(HashTable)

find_package(pybind11 REQUIRED)
pybind11_add_module(HashTable HashTable.cpp)
