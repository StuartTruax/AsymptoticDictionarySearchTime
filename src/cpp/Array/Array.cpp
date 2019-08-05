#include "Array.h"



Array::Array(int size, bool is_sorted)
{
  this->size = size;
  this->is_sorted = is_sorted;
  this->last_element = 0;
  this->data = (int*)malloc(sizeof(int)*size);
}

void Array::insert(int input){
  if(last_element < size)
  {
    data[last_element] = input;
    last_element++;
  }
  if(is_sorted)
  {
    sort();
  }
}

void Array::sort()
{
  vector<int> temp(data, data+last_element);
  std::sort(temp.begin(),temp.end());
  for(int i=0; i < last_element; i++)
  {
    data[i] = temp[i];
  }
}



bool Array::search(int input)
{
  if(is_sorted)
  {
    return binarySearch(input, 0, last_element-1);
  }
  else
  {
    for(int i=0; i < last_element;i++)
    {
      if(data[i] == input){
        return true;
      }
    }
  }
  return false;
}

bool Array::binarySearch(int input, int start, int end)
{
  if(start == end)
  {
    if(data[start]==input)
    {
      return true;
    }
    return false;
  }

  int mid = (int)((start + end)/2);

  if ((input >=data[start]) && ( input <= data[mid]))
  {
    return binarySearch(input,start,mid);
  }
  else if((input > data[mid]) && (input <= data[end]))
  {
    return binarySearch(input, mid+1, end);
  }

  return false;
}


Array::~Array()
{
}
