import numpy as np
from PIL import Image

img = Image.open("static/img/temp_img.jpeg")
img = img.convert("RGB")

img_arr = np.asarray(img)
#img_arr.setflags(write=1)
new_size = ((img_arr.shape[0]//2), (img_arr.shape[1]//2), img_arr.shape[2])
new_arr = np.full(new_size, 255)
print(img_arr.shape, new_size)
new_arr.setflags(write=1)

img_arr_shape = img_arr.shape

for row in range(img_arr_shape[0]):
    for col in range(img_arr_shape[1]):
        try:
            new_arr[row,col,0] = (int(img_arr[row,col,0]) + int(img_arr[row+1,col,0]) + int(img_arr[row,col+1,0]) + int(img_arr[row+1,col+1,0])) // 4
            new_arr[row,col,1] = (int(img_arr[row,col,1]) + int(img_arr[row+1,col,1]) + int(img_arr[row,col+1,1]) + int(img_arr[row+1,col+1,1])) // 4
            new_arr[row,col,2] = (int(img_arr[row,col,2]) + int(img_arr[row+1,col,2]) + int(img_arr[row,col+1,2]) + int(img_arr[row+1,col+1,2])) // 4
        except:
            break
        col += 1
    row += 1

new_arr = np.uint8(new_arr)
img_new = Image.fromarray(new_arr)
#img_new = img_new.convert("RGB")
img_new.show()
