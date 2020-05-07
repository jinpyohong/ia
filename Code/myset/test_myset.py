import pytest
from myset import Set

@pytest.fixture
def x():
    return Set(['a', 'b', 'c', 1, 2, 3])

@pytest.fixture
def y():
    return Set(['x', 3])

@pytest.fixture
def xx():
    return set(['a', 'b', 'c', 1, 2, 3])

@pytest.fixture
def yy():
    return set(['x', 3])
        
def test_init():
    xl = ['a', 'b', 'c', 1, 2, 3] + ['x', 3]
    x = Set(xl)
    assert len(x.data) == len(set(xl))  # check duplication
    assert set(x.data) == set(xl)

def test_init_empty():
    x = Set()
    assert x.data == []

def test_intersection(x, y, xx, yy):
    z = x.intersection(y)
    assert set(z.data) == xx.intersection(yy)
    
def test_union(x, y, xx, yy):
    z = x.union(y)
    assert set(z.data) == xx.union(yy)

def test_ior(x, y, xx, yy):
    x_copy = x     # copy reference
    x |= y
    assert set(x.data) == xx | yy
    assert x is x_copy    # same reference to the Set object

def test_iand(x, y, xx, yy):
    x_copy = x     # copy reference
    x &= y
    assert set(x.data) == xx & yy
    assert x is x_copy    # same reference to the Set object

def test_add(x, xx):
    x_copy = x
    x.add('z')
    xx.add('z')
    assert set(x.data) == xx
    assert x is x_copy
    