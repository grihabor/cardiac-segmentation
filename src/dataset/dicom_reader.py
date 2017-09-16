import os
import png
import dicom
import logging

import numpy as np

logger = logging.getLogger(__name__)


def get_dicom_image(content):
    try:
        img = content.pixel_array
    except ValueError as e:
        logger.warning(e)
        pixel_data = content.PixelData
        numpy_pixel_data_8 = np.fromstring(pixel_data, dtype=np.uint8)
        numpy_pixel_data_16 = np.fromstring(pixel_data, dtype=np.uint16)
        # print(np.max(numpy_pixel_data_8))
        # print(np.max(numpy_pixel_data_16))
        # data = numpy_pixel_data

        normalized_pixel_data = numpy_pixel_data_16.astype(np.float64) / content.LargestImagePixelValue
        data = (normalized_pixel_data * 255).astype(np.uint8)

        width = content.Columns

        tail = data.shape[0] % width
        if tail != 0:
            padding = width - tail
            logger.warning(f'Added padding: {padding}')
            data = np.append(data, np.zeros((padding,)))

        img = np.reshape(data, (-1, width))
        # img = np.reshape(data, (content.Rows, -1))
    print(img.shape)
    return img


def save_as_png(arr, path):
    writer = png.Writer(
        height=arr.shape[0],
        width=arr.shape[1],
        bitdepth=8,
        greyscale=True
    )
    with open(path, 'wb') as f:
        writer.write(f, arr)


def read_dicom(path):
    content = dicom.read_file(path)
    print(content)
    img = get_dicom_image(content)
    filename = os.path.split(path)[-1]
    save_as_png(img, f'/data/cache/{filename}.png')


