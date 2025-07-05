# Project No.20
# String Formatting

names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]

# Print a formatted header for the table

print('{0:<10} {1:<5}'.format("Name", "Score"))
# {0:<10} -> index 0 ("Name"), left-aligned, width of 10 characters
# {1:>5}  -> index 1 ("Score"), right-aligned, width of 5 characters

for index in range(len(names)):
    name = names[index]
    score = scores[index]
    print('{0:<10} {1:>5}'.format(name, score))
