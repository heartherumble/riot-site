Date: 2011-01-30
Title: Timing Code Execution in Python
Tags: python, execution, timing
Slug: timing-code-execution-in-python


I wrote an implementation of the [Levenshtein algorithm](http://en.wikipedia.org/wiki/Levenshtein_distance) in python a few days back, and today while noodling around, I came across another implementation of the same algorithm, written by [Magnus Hetland](http://hetland.org) the author of [Python Algorithms](http://www.amazon.com/Python-Algorithms-Mastering-Basic-Language/dp/1430232374/) and wanted to see which was the "faster" implementation.

So, enter the [timeit()](http://docs.python.org/library/timeit.html) module in python. Here's what I did:

    #!python
    >>> def levenshtein(a,b):
    ...     "Magnus's Code"
    ...     
    ...     [ Code here ]
    ...   
    >>> def leven(a,b):
    ...     "Rohit's Code"
    ...     
    ...     [ Code here ]
    ...     
    >>> import timeit
    >>> t1 = timeit.Timer(setup='from __main__ import levenshtein', stmt='levenshtein("plumber","causes")').timeit()
    >>> t1
    50.655728101730347
    >>> t2 = timeit.Timer(setup='from __main__ import leven', stmt='leven("plumber","causes")').timeit()
    >>> t2
    68.573153972625732

Seems like Magnus has me beat :(.

One point to note here is that timeit() temporarily turns off garbage collection, so if your code requires it you will need to add it in.

    #!python
    >>> import gc
    >>> setup = """\
    ... from __main__ import levenshtein
    ... gc.enable()
    ... """
    >>> t2 = timeit.Timer(setup=setup, stmt='levenshtein("plumber","causes")').timeit()

There is also quite a nice collection of python performance tips [here](http://wiki.python.org/moin/PythonSpeed/PerformanceTips).
