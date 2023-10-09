import cv2
import numpy as np


# def sharpen_image(input_path, output_path):
#     image = cv2.imread(input_path)
#     # 转换为浮点类型
#     image = image.astype(np.float32)

#     # 定义锐化滤波器
#     kernel = np.array([[0, -1, 0],
#                        [-1, 5, -1],
#                        [0, -1, 0]])

#     # 应用锐化滤波器
#     sharpened_image = cv2.filter2D(image, -1, kernel)

#     # 将像素值限制在0到255之间
#     sharpened_image = np.clip(sharpened_image, 0, 255)

#     # 转换回整数类型
#     sharpened_image = sharpened_image.astype(np.uint8)
#     cv2.imwrite(output_path, sharpened_image)

def sharpen_image(source):
    # 转换为浮点类型
    image = source.astype(np.float32)

    # 定义锐化滤波器
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # 应用锐化滤波器
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # 将像素值限制在0到255之间
    sharpened_image = np.clip(sharpened_image, 0, 255)

    # 转换回整数类型
    ret = sharpened_image.astype(np.uint8)
    return ret


if __name__ == '__main__':
    input_path = 'C:/Users/jin_j/Desktop/enhancement.jpg'
    output_path = 'C:/Users/jin_j/Desktop/tmp.jpg'
    sharpen_image(input_path, output_path)