import dicom
import logging

import numpy as np

logger = logging.getLogger(__name__)


def get_dicom_image(content):
    try:
        img = content.pixel_array
    except ValueError as e:
        logger.warning(e)
        raw = content.PixelData
        data = np.fromstring(raw, dtype=np.uint8)  # np.array

        tail = data.shape[0] % content.Columns
        if tail != 0:
            padding = content.Columns - tail
            logger.warning(f'Added padding: {padding}')
            data = np.append(data, np.zeros((padding,)))
            print(data.shape, data.shape[0] % content.Columns)

        img = np.reshape(data, (-1, content.Columns))

    return img


def read_dicom(filename):
    content = dicom.read_file(filename)
    print(content)
    img = get_dicom_image(content)
    numpy


