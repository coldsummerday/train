import tensorflow as tf 
import argparse
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def getImage(filename):
    image = tf.gfile.FastGFile(filename,'rb').read()
    return image

def getLabels(labelsName):
    labels = []
    for label in tf.gfile.GFile(labelsName):
        labels.append(label.rstrip())
    return labels
def getGraph(graphName):
    with tf.gfile.FastGFile(graphName,'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def,name='')
def init():
    paser=argparse.ArgumentParser()
    paser.add_argument('-i','--image',help='imagefile',type=str)
    paser.add_argument('-l','--lable',help='lablefile',type=str)
    paser.add_argument('-g','--graph',help='graphfile',type=str)
    args=paser.parse_args()
    if args.image and args.lable and args.graph:
        return (args.image,args.lable,args.graph)
    else:
        return (None,None,None)
if __name__=="__main__":

    (imagefile,lablefile,graphfile) = init()
    if imagefile == None:
        exit("请输出正确文件路径")

    else:
        labels = getLabels(lablefile)
        image = getImage(imagefile)
        getGraph(graphfile)
        with tf.Session() as sess:
            softmax_tensor = tf.get_default_graph().get_tensor_by_name('final_result:0')
            predict = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image})

            top = predict[0].argsort()[-len(predict[0]):][::-1]
            for index in top:
                human_string=labels[index]
                score=predict[0][index]
                print(human_string,score)
