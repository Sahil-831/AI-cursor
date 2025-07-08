def bulbSwitch(n):
    """
    There are n bulbs that are initially off. You first turn on all the bulbs, 
    then you turn off every second bulb. On the third round, you toggle every 
    third bulb (turning on if it's off or turning off if it's on). For the ith 
    round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
    
    Return the number of bulbs that are on after n rounds.
    
    Key insight: A bulb at position k gets toggled in round i if i divides k.
    So bulb k gets toggled once for each divisor of k.
    A bulb will be ON if it gets toggled an odd number of times.
    A number has an odd number of divisors if and only if it's a perfect square.
    
    Therefore, the answer is the number of perfect squares from 1 to n.
    """
    import math
    return int(math.sqrt(n))


def test_bulb_switch():
    """Test the solution with the provided examples"""
    # Test case 1
    assert bulbSwitch(3) == 1, f"Expected 1, got {bulbSwitch(3)}"
    print("✓ Test case 1 passed: n=3 -> 1")
    
    # Test case 2  
    assert bulbSwitch(0) == 0, f"Expected 0, got {bulbSwitch(0)}"
    print("✓ Test case 2 passed: n=0 -> 0")
    
    # Test case 3
    assert bulbSwitch(1) == 1, f"Expected 1, got {bulbSwitch(1)}"
    print("✓ Test case 3 passed: n=1 -> 1")
    
    # Additional test cases
    assert bulbSwitch(4) == 2, f"Expected 2, got {bulbSwitch(4)}"  # Perfect squares: 1, 4
    print("✓ Additional test: n=4 -> 2")
    
    assert bulbSwitch(9) == 3, f"Expected 3, got {bulbSwitch(9)}"  # Perfect squares: 1, 4, 9  
    print("✓ Additional test: n=9 -> 3")
    
    assert bulbSwitch(16) == 4, f"Expected 4, got {bulbSwitch(16)}"  # Perfect squares: 1, 4, 9, 16
    print("✓ Additional test: n=16 -> 4")
    
    print("\nAll tests passed! 🎉")


def simulate_bulb_switch(n):
    """
    Simulation approach to verify our mathematical solution
    This is less efficient but helps understand the problem
    """
    if n == 0:
        return 0
        
    # Initialize all bulbs as off (False)
    bulbs = [False] * n
    
    # Perform n rounds
    for round_num in range(1, n + 1):
        # Toggle every round_num-th bulb
        for i in range(round_num - 1, n, round_num):
            bulbs[i] = not bulbs[i]
    
    # Count bulbs that are on
    return sum(bulbs)


def verify_with_simulation():
    """Verify our mathematical solution matches the simulation"""
    test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 25, 100]
    
    print("Verifying mathematical solution against simulation:")
    for n in test_cases:
        math_result = bulbSwitch(n)
        sim_result = simulate_bulb_switch(n)
        status = "✓" if math_result == sim_result else "✗"
        print(f"{status} n={n}: Math={math_result}, Simulation={sim_result}")


if __name__ == "__main__":
    print("Bulb Switcher Problem Solution")
    print("=" * 40)
    
    # Run basic tests
    test_bulb_switch()
    
    print("\n" + "=" * 40)
    
    # Verify with simulation
    verify_with_simulation()
    
    print("\n" + "=" * 40)
    print("Example walkthrough for n=3:")
    print("Initial: [off, off, off]")
    print("Round 1: Toggle all -> [on, on, on]") 
    print("Round 2: Toggle every 2nd -> [on, off, on]")
    print("Round 3: Toggle every 3rd -> [on, off, off]")
    print("Result: 1 bulb is on")
    print(f"Our solution: {bulbSwitch(3)}")