# Cyrus Beck Algorithm Python

## Project Details

[Cyrus Beck Algorithm](https://en.wikipedia.org/wiki/Cyrus%E2%80%93Beck_algorithm) implementation in Python. Could not find an implementation in Python, so I made one myself.

## Instructions

Set the bounding box coordinates

```python
x_min, y_min = 4, 4
x_max, y_max = 10, 8
```

Call the function CyrusClipping(x0, y0, x1, y1) where (x0, y0) and (x1, y1) is the starting and ending points of the line

```python
CyrusClipping(7, 9, 11, 4)
```

To show calculations

```python
SHOW_CALCULATION = True
```

## TODO

Clean up how function is called and how bounding box coordinates are set