#coding:UTF-8
import math

#シグモイド関数
def sigmoid(a):
    return 1.0/(1.0 + math.exp(-a))

# ニューロン
class Neuron:
    input_sum = 0.0
    output = 0.0

    def setInput(self, inp):
        self.input_sum += inp

    def getOutput(self):
      self.output =sigmoid(self.input_sum)
      return self.output

# ニュートラルネットワーク
class NeuralNetwork:
    #　入力の重み
    w =(1.5,-2.5,-0.5)
    #　ニューロンのインスタンス
    neuron = Neuron()
    # 実行
    def commit(self, input_data):
        self.neuron.setInput(input_data[0] * self.w[0])
        self.neuron.setInput(input_data[1] * self.w[1])
        self.neuron.setInput(input_data[2] * self.w[2])
        return self.neuron.getOutput()

# 基準点(データの範囲を0.0～1.0の範囲に収める為)
refer_point_0 = 34.5
refer_point_1= 137.5

# ファイルの読み込み
trial_data=[]
trial_data_file =open("trial_data","r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    trial_data.append([float(line[0]) - refer_point_0, float(line[1])- refer_point_1])
trial_data_file.close()

print trial_data

# ニュートラルネットワークのインスタンス
neural_network = NeuralNetwork()

#　実行
trial_data =(1.0, 2.0, 3.0)
print neural_network.commit(trial_data)