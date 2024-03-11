# Maximum Full Bags of Marbles

Consider having `n` bags labeled from `0` to `n - 1`, each with defined capacities in the `capacity` array and current marble counts in the `marbles` array. There is also an integer named `extraMarbles` indicating the surplus marbles available for distribution. 

Return the maximum number of bags that can achieve full capacity by strategically allocating the extra marbles.

## **Example 1:**
```
Input: capacity = [3,5,8,10], marbles = [2,2,6,1], extraMarbles = 3
Output: 2
Explanation: You can add 2 marbles to the third bag to make it full, and one marble to the first bag, resulting in two bags at full capacity.
```

## **Example 2:**
```
Input: capacity = [2,4,6], marbles = [2,4,6], extraMarbles = 5
Output: 3
Explanation: All 3 bags are already at capacity. No extraMarbles necessary.
```