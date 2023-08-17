import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글깨짐 방지
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

# 그래프가 안만들어질 경우
# pip install msvc-runtime 터미널에 입력
# plt.plot([1, 2, 3, 4], [3, 6, 10, 12]) #좌x ,우y

x_values = [1, 2, 3, 4]
y_values = [3, 6, 10 ,12]
plt.plot(x_values, y_values, "o--")
plt.xlabel("x 축") # x축 이름
plt.ylabel("y 축") # y축 이름
plt.show()
