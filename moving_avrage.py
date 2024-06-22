import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import pandas

plt.style.use('ggplot')


# Extrating data
df = pandas.read_csv("data_yahoo.csv")
print(df['Close'].rolling(1).mean())

for x in df:
    ar = [x]
    print(ar)


plt.plot(df['Close'],label= 'Close')
plt.plot(df['Close'].rolling(2).mean(),label= 'MA 1 days')
plt.plot(df['Close'].rolling(7).mean(),label= 'MA 7 days')
plt.legend(loc='best')
plt.title('EUR/INR Closing Average')
plt.show()
