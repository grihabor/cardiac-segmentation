import dicom
import logging

import numpy as np

logger = logging.getLogger(__name__)


def get_dicom_image(content):
    pixel_data = content.PixelData
    numpy_pixel_data_16 = np.fromstring(pixel_data, dtype=np.uint16)

    factor = 255. / np.max(numpy_pixel_data_16)
    normalized_pixel_data = numpy_pixel_data_16.astype(np.float64) * factor
    data = normalized_pixel_data.astype(np.uint8)

    width = content.Columns

    tail = data.shape[0] % width
    if tail != 0:
        padding = width - tail
        logger.debug(f'Added padding: {padding}')
        data = np.append(data, np.zeros((padding,), dtype=np.uint8))

    img = np.reshape(data, (-1, width))
    logger.debug(f'Image: shape - {img.shape}, dtype - {img.dtype}')
    return img


def read_dicom_image(path):
    content = dicom.read_file(path)
    return get_dicom_image(content)