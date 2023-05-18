# Automatic Number-Plate Recognition
This project was created using Python with OpenCV to detect the number plates and EasyOCR to read the plates

## Setup
1. Install OpenCV   ```pip install open-cv python```

2. Install CUDA Toolkit from NVIDIA (Optional)\
CUDA Toolkit functions to process EasyOCR in reading text derived from images using the GPU. This can make processes run faster than using the CPU

3. Install Pytorch\
An Example when already have CUDA Toolkit\
```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117```\
\
Installing without CUDA :\
```pip install torch torchvision torchaudio ```

4. Install EasyOCR ```(https://github.com/JaidedAI/EasyOCR)```

## How to Use
1. Run ```plate_capture.py```\
Make sure the slot of the device that will be used to take pictures is correct

2. If ROI has detected your plate, press the 's' button\
\
![alt text](https://github.com/WaduheX99/ANPR-Python/blob/main/test/1.png?raw=true)\
\
![alt text](https://github.com/WaduheX99/ANPR-Python/blob/main/test/2.png?raw=true)\
\
![alt text](https://github.com/WaduheX99/ANPR-Python/blob/main/test/3.png?raw=true)\
\
The image will be saved in the plates folder with ```.jpg``` format

3. Open ```PlatesRead.ipynb``` using your favorite IPython Notebook editor like Jupyter Notebook, Google Colab, etc.

4. EasyOCR will read the plates along with the accuracy obtained
