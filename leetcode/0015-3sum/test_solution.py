import pytest
from solution import threeSum

def test_examples():
    assert sorted(threeSum([-1,0,1,2,-1,-4])) == sorted([[-1,-1,2],[-1,0,1]])
    assert threeSum([0,0,0]) == [[0,0,0]]
    assert threeSum([1,2,3]) == []
    assert threeSum([-2,0,0,2,2]) == [[-2,0,2]]
    assert threeSum([100000,-100000,0]) == [[-100000,0,100000]]