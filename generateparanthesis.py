def generate_parenthesis(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            combinations.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    combinations = []
    backtrack('', 0, 0)
    return combinations

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if n % 2 != 0:
        print("Please enter an even number.")
    else:
        combinations = generate_parenthesis(n // 2)
        for combo in combinations:
            print(combo)
