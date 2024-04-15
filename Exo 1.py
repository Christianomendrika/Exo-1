from itertools import product

def truth_table(expression):
    variables = sorted(set(expression.replace('(', '').replace(')', '').replace('+', '').replace('*', '')))
    header = variables + [expression]

    table = []
    for values in product([0, 1], repeat=len(variables)):
        value_dict = dict(zip(variables, values))
        eval_result = eval(expression, value_dict)
        row = [value_dict[var] for var in variables] + [eval_result]
        table.append(row)

    print("Truth Table:")
    print("|".join(header))
    print("-" * (len("|".join(header))))
    for row in table:
        print("|".join(map(str, row)))

    # Generating canonical forms
    minterms = [index for index, row in enumerate(table) if row[-1] == 1]
    maxterms = [index for index, row in enumerate(table) if row[-1] == 0]

    print("\nFirst Canonical Form:")
    first_canonical = " + ".join([f"({''.join(['~' + variables[i] if value == 0 else variables[i] for i, value in enumerate(table[row][:-1])])})" for row in minterms])
    print(first_canonical)

    print("\nSecond Canonical Form:")
    second_canonical = " * ".join([f"({''.join(['~' + variables[i] if value == 1 else variables[i] for i, value in enumerate(table[row][:-1])])})" for row in maxterms])
    print(second_canonical)

if __name__ == "__main__":
    expression = input("Entrez une expression logique en utilisant les opérateurs *, + et ~ pour la négation : ")
    truth_table(expression)
