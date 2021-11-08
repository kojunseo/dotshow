# imgdot
    We generate image to text on terminal
    It is made for linux server to show image.
    When we want to see image on python  linux server, 
    we have to save image or use jupyter notebook.

    To see thumnail of the image, we can use cv2.imshow in local environment.
    However, it is impossible for server ssh terminal.
    It is simple thumnail printer using python.
    
# How to use
### Git cloning on your repository
    git clone https://github.com/KorKite/imgdot
    
## import package on python
### cv2 version
    import cv2
    from imgdot import thumshow
    img = cv2.imread(<img-path>)
    thumshow(img) # run the code

### PIL Image version
    import numpy as np
    from PIL import Image
    from imgdot import thumshow
    img = np.array(Image.open(<img-path>))
    thumshow(img) # run the code

# Example
    We can print images like down below.
<img width="300" alt="before" src="https://user-images.githubusercontent.com/50725139/140743113-9db67704-0a93-4f58-9542-a893b915a543.png">
<img width="300" alt="after" src="https://user-images.githubusercontent.com/50725139/140743199-64cac4d2-08be-4b23-9f21-393b2577bc51.png">

<img width="300" alt="before" src="https://user-images.githubusercontent.com/50725139/140743399-5daf658c-085e-44f5-8e65-d9821f53512d.png">
<img width="300" alt="after" src="https://user-images.githubusercontent.com/50725139/140743425-35af69bf-3aca-4105-9c3b-4540b846ad7f.png">
