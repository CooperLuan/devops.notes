# IPython Note

## [Interactive demos with IPython](http://ipython.org/ipython-doc/stable/interactive/reference.html)

- `# <demo> --- stop ---`
- `# <demo> silent`
- `# <demo> auto`

## Output

- convert by `nbconvert` to HTML/PDF/Slide shows
- `nbviewer` view notebook on web

## [ipcuster](http://ipython.org/ipython-doc/2/parallel/parallel_intro.html#getting-started)

start cluster by `ipcluster start -n 4`, then run

```
In [1]: from IPython.parallel import Client

In [2]: c = Client()

In [4]: c.ids
Out[4]: set([0, 1, 2, 3])

In [5]: c[:].apply_sync(lambda : "Hello, World")
Out[5]: [ 'Hello, World', 'Hello, World', 'Hello, World', 'Hello, World' ]
```

## skip parallel part
