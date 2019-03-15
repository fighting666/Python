import jieba
import jieba.analyse
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
import numpy as np
import random
import os, struct
from array import array as pyarray
from numpy import append, array, int8, uint8, zeros
from matplotlib import pyplot as plt

class NeuralNet(object):
    
    # 初始化神经网络，sizes是神经网络的层数和每层神经元个数
    def __init__(self, sizes):
        self.sizes_ = sizes
        self.num_layers_ = len(sizes)  # 层数
        self.w_ = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]  # w_、b_初始化为正态分布随机数
        self.b_ = [np.random.randn(y, 1) for y in sizes[1:]]
    
    # Sigmoid函数，S型曲线，
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))
    # Sigmoid函数的导函数
    def sigmoid_prime(self, z):
        return self.sigmoid(z)*(1-self.sigmoid(z))
    
    def feedforward(self, x):
        for b, w in zip(self.b_, self.w_):
            x = self.sigmoid(np.dot(w, x)+b)
        return x
    
    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.b_]
        nabla_w = [np.zeros(w.shape) for w in self.w_]
        
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.b_, self.w_):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)
        
        delta = self.cost_derivative(activations[-1], y) * \self.sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        
        for l in range(2, self.num_layers_):
            z = zs[-l]
            sp = self.sigmoid_prime(z)
            delta = np.dot(self.w_[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
    
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.b_]
        nabla_w = [np.zeros(w.shape) for w in self.w_]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.w_ = [w-(eta/len(mini_batch))*nw for w, nw in zip(self.w_, nabla_w)]
        self.b_ = [b-(eta/len(mini_batch))*nb for b, nb in zip(self.b_, nabla_b)]
    
    
    # training_data是训练数据(x, y);epochs是训练次数;mini_batch_size是每次训练样本数;eta是learning rate
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data:
            n_test = len(test_data)
            
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test))
            else:
                print("Epoch {0} complete".format(j))
                
        def evaluate(self, test_data):
        test_results = [(self.feedforward(x).tolist().index(max(self.feedforward(x))), y.tolist().index(max(y))) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)
    
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
    
    # 预测
    def predict(self, data):
        value = self.feedforward(data)
        return value.tolist().index(max(value))
    
    # 保存训练模型
    def save(self):
        # 把w_和b_保存到文件(npy)
        np.save("D:\para\para_w test.npy",self.w_)
        np.save("D:\para\para_b test.npy",self.b_)
    def load(self):
        # 加载w和b，构建模型
        self.w_=np.load("D:\para\para_w test.npy").tolist()
        self.b_=np.load("D:\para\para_b test.npy").tolist()

if __name__ == '__main__':
    f=open(r'D:\数据分析项目\3-项目组\代扣失败原因分类\代扣失败原因分类测试.csv')
    remark=pd.read_csv(f)
    
    #自定义词典
    jieba.load_userdict(r'D:\数据分析项目\3-项目组\代扣失败原因分类\dict.txt')
    sentence_list=[]
    for sentence in remark.iloc[:,0]:
        segs = jieba.cut(str(sentence), cut_all=False)
        #去除停用词
        stopwords = {}.fromkeys(['?','的','亲','您','该','了',' '])
        final=''
        for seg in segs:
            if seg not in stopwords:
                final+=seg
                
        seg_list = jieba.cut(final, cut_all=False)
        sentence_list.append(" ".join(seg_list))
        
    #将文本中的词语转换为词频矩阵  
    vectorizer = CountVectorizer()  
    #计算个词语出现的次数  
    X = vectorizer.fit_transform(sentence_list)   
    #转为数组  
    arr=X.toarray()
    #添加标签
    Y = vectorizer.fit_transform(remark.iloc[:,1])
    brr=Y.toarray()
    class_list=vectorizer.vocabulary_
    class_list = dict(zip(class_list.values(), class_list.keys()))
    #构建训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(arr[remark.iloc[:,2]!=3], brr[remark.iloc[:,2]!=3], test_size=0.3, random_state=0)
    x_train=np.reshape(x_train,(len(x_train),len(x_train[0]),1))
    x_test=np.reshape(x_test,(len(x_test),len(x_test[0]),1))
    y_train=np.reshape(y_train,(len(y_train),len(y_train[0]),1))
    y_test=np.reshape(y_test,(len(y_test),len(y_test[0]),1))    
    train_set=list(zip(x_train,y_train))
    test_set=list(zip(x_test,y_test))
    
    #构建神经网络
    INPUT = len(x_train[0])
    OUTPUT = len(y_train[0])   
    net = NeuralNet([INPUT, 42, OUTPUT])
    net.SGD(train_set, 200, 100, 3.0, test_data=test_set)
    #准确率
    correct = 0
    for test_feature in test_set:
        if net.predict(test_feature[0]) == test_feature[1].tolist().index(max(test_feature[1])):
            correct += 1
    print("准确率: ", correct/len(test_set))
    net.save()
    #测试待分类集
    test_result=[]
    x_extra_test=np.reshape(arr[remark.iloc[:,2]==3],(len(arr[remark.iloc[:,2]==3]),len(arr[remark.iloc[:,2]==3][0]),1))
    for test_feature in x_extra_test:
        test_result.append(class_list[net.predict(test_feature)])
    result=pd.DataFrame(test_result,remark[remark.iloc[:,2]==3]['REMARK'].tolist())
    result.to_csv(r'D:\数据分析项目\3-项目组\代扣失败原因分类\代扣失败原因分类测试结果.csv')