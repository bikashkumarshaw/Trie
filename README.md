# Trie DS:
#### Provides prefix matches for queried initials

How to use:
```
python my_trie.py --file `input the file name containig the vocabs, 1 word each line` --prefix `enter the starting letters of word to be searched`
```

### Eg.

```
python my_trie.py --file test.txt --prefix Bi

test.txt file contents:

Bikash
bison
big
kumar
shaw
sunny
sun
kumar
shaw
bitter
sunflower
bill

Output:

python my_trie.py --file test.txt --prefix Bi

bikash
bison
big
bitter
bill
```
