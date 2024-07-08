import polars as pl
import matplotlib as plt


#find equivalent for iloc method in documentation

pData = pl.read_csv("california_housing_test.csv")

def gradient_descent(m_now, b_now, points, L):
    #L is the learning rate
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].median_house_value
        y = points.iloc[i].median_income

    m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
    b_gradient += -(2/n) * (y - (m_now * x + b_now))
    # encountering an overflow with the scalar multiply function. need to be more efficient and easy on the system I think

    m = m_now - (m_gradient * L)
    b = m_now - (b_gradient * L)
    #giving me an invalid value because the math in the gradient variables is causing overflow
    #which is causing difficulties in calculating the values of m_gradient and b_gradient
    return m, b


m = 0
b = 0
L = 0.0001

epochs = 100


for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, pData, L)

print(m, b)

plt.scatter(pData.median_income, pData.median_house_value, color = "black")
plt.plot(list(range(1000, 2500)), [m * x * b for x in range(1000, 2500)], color = "red")
plt.show()