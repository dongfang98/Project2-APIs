from example import *

def test_add():
  assert add(2,3) == 5
  assert add('boston','university') == 'bostonuniversity'
  assert numpy_add(2,3) == 5
  
def test_subtract():
  assert subtract(2,3) == -1
  assert numpy_subtract(2,3) == -1
