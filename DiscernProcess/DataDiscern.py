
import cv2
import numpy as np
import tensorflow as tf
import config

from DiscernProcess import ImageDispose
from DiscernProcess import LSTMOCR

FLAGS = tf.app.flags.FLAGS
ImageDispose = ImageDispose.ImageDispose()

charset = '0123456789'
encode_maps = {}
decode_maps = {}
for i, char in enumerate(charset, 1):
    encode_maps[char] = i
    decode_maps[i] = char

SPACE_INDEX = 0
SPACE_TOKEN = ''
encode_maps[SPACE_TOKEN] = SPACE_INDEX
decode_maps[SPACE_INDEX] = SPACE_TOKEN

class DataDiscern:

    def infer(self , imgList):
        model = LSTMOCR.LSTMOCR('infer')
        model.build_graph()
        total_steps = int(len(imgList) / FLAGS.batch_size)
        config = tf.ConfigProto(allow_soft_placement=True)
        with tf.Session(config=config) as sess:
            sess.run(tf.global_variables_initializer())
            saver = tf.train.Saver(tf.global_variables(), max_to_keep=100)
            ckpt = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
            if ckpt:
                saver.restore(sess, ckpt)
                print('restore from ckpt{}'.format(ckpt))
            else:
                print('cannot restore')

            decoded_expression = []
            for curr_step in range(total_steps):
                imgs_input = []
                seq_len_input = []
                for img in imgList[curr_step * FLAGS.batch_size: (curr_step + 1) * FLAGS.batch_size]:
                    im = cv2.imread(img, 0).astype(np.float32) / 255.
                    im = np.reshape(im, [FLAGS.image_height, FLAGS.image_width, FLAGS.image_channel])
                    def get_input_lens(seqs):
                        length = np.array([FLAGS.max_stepsize for _ in seqs], dtype=np.int64)
                        return seqs, length
                    inp, seq_len = get_input_lens(np.array([im]))
                    imgs_input.append(im)
                    seq_len_input.append(seq_len)
                imgs_input = np.asarray(imgs_input)
                seq_len_input = np.asarray(seq_len_input)
                seq_len_input = np.reshape(seq_len_input, [-1])

                feed = {model.inputs: imgs_input,
                        model.seq_len: seq_len_input}
                dense_decoded_code = sess.run(model.dense_decoded, feed)
                for item in dense_decoded_code:
                    expression = ''

                    for i in item:
                        if i == -1:
                            expression += ''
                        else:
                            expression += decode_maps[i]

                    decoded_expression.append(expression)

            return decoded_expression