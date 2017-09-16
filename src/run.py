import os
from dataset.sunnybrook import read_sunnybrook_images


DIR_SUNNYBROOK= '/data/sunnybrook'
FILE_SUNNYBROOK_IMAGES = 'SCD_DeidentifiedImages.zip'
PATH_SUNNYBROOK_IMAGES = os.path.join(DIR_SUNNYBROOK, FILE_SUNNYBROOK_IMAGES)


def main():
    read_sunnybrook_images(PATH_SUNNYBROOK_IMAGES)


if __name__ == '__main__':
    main()
