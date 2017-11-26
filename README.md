# EEE-ICR 15-122 Project
"An extremely exceedingly exceptionally intelligent character recognizer"


A user-friendly program that takes images with handwritten text as input and recognizes the text and saves it in a text file.

How to run:
download all the files in the repository
run trial.py

Restrictions:
Scanned image must be of high quality
Scanned image must only contain lowercase English letters
Scanned image must have as minimal noise in the background as possible
***Failure to meet these requirements will affect the handwritten recognition

Libraries:
In order to run this program, the user needs to have scikit learn library installed. There are other libraries and modules that are used in the code, such as skimage, PIL image, and tkinter, but all of them are either pre-installed with python or with scikit learn.

I would recommend, however, that the user installs sci-kit learn through Anaconda which ensure that all of the other libararies are installed as well.


How it works:
Samples of handwritten letters were colected from students. Then these samples were cropped using the file Cropping Samples.py
Then, these samples were further cropped using the file further crop.py to standardize their shapes for accurate results
Then, two main features were extracted from each sample and saved into a text file :Histogram of Gradients and Daisy Features, this was done using the files hog.py and dz_features.py
Then, a neural network classifier was trained on these features, and the trained classifier was saved as a file to avoid having to retrain it -this was done using the file newclg.py **it should have been newclf, that was a typo**
Then, the file Segmentation.py does all the work of taking an input image, cropping it, extracting its features, recognizing the letters, and converting them into sentences.
trial.py is the gui implementation of the program.



If you have any issues or inquiries, please contact me at loe@andrew.cmu.edu
