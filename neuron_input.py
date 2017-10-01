#coding:UTF-8

# ニューロン
class Neuron:
    # 入力値の合計を入れる変数
    input_sum = 0.0

    # 入力値をinput_sumに足し合わせる
    def setInput(self, inp):
        self.input_sum += inp
        print self.input_sum

# ニュートラルネットワーク
class NeuralNetwork:
    #　ニューロンのインスタンス
    neuron = Neuron()
    # 実行
    def commit(self, input_data):
        for data in input_data:
            self.neuron.setInput(data)

# ニュートラルネットワークのインスタンス
neural_network = NeuralNetwork()

#　実行
trial_data =(1.0, 2.0, 3.0)
#　trial_dataがcommitメソッドのinput_dataに代入される
neural_network.commit(trial_data)