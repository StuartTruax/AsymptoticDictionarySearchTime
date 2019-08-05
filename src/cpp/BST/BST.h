#include <cstdlib>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>

using namespace std;

namespace py = pybind11;


class BSTNode{
public:
  BSTNode* left;
  BSTNode* right;
  int val;

  BSTNode(){};

  BSTNode(BSTNode* left, BSTNode* right, int val)
  {
    this->left = left; this->right=right; this->val = val;
  };

};

class BST{
  public:
    BST(){};
    //BST(BSTNode*);
    void insert(int);
    bool search(int);
    void del(int);
    string to_string_in_order();

  private:
      void insert(int,BSTNode&);
      bool search(int, BSTNode&);
      void del_search(int,BSTNode&);
      void del_parent(BSTNode*,BSTNode*);
      string to_string_in_order_traverse(string&,BSTNode&);
      BSTNode* find_min(BSTNode*);
      BSTNode* root = NULL;

};

PYBIND11_MODULE(BST, m) {
    py::class_<BST>(m, "BST")
    .def(py::init<>())
    // (<return type> (<scope>::*)(<param>)) syntax to accomodate overloaded
    //cpp function
    .def("insert", (void (BST::*)(int)) &BST::insert)
    .def("search", (bool (BST::*)(int)) &BST::search)
    .def("delete",  &BST::del)
    .def("toStringInOrder",  &BST::to_string_in_order);

}
