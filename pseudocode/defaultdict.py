from collections import defaultdict
# defaultdict auto inits missing keys to 0
# avoids KeyError on standard python {}


# ints
counts = defaultdict(int)

counts['a'] += 1 # no error, auto init to 0
counts['a'] += 1
print(counts['a']) # 2

# lists (arrays)
groups = defaultdict(list)
groups['fruit'].append('apple')
groups['fruit'].append('cherry')
groups['meat'].append('steak')
# groups['meat'].append(5)

print(groups) # defaultdict(<class 'list'>, {'fruit': ['apple', 'cherry'], 'meat': ['steak']})

# sets
seen = defaultdict(set)
seen['users'].add('vela')
seen['users'].add('adam')
seen['users'].add(20)

print(seen) # defaultdict(<class 'set'>, {'users': {20, 'adam', 'vela'}})