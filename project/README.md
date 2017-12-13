## Installation
  The Python scripts run with Python3 (3.5 to be exact).

  
  Assuming install for MAC OS
  To run this program the following must be installed via these pip commands within python terminal:
  * For Preprocessing and OCR:
  
```
    $ pip3 install Pillow
    $ pip3 install pytesseract
    $ pip3 install opencv-python
```
  * For Data Collection
```
    $ pip3 install pyobjc-core
    $ pip3 install pyobjc
    $ pip3 install selenium
```
  Along with theses pip3 installs, you will also need to install tesseract library which can be done with the following howebrew command:
```
  $ brew install tesseract
```
  Selenium requires the chromedriver which can be found here (if it is not already included): 
```
    http://www.seleniumhq.org/download/    
```
  Selenium also requires the PATH to the folder in which the chromdriver exists. The command to do so is:
```
  $ export PATH=$PATH:/Directory/containing/driver/
```