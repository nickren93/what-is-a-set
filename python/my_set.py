class MySet:
  # throw an error if called with anything other than string, array or nothing
  # if an iterable is provided only its unique values should be in data
  # strings and arrays will need to be broken down by their elements/characters
  def __init__ (self, iterable=None):
    self.data = {}
    if type(iterable) not in [str, list] and iterable is not None:
      raise Exception("MySet instance must be initialized with nothing, a string, or an array!")
    
    if iterable is not None:
      for e in iterable:
        if e not in self.data:
          self.data[e] = True

  # return number of elements in MySet
  def size(self):
    return len(self.data.keys())
  

  # add an item to MySet as is
  # don't worry about arrays here!
  # return the MySet instance
  def add(self, item):
    if item not in self.data:
      self.data[item] = True
    return self
  

  # delete an item from MySet
  # don't worry about arrays here!
  # return true if successful, otherwise false
  def delete(self, item):
    if item in self.data:
      del self.data[item]
      return True
    return False
  

  # return true if in MySet, otherwise false
  # don't worry about arrays here!
  def has(self, item):
    return item in self.data
  

  # return data as an array
  # don't worry about arrays here!
  def entries(self):
    return list(self.data.keys())


  


# if (require.main === module) {
#   // add your own tests in here
  
# }

# module.exports = MySet;

