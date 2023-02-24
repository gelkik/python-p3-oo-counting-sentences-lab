#!/usr/bin/env python3

class MyString:
  def __init__(self,value=''):
    self._value = value
    
  def get_value(self):
    return self._value

  def set_value(self,value):
    if type(value)==str:
      self._value = value
    else:
      print('The value must be a string.')

  value = property(get_value,set_value)

  def is_sentence(self):
    return self._value[-1] == '.'
  
  def is_question(self):
    return self._value[-1] == '?'
  
  def is_exclamation(self):
    return self._value[-1] == '!'
  
  def count_sentences(self):
    count = 0
    i = 0
    while i < len(self._value):
      punct = [x for x in self._value]
      if (punct[i] == '.' or punct[i] == '!' or punct[i] == '?'):
        if (punct[i-1] != '.' and punct[i-1] != '!' and punct[i-1] != '?'):
          count += 1
      i+=1
    return count



  
      