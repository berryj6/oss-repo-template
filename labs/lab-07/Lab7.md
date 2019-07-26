# Lab 7

## 1

**chaos to order:**

- chaos
- chats
- coats
- colts
- colas
- codas
- codes
- coder
- cider
- eider
- elder
- older
- order


**nodes to graph:**

- nodes
- modes
- moles
- molds
- golds
- goads
- grads
- grade
- grape
- graph

**moron to smart:**

- moron
- boron
- baron
- caron
- capon
- capos
- capes
- canes
- banes
- bands
- bends
- beads
- bears
- sears
- stars
- start
- smart

**flies to swims:**

- flies
- flits
- slits
- slims
- swims

**mango to peach:**

- mango
- mange
- marge
- merge
- merse
- terse
- tease
- pease
- peace
- peach

**pound and marks:**

None

## 2

**cold to warm:**

- cold
- cord
- word
- worm
- warm

**love to hate:**

- love
- hove
- have
- hate

**good to evil:**

None

**pear to beef:**

- pear
- bear
- beer
- beef

**make to take:**

- make
- take

## 3

The ```edit_distance_one``` function was changed to the following.

```python
def edit_distance_one(word):
    for i in range(len(word)):
        left, c, right = word[0:i], word[i], word[i + 1:]
        j = lookup[c]  # lowercase.index(c)
        for cc in lowercase[j + 1:]:
            results = itertools.permutations(left + cc + right)
            for result in results:
                yield ''.join(result)
```

This edit distance function yield the following results:

**chaos to order:**

- chaos
- echos
- chore
- coder
- order

**nodes to graph:**

- nodes
- shoed
- hades
- heaps
- phage
- graph

**moron to smart:**

- moron
- moors
- morts
- smart

**flies to swims:**

- flies
- slime
- semis
- swims

**mango to peach:**

- mango
- conga
- capon
- poach
- peach

**pound to marks:**

- pound
- sound
- modus
- drums
- mrads
- marks
