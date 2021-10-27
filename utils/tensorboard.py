# from PIL import Image
# import scipy.misc
# from io import BytesIO
# import tensorboardX as tb
# from tensorboardX.summary import Summary

# class TensorBoard(object):
#     def __init__(self, model_dir):
#         self.summary_writer = tb.FileWriter(model_dir)

#     def add_image(self, tag, img, step):
#         summary = Summary()
#         bio = BytesIO()

#         if type(img) == str:
#             img = Image.open(img)
#         elif type(img) == Image.Image:
#             pass
#         else:
#             img = Image.fromarray(img)

#         img.save(bio, format="png")
#         image_summary = Summary.Image(encoded_image_string=bio.getvalue())
#         summary.value.add(tag=tag, image=image_summary)
#         self.summary_writer.add_summary(summary, global_step=step)

#     def add_scalar(self, tag, value, step):
#         summary = Summary(value=[Summary.Value(tag=tag, simple_value=value)])
#         self.summary_writer.add_summary(summary, global_step=step)
from PIL import Image
from io import BytesIO
import tensorboardX as tb
from tensorboardX import SummaryWriter
from tensorboardX.summary import Summary
import numpy as np

class TensorBoard(object):
    def __init__(self, model_dir):
        self.summary_writer = SummaryWriter(model_dir)
    def add_image(self, tag, img, step):
        ''' Expects channels last rgb image '''
        img = np.array(img)
        if len(img.shape) == 2:
            img = Image.fromarray(img)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = np.array(img)
        img = np.transpose(img, (2, 0, 1))
        self.summary_writer.add_image(tag, img)

    def add_scalar(self, tag, value, step):
        self.summary_writer.add_scalar(tag, value, step)

    def add_text(self, tag, text, step):
        self.summary_writer.add_text(tag, text, step)