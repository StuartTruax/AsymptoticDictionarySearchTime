#include "BST.h"


void BST::insert(int to_insert)
{
  if(root == NULL)
  {
    this->root = new BSTNode(NULL,NULL,to_insert);
  }
  else
    insert(to_insert,*root);
}


void BST::insert(int to_insert, BSTNode& node)
{
  if(&node == NULL)
     return;
  else if (node.val == to_insert)
    return;
  else if (node.val > to_insert)
    if (node.left == NULL)
    {
      BSTNode* new_node = new BSTNode(NULL,NULL,to_insert);
      node.left = new_node;
    }
    else
      insert(to_insert, *node.left);
  else
  {
    if (node.right == NULL)
    {
      BSTNode* new_node = new BSTNode(NULL,NULL,to_insert);
      node.right = new_node;
    }
    else
      insert(to_insert, *node.right);
  }
}


bool BST::search(int to_find)
{
  return search(to_find,*root);
}

bool BST::search(int to_find, BSTNode& node)
{
  if(&node == NULL)
  {
    return false;
  }
  else if (node.val == to_find)
  {
    return true;
  }
  else
  {
    if (( to_find < node.val) && (node.left  != NULL))
      return search(to_find, *node.left);
    else if (node.right  != NULL)
      return search(to_find, *node.right);
  }
  return false;
}


void BST::del(int to_delete)
{
   if (root != NULL)
   {
     // deal with case of root here
     if( root->val == to_delete)
      del_parent(root,NULL);
     else
      del_search(to_delete,*root);
   }

}

void BST::del_search(int to_delete, BSTNode& node)
{

  if(&node == NULL)
    return;
  else if (node.left != NULL)
  {
    if (node.left->val == to_delete)
    {
      del_parent(node.left,&node);
    }
    else
      del_search(to_delete, *node.left);
  }
  else if (node.right != NULL)
  {
    if (node.right->val == to_delete)
    {
      del_parent(node.right,&node);
    }
    else
      del_search(to_delete, *node.right);
  }

}

BSTNode* BST::find_min(BSTNode* node)
{
  if(node->left !=  NULL)
  {
    return find_min(node->left);
  }
  return node;
}


void BST::del_parent(BSTNode* to_delete, BSTNode* parent)
{
  if ((to_delete->right ==  NULL) && (to_delete->left == NULL))
  {
    if (parent == NULL)
    {
      this->root =  NULL;
    }
    else
    {
      if (to_delete == parent->right)
      {
        parent->right =  NULL;
      }
      else
      {
        parent->left =  NULL;
      }
    }
  }
    else if ((to_delete->right != NULL) && (to_delete->left == NULL))
    {
      if (parent == NULL)
      {
        this->root =  to_delete->right;
      }
      else
      {
        if (to_delete == parent->right)
        {
          parent->right =  to_delete->right;
        }
        else
        {
          parent->left =  to_delete->right;
        }
      }
    }
      else if ((to_delete->right == NULL) && (to_delete->left != NULL))
      {
        if (parent == NULL)
        {
          this->root =  to_delete->left;
        }
        else
        {
          if (to_delete == parent->right)
          {
            parent->right =  to_delete->left;
          }
          else
          {
            parent->left =  to_delete->left;
          }
        }
      }
     else
     {
          BSTNode* left_min = find_min(to_delete->left);
          to_delete->val = left_min->val;
          del_search(left_min->val, *to_delete);
      }

}




string BST::to_string_in_order()
{
  string ret;
  ret = to_string_in_order_traverse(ret,*root);
  return ret;
}


string BST::to_string_in_order_traverse(string& ret,BSTNode& node)
{
  if(&node != NULL)
  {
    ret = to_string_in_order_traverse(ret,*node.left);
    if(ret.length() == 0)
    {
      ret=ret+to_string(node.val);
    }
    else
    {
      ret=ret+" "+to_string(node.val);
    }
    ret = to_string_in_order_traverse(ret,*node.right);
  }

  return ret;
}
