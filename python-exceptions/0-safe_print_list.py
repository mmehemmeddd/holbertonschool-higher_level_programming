def safe_print_list(my_list=[], x=0):
    count = 0                          # tracks how many were actually printed

    for i in range(x):                 # loop up to x times
        try:
            print(my_list[i], end="")  # print element, no space/newline
            count += 1                 # only increments if no error
        except IndexError:
            break                      # list ran out, stop the loop

    print()                            # the final newline after all elements
    return count                       # return real number printed
```

---

## Step-by-Step Explanation

| Line | What it does |
|---|---|
| `count = 0` | Our counter — replaces `len()` |
| `for i in range(x)` | Try to loop `x` times |
| `try:` | Attempt to access `my_list[i]` |
| `print(my_list[i], end="")` | Print without newline/space so all elements stay on one line |
| `count += 1` | Only runs if the print succeeded (no error) |
| `except IndexError:` | Catches when `i` goes past the list's last index |
| `break` | Stops the loop cleanly when list is exhausted |
| `print()` | Prints the final newline after all elements |
| `return count` | Returns the real number printed |

---

## Tracing Through Each Test Case

**Case 1: `safe_print_list([1,2,3,4,5], 2)`**
```
i=0 → try my_list[0]=1 ✅ → print "1", count=1
i=1 → try my_list[1]=2 ✅ → print "2", count=2
loop ends (range(2) done)
print()  → newline
return 2
```
Output: `12\nnb_print: 2`

**Case 2: `safe_print_list([1,2,3,4,5], 5)`**
```
i=0..4 → all succeed → count=5
return 5
```
Output: `12345\nnb_print: 5`

**Case 3: `safe_print_list([1,2,3,4,5], 7)` ← x bigger than list**
```
i=0..4 → all succeed → count=5
i=5 → my_list[5] → IndexError! → break
return 5   ← not 7, the real count
