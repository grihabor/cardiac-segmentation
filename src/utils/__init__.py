import png


def save_as_png(arr, path):
    writer = png.Writer(
        height=arr.shape[0],
        width=arr.shape[1],
        bitdepth=8,
        greyscale=True
    )
    with open(path, 'wb') as f:
        writer.write(f, arr)

