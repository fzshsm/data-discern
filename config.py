# -*- coding: utf-8 -*-
import platform
import tensorflow as tf

tf.app.flags.DEFINE_integer('batch_size', 10, 'the batch_size')
tf.app.flags.DEFINE_string('checkpoint_dir', './checkpoint/', 'the checkpoint dir')
tf.app.flags.DEFINE_integer('image_height', 25, 'image height')
tf.app.flags.DEFINE_integer('image_width', 60, 'image width')
tf.app.flags.DEFINE_integer('image_channel', 1, 'image channels as input')
tf.app.flags.DEFINE_integer('max_stepsize', 64, 'max stepsize in lstm, as well as '
                                                'the output channels of last layer in CNN')
tf.app.flags.DEFINE_integer('num_hidden', 128, 'number of hidden units in lstm')
tf.app.flags.DEFINE_float('initial_learning_rate', 1e-3, 'inital lr')
tf.app.flags.DEFINE_float('decay_rate', 0.98, 'the lr decay rate')
tf.app.flags.DEFINE_integer('decay_steps', 10000, 'the lr decay_step for optimizer')

tf.app.flags.DEFINE_float('beta1', 0.9, 'parameter of adam optimizer beta1')
tf.app.flags.DEFINE_float('beta2', 0.999, 'adam parameter beta2')

pl = platform.platform()
if 'Window' in pl:
    #local
    # IMAGE_PATH = 'D:/web/data-center/runtime/gameData'
    IMAGE_PATH = 'D:/image'
    MYSQL = {'host':'127.0.0.1' , 'user' : 'root' , 'password' : '' , 'database' : 'game_data' , 'charset' : 'utf8'}
elif 'centos-7.4.1708' in pl :
    #dev
    IMAGE_PATH = '/webService/wwwroot/develop.datacenter.baidourank.com/runtime/gameData'
    MYSQL = {'host':'127.0.0.1' , 'user' : 'gamedata' , 'password' : 'gamedata!@#' , 'database' : 'game_data' , 'charset' : 'utf8'}
else:
    #product
    IMAGE_PATH = '/webService/wwwroot/datacenter.baidourank.com/runtime/gameData'
    MYSQL = {'host':'172.17.0.11' , 'user' : 'gamedata' , 'password' : 'gamedata!@#' , 'database' : 'game_data' , 'charset' : 'utf8'}


IMAGE_TEMP = './s_img'
IMAGE_CROP = {'width': 60, 'height': 25, 'wh' : 28 , 'x':(75 , 325 , 568 , 760 , 826 , 873 , 926) , 'y' : {'begin' : 2 , 'offset' : 50 , 'invalid' : 30 , 'whBegin' : 14 , 'whOffset' : 22} }

IMAGE = {'path': IMAGE_PATH, 'temp': IMAGE_TEMP, 'width' : 1030  , 'height' : 500}