#coding:UTF-8

# ニューロン
class Neuron:
    input_sum = 0.0
    output = 0.0

    def setInput(self, inp):
        self.input_sum += inp

    def getOutput(self):
      self.output = self.input_sum
      return self.output

# ニュートラルネットワーク
class NeuralNetwork:
    #　ニューロンのインスタンス
    neuron = Neuron()
    # 実行
    def commit(self, input_data):
        for data in input_data:
            self.neuron.setInput(data)
        #for構文でdataを加算し切ったinput_sumをoutputに代入する処理
        return self.neuron.getOutput()

# ニュートラルネットワークのインスタンス
neural_network = NeuralNetwork()

#　実行
trial_data =(1.0, 2.0, 3.0)
print neural_network.commit(trial_data)