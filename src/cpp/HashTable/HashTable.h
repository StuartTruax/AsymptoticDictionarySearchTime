#include <cstdlib>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>

using namespace std;

namespace py = pybind11;


class HashNode{
public:
  HashNode* next;
  HashNode* prev;
  int val;

  HashNode(){};

  HashNode(HashNode* next, HashNode* prev, int val)
  {
    this->next = next; this->prev=prev; this->val = val;
  };

};

class HashTable{
  public:
    HashTable(int);
    void insert(int);
    bool search(int);
    void del(int);
    string to_string();

  private:
      int hash(int);
      int M = 0;
      HashNode** table = NULL;
};

PYBIND11_MODULE(HashTable, m) {
    py::class_<HashTable>(m, "HashTable")
    .def(py::init<int>())
    .def("insert",  &HashTable::insert)
    .def("search",  &HashTable::search)
    .def("delete",  &HashTable::del)
    .def("__str__", &HashTable::to_string);

}
