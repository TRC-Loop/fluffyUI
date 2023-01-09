![fluffyUILogo](https://github.com/TRC-Loop/fluffyUI/raw/7fa4cb61d452c982478d247b30a7ead5bfbb120f/other/logo-color.png)
#### A new way to make GUIs in the Console
##### (In python)
## What is fluffyUI?
fluffyUI is a library that allows you to make GUIs in the console. It is very easy to use and is very customizable.

## How do I use it?
To use fluffyUI all you need to is to exectute the following code:

`pip install fluffyui`

If that does not work
try this command
`py -m pip install fluffyui`

replace py with your python call method. Usually it is one of these:
`python` or `py` or `python3`

## How do I make a GUI?
First of all, choose what you need
- GridUI
    - For a grid based GUI
    - With Rows and Columns
    - Easy to use

- CoordinateUI
    - For a coordinate based GUI
    - With X and Y
    - More Percision placing of elements
    - Harder to use

- MapUI
    - For a map based GUI 
    - With X and Y
    - More Percision placing of elements, for games.

GridUI:
First of all, we initalize the Object.
```python
import fluffyui

gr = fluffyui.Grid(5, 1, show=True, repr_char_notshow="\t", empty_cell="")
 ```
Now with that knowledge we can set something in cells and print the whole thing:
```python
import fluffyui

gr = fluffyui.Grid(5, 1, show=True, repr_char_notshow="\t", empty_cell="")

gr.set(0, 0, "FluffyUI for Python.",align='center')
gr.set(1, 0, "Easy as that!", align='left')
gr.set(2, 0, "Time to make your", align='center')
gr.set(3, 0, "OWN GUI", align='right')
print(gr) # prints the whole thing with the settings you´ve made
print(gr.get(0, 0)) # gets a value from a cell
```

It is also compatible with the `with` statement:
```python
import fluffyui
with Grid(5, 1, show=True, repr_char_notshow="\t", empty_cell="") as gr:
    gr.set(0, 0, "FluffyUI for Python.", align='center')
    gr.set(1, 0, "Easy as that!", align='center')
    gr.set(2, 0, "Time to make your", align='center')
    gr.set(3, 0, "OWN GUI", align='center')
    print(gr)
    print(gr.get(0, 0))
````
Pretty easy huh?


We will be adding real-time updates soon, so you can make a GUI that updates in real-time.

and also a way to select things in the GUI (like buttons).

We have these planned:
- Label (To dispkay text)
- Button (To do something when clicked)
- TextBox (To get input from the user)
- AsciiImageBox (To display an image that was converted to ascii using the AsciiConv class)
- RealTimeLabel (To display text that updates in real-time)
- CodeLabel (To display code (like python) in a GUI)
- Separator (To separate things in the GUI or make borders)
- DropDownButton (To select something from a list of options)