import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("C:\\Users\\sergi\\.vscode\\Python data\\imigrantes_canada.csv")
df.set_index('País',inplace=True)
anos=list(map(str,range(1980,2014)))
brasil=df.loc["Brasil",anos]

brasil_dic = {"anoImi": anos, "valorImi": brasil.values}

dfBrasil = pd.DataFrame(brasil_dic)

plt.figure(plt.figure(figsize=(10, 6)))
plt.plot(dfBrasil["anoImi"],dfBrasil["valorImi"])
plt.xticks(["1980","1985","1990","1995","2000","2005","2010"])
plt.title("Imigrações do Brasil para o Canadá")
plt.xlabel("Anos das imimigrações")
plt.ylabel("Número de imigrantes")
plt.show()



 