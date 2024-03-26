
#how to I do summation in python without libraries. need to do this function and output it. #Answer: add the variables like you do in the formula
x_input = [0,1]# 2 inputs. need to randomize it and make a while loop to take in user input
w_weights = [-0.2, 0.6, -0.4] # 3 weights
x1 = x_input[0]
x2 = x_input[1]
w0 = w_weights[0]
w1 = w_weights[1]
w2 = w_weights[2]
s = w0*1 + w1*x1 + w2*x2 #our sigmoid function
learningRate = 0.1
target = 0
def activationFunction(s):
#s is the weighted sum, 0 is the threshold
    if s > 0:
        return 1
    else:
        return -1

def perceptron():
    weighted_sum = 0
    for x,w in zip(x_input, w_weights):
        weighted_sum += x*w
        errorRate = activationFunction(s) - target
        updatedWeights1 = learningRate * errorRate * x1
        updatedWeights2 = learningRate * errorRate * x2
        print(weighted_sum)
        print(errorRate)
        print(updatedWeights1)
        print(updatedWeights2)


    return activationFunction(weighted_sum)



output =perceptron()
print("output: " + str(output))





''' def neuron(weights, x):
            #0.3, -1
            x = [1, 0]
            s = -0.2 + weights[0] * x[0] + weights[1] * x[1]
            output = activationFunction(s)
            return output
'''

