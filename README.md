# PaintRL

This repo contains project codes for CS 285: Deep Reinforcement Learning at UC Berkeley. Our work explores the human-like artisitc stylization with a model-based deep reinforcement learning painting agent. The code is adapted from the [repo](https://github.com/megvii-research/ICCV2019-LearningToPaint) by [Huang et al. 2019](https://arxiv.org/abs/1903.04411). 

## Train the model
Monitor the training progress using: `$ tensorboard --logdir=train_log --port=6006`
### Train Neural Renderer
```
$ python train_renderer.py
```
### Train the Actor
Please follow the code chunks in `CM.ipynb` and download the training data
For instance, train with our Approach 2 and Modified Perceptual Loss (CM+L1 & Style Loss), then run:
```
$ python train.py --debug --batch_size=12 --max_step=120 --loss_mode=cml1+style --dataset=celeb --style_type=img --canvas_color=white
```
