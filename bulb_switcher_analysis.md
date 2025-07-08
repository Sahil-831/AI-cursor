# Bulb Switcher Problem Analysis

## Problem Statement
Given n bulbs initially off, perform n rounds where:
- Round 1: Toggle all bulbs
- Round 2: Toggle every 2nd bulb  
- Round 3: Toggle every 3rd bulb
- Round i: Toggle every ith bulb
- Round n: Toggle only the nth bulb

Find how many bulbs are on after all rounds.

## Key Insight
A bulb at position k gets toggled in round i **if and only if** i divides k. Therefore:
- Bulb k gets toggled once for each divisor of k
- A bulb is ON if toggled an odd number of times (starts OFF)
- **A number has odd divisors if and only if it's a perfect square**

## Mathematical Explanation
Most numbers have divisors in pairs: (d, n/d). For example:
- 12 has divisors: 1×12, 2×6, 3×4 → 6 divisors (even)
- 9 has divisors: 1×9, 3×3 → 3 divisors (odd, because 3×3 = 9)

Perfect squares have one divisor that pairs with itself (√n), giving odd total divisors.

## Solution
The answer is simply: **floor(√n)**

This counts perfect squares from 1 to n.

## Examples
- n=3: Perfect squares ≤ 3 are {1} → Answer: 1
- n=4: Perfect squares ≤ 4 are {1, 4} → Answer: 2  
- n=9: Perfect squares ≤ 9 are {1, 4, 9} → Answer: 3

## Time Complexity
- **Optimal Solution**: O(1) - just compute √n
- **Simulation**: O(n²) - toggle bulbs in n rounds

## Verification
The mathematical solution matches simulation for all test cases, confirming the perfect square pattern.