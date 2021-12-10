# OCR Diagram Tools

This suite of tools is to help create a simpler way to get braille diagrams made.
This works upon the *original* image and does not create a new diagram from scratch.
I believe this is optimal for most cases.

You can run each tool individually with `cargo run --bin <binary_name_here> [arg1] [arg2]`.

Go to `braille-diagram-tools` to use the binaries.

## btt-get-ocr

`btt-get-ocr [diagram.png] [out.json]`

This program take the image at `diagram.png` (this is the default value) and output OCR data in JSON format into `out.json` (default).

## btt-label-ocr

`btt-label-ocr [diagram.png] [out.json]`

This program takes the OCR data and lays it overtop the diagram.
How so?
It adds a rectangular box around each OCRed piece of text, along with a label (usually a number starting from 0) to the left of the box.
This allows you to see how acurate the OCR was and to change what is broken with this next tool:

## btt-edit-tools

`btt-edit-tools [out.json]`

The program edits the json (NOT in place) with advanced manipulation functions to help with OCR-related tasks.
The id to the left of the box is very useful right about now.

Here is a list of all the commands you can use while running `btt-edit-tools`:

```
merge|id1|id2 # merges two OCRed sections together, least of x and y to greatest of x+width and y+height.
vsplit|id # split OCRed section into top and bottom pieces.
hsplit|id # split OCRed section into left and right pieces.
add|x|y|w|h # add a new OCR section with x, y, width and height.
rem|id # remove an OCR section
triml|id|dw # change width by dw (delta width)
trimr|id|dw # change width by dw (delta width) and move x the same amount (plus)
trimt|id|dh # change height by dh (delta height) and move y the same amount (minus)
trimb|id|dh # change height by dh (delta height)
movel|id|dx # change x by dx (positive = left move)
mover|id|dx # change x by dx (positive = right move)
moveu|id|dy # change y by dy (positive = upward move)
moved|id|dy # change y by dy (positive = downward move)
paddl|id|dx # change x by dx and add to width same amount
paddr|id|dx # add dx to width
paddt|id|dy # negate dy from y
paddb|id|dy # add dy to height
text|id|some string # make the text of some string (used for braille printing later) associated with id
save|filename # save current json data to filename
```

**NOTE: currently, any command error will crash the program;
this will be fixed eventually.**

## btt-whiteout-labels

`btt-whiteout-labels [out.img] [out.json]`

This program takes an image and a json file and places a filled white box overtop all OCR sections.
This is useful before running the next tool.

## btt-add-braille

`btt-add-braille [out.img] [out.json] [font_size]`

This program takes an image and a json file and based upon the position (x,y) adds text of `font_size` (default `20.0`) where each OCR section is in the JSON.
This often does not work the first time due to the braille using more characters than standard print.
You'll generally need to go back to editing the json, running `whiteout` and running this tool a few times to get it just right.
