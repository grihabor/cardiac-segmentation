# Cardiac Segmentaion 
Implementaion of neural network algorithm for cardiac MRI segmentation task

## How to run
1. Create `sunnybrook/` directory 
2. Download [Sunnybrook dataset](http://www.cardiacatlas.org/studies/sunnybrook-cardiac-data/) .zip files and store them in `sunnybrook/`
3. Edit `docker/env.sh` file: set path for `sunnybrook/`
4. Run `source env.sh`   
5. Run `make`

## Links
 - Previous Caffe implementation - [grihabor/heart-segm](https://github.com/grihabor/heart-segm) 
 - [Fully Convolutional Networks for Semantic Segmentation](https://arxiv.org/pdf/1605.06211.pdf)
 - [Efficient and generalizable statistical models of shape and appearance for analysis of cardiac MRI](https://pdfs.semanticscholar.org/a8e0/4dcc2b230a626ab56c898bcfdf5e3591180c.pdf)
 - [Deconvolutional Networks](http://www.matthewzeiler.com/wp-content/uploads/2017/07/cvpr2010.pdf)
