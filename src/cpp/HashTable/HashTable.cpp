#include "HashTable.h"


HashTable::HashTable(int m)
{
  if (m > 0)
  {
    this->M = m;
    this->table = (HashNode**)malloc(m*sizeof(HashNode*));

    for(int i = 0; i < M; i++)
    {
      table[i] = NULL;
    }

  }
}



void HashTable::insert(int to_insert)
{
  int index = hash(to_insert);

  if (table[index] == NULL)
  {
    table[index] = new HashNode(NULL,NULL,to_insert);
  }
  else
  {
    //chain on collision condition here
    HashNode* cur = table[index];
    HashNode* new_node = new HashNode(NULL,NULL,to_insert);
    while( cur->next != NULL)
    {
      cur = cur->next;
    }

    new_node->prev=cur;
    cur->next = new_node;
  }


}



int HashTable::hash(int to_hash)
{
  int ret;
  if (to_hash < 0)
  {
    ret = -to_hash%M;
  }
  else
  {
    ret = to_hash%M;
  }
  return ret;

}

bool HashTable::search(int to_search)
{
  int index = hash(to_search);

  HashNode* node = table[index];

  if(node ==  NULL)
  {
    return false;
  }
  else
  {
    while(node != NULL)
    {
      if(node->val == to_search)
      {
        return true;
      }
      node = node->next;
    }
  }

  return false;
}


void HashTable::del(int to_delete)
{
  int index = to_delete;

  HashNode* node = table[index];

  if (node != NULL)
  {
    HashNode* prev = NULL;
    while( node != NULL)
    {
      if(node->val == to_delete)
      {
        if(prev != NULL)
        {
          prev->next = node->next;
          if(node->next != NULL)
          {
            node->next->prev = prev;
          }

        }
        else
        {
          table[index] = node->next;
          if(table[index] != NULL)
          {
            table[index]->prev = NULL;
          }
        }
      }

      prev = node;
      node = node->next;
    }
  }
}


string HashTable::to_string()
{
  string ret("[\n");
  for(int i=0; i < M; i++)
  {
    ret+="[";
    if(table[i] != NULL)
    {
      //ret=ret+" <-[ "+std::to_string(table[i]->val)+" ]->, ";

        HashNode* node = table[i];

        while (node != NULL)
        {
          ret+=" <-[ "+std::to_string(node->val)+" ]->, ";
          node = node->next;
        }
    }
    else
    {
      ret+=" X,";
    }
      ret+="]\n";
  }
  ret+="]";

  return ret;
}
