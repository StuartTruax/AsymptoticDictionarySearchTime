#include <cstdlib>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <algorithm>

using namespace std;

namespace py = pybind11;

class Array{
  public:
      Array(int,bool);
      void insert(int);
      bool search(int);
      ~Array();

  private:
      bool binarySearch(int,int,int);
      void sort();
      bool is_sorted;
      int* data;
      int size;
      int last_element;

};

PYBIND11_MODULE(Array, m) {
    py::class_<Array>(m, "Array")
        .def(py::init<int,bool>())
        .def("insert", &Array::insert)
        .def("search", &Array::search);
}
