# culour
Print colored strings in curses windows easily

### The problem
There's no way to print pre-formatted, colored terminal text into curses.
If you're printing '\033[94m Blue', which in regular bash terminal is a nice-blue text,
in curses, it will be printed as '^[[94m Blue'

### Solution
Use culour (pronounced 'cooler') to print the colored strings onto your curses window.
Instead of using:
```python
window.addstr("colored string")
```
Simply use;
```python
import culour
culour.addstr(window, "colored string")
```

And your string will be added to the screen nice and colored.
