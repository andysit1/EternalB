+++
title = "patterns.md"
date = "2024-08-23"
+++
### Prefix Sum 
- Given an array nums, answer multiple queries about the sum of elements within a range of [i, j]
- nums = [x + 1] i = 1, j = 3
```

class NumArray:

  

    def __init__(self, nums: List[int]):

        self.pre = []

        for i in range(len(nums)):

            _ = sum(nums[0 : i + 1])

            self.pre.append(_)

        print("pre", self.pre)

    def sumRange(self, left: int, right: int) -> int:

        r = self.pre[right]

        l = self.pre[left - 1] if left > 0 else 0  

  
        return r - l
```

Issues
- syntax error
- I misunderstood that the left > 0 else 0 part. didnt undeerstand self.pre[0] and 0 were different

### Two Pointers

>Use this pattern when dealing with sorted arrays or lists where you need to find pairs that satisfy a specific condition.

>Contiguous Subarrays are arrays just are fixed (same order)

Requirement : Sorted List

1.) 2 pointers left and right of the array
2.) the left point is used for small values adjustments x > target
3.) the right point is used for large value adjustments x < target

### Sliding Window
>Use this pattern when dealing with problems involving contiguous subarrays or substrings.

1.) start with the sum of the first k elements
2.) pop elements that do not belong or use a dict

use dict slicing, it's more clean


### Fast & Slow Pointers
>The Fast & Slow Pointers (Tortoise and Hare) pattern is used to detect cycles in linked lists and other similar structures.

1. If there is a cycle, the fast pointer will eventually meet the slow pointer.
2.  If the fast pointer reaches the end of the list, there is no cycle.

Follow up question
How are cycles used in programming and real word. For example, how would one identity the use of a pointer.


At this point patterns are going into my details 

Key Words
- link list
- stacks
- k elements
- intervals
- trees
	- dfs
	- bfs
- matrix traversal
- backtracking
- dynamic programming 

### LinkedList In-place Reversal
>Use this pattern when you need to reverse sections of a linked list.



