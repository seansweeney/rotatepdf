# Rotate PDF
Python script to do simple rotation of all pages of an input PDF by a given amount.

## Requirements
Requires PyPDF2.

```sh
pip install pypdf2
```

## Usage
`rotatepdf.py <in file> <rotation> [<out file>]`

  `<in file>`   Input PDF.  
  `<rotation>`  Clockwise rotation in degrees (use negative numbers for counterclockwise).  
  `<out file>`  Output PDF (optional).  Defaults to input file name plus '-rotated' suffix.  
  
## Examples
`rotatepdf.py documentation.pdf 90`  
`rotatepdf.py landscan.pdf -90 portscan.pdf`
