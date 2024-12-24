culour: color in curses
========================

.. image:: https://img.shields.io/pypi/v/culour.svg
    :target: https://pypi.python.org/pypi/culour
    
Print colored strings in curses windows easily

The problem
-----------
There's no way to print pre-formatted, colored terminal text into curses.
If you're printing ``\033[94m Blue``, which in regular bash terminal is a nice-blue text,
in curses, it will be printed as ``^[[94m Blue``

Solution
--------
Use culour (pronounced 'cooler') to print the colored strings onto your curses window.
Instead of using:

.. code:: python

	window.addstr("colored string")

Simply use:

.. code:: python

	import culour
	culour.addstr(window, "colored string")


And your string will be added to the screen nice and colored.

To print to a specific place in the screen, use:

.. code:: python

	culour.addstr(window, y, x, "colored string")


Don't forget to initialize the color usage in your curses window by calling ``curses.start_color()`` immediately after ``curses.initscr()``
