#!/bin/bash
cd simulator/cpp_implementations
cmake ../../src/cpp
make
mv Array/Array.so Array.so
mv BST/BST.so BST.so
mv HashTable/HashTable.so HashTable.so

#clean up build directory
shopt -s extglob
rm -rv !(*.so|*.py)
