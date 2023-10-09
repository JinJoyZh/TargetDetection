
from defog_SDCP import SDCP
from sharpen import sharpen_image
from pathlib import Path
import cv2
import os
import glob

IMG_FORMATS = ['bmp', 'dng', 'jpeg', 'jpg', 'mpo', 'png', 'tif', 'tiff', 'webp']  # include image suffixes
VID_FORMATS = ['asf', 'avi', 'gif', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'wmv']  # include video suffixes

def preprocess(input_path, output_path):
    p = str(Path(input_path).resolve()) 
    if os.path.isdir(p):
        files = sorted(glob.glob(os.path.join(p, '*.*')))  # dir
    elif os.path.isfile(p):
        files = [p]  # files
    else:
        raise Exception(f'ERROR: {p} does not exist')
    images = [x for x in files if x.split('.')[-1].lower() in IMG_FORMATS]
    videos = [x for x in files if x.split('.')[-1].lower() in VID_FORMATS]
    files = images + videos
    ni, nv = len(images), len(videos)
    nf = ni + nv  # number of files
    video_flag = [False] * ni + [True] * nv
    for i in range(nf):
        path = files[i]
        dir, file_name = os.path.split(path)
        new_file_name = "enhanced_" + file_name
        dst_path = os.path.join(output_path, new_file_name)
        if video_flag[i]:
            # Read video
            cap = cv2.VideoCapture(path)
            ret_val, img0 = cap.read()
            if not ret_val:
                continue
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            fps = 25
            width = img0.shape[1]
            height = img0.shape[0]
            dst_path = dst_path[:dst_path.rindex('.')] + '.mp4'
            video_writer = cv2.VideoWriter(dst_path, fourcc, fps, (width, height))
            while True:
                if not ret_val:
                    break
                ret_val, img0 = cap.read()
                tmp = SDCP(img0)
                enhanced = sharpen_image(tmp)
                #save video
                video_writer.write(enhanced)
            video_writer.close()
        else:
            # Read image
            img0 = cv2.imread(path)  # BGR
            assert img0 is not None, f'Image Not Found {path}'
            tmp = SDCP(img0)
            enhanced = sharpen_image(tmp)
            #save image
            cv2.imwrite(dst_path, enhanced)


if __name__ == '__main__':
    input_path = 'C:/Users/jin_j/Desktop/in'
    output_path = 'C:/Users/jin_j/Desktop/out'
    preprocess(input_path, output_path)