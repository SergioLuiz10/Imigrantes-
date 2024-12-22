import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\sergi\\.vscode\\Python data\\imigrantes_canada.csv")
df.set_index("País", inplace=True)
years = list(map(str, range(1980, 2014)))
findyArgentina = df.loc["Argentina", years].values.tolist()
findyBrasil = df.loc["Brasil", years].values.tolist()
countrieArg= {"anoImiAr": years, "qtdImiAR": findyArgentina}
countreiBra={"anoImiBra":years,"qtdImiBra":findyBrasil}
dfAr = pd.DataFrame(countrieArg)
dfBra=pd.DataFrame(countreiBra)

plt.figure(figsize=(10,6))
plt.plot(dfAr["anoImiAr"], dfAr["qtdImiAR"],label="Argentina", color="blue")
plt.plot(dfBra["anoImiBra"],dfBra["qtdImiBra"],label="Brasil",color="red")
plt.title("Imigração Argentina e Brasil para o Canadá")
plt.xlabel("Ano de imigração")
plt.ylabel("Número de imigrantes") 
plt.xticks(["1980", "1985", "1990", "1995", "2000", "2005", "2010"])
plt.legend(loc="upper left") 

fig, ax = plt.subplots(figsize=(10, 6)) 
ax.plot(dfAr["anoImiAr"], dfAr["qtdImiAR"],label="Argentina", color="blue")
ax.plot(dfBra["anoImiBra"],dfBra["qtdImiBra"],label="Brasil",color="red")
ax.set_title("Imigração Argentina e Brasil para o Canadá \n 1980 a 2013")
ax.set_xticks(["1980", "1985", "1990", "1995", "2000", "2005", "2010"])
ax.set_xlabel("Ano de imigração")
ax.set_ylabel("Número de imigrantes") 
ax.legend(loc="upper left") 

fig, axs = plt.subplots(1, 2, figsize=(14, 6))
axs[0].plot(dfAr["anoImiAr"], dfAr["qtdImiAR"],label="Argentina", color="blue")
axs[0].plot(dfBra["anoImiBra"],dfBra["qtdImiBra"],label="Brasil",color="red")
axs[0].set_title("Imigração Argentina e Brasil para o Canadá \n 1980 a 2013")
axs[0].set_xticks(["1980", "1985", "1990", "1995", "2000", "2005", "2010"])
axs[0].set_xlabel("Ano de imigração")
axs[0].set_ylabel("Número de imigrantes") 
axs[0].legend(loc="upper left")
axs[0].grid()

axs[1].boxplot([dfAr["qtdImiAR"], dfBra["qtdImiBra"]], labels=["Argentina", "Brasil"])
axs[1].set_title("Distribuição de Imigrantes (1980-2013)")
axs[1].set_xlabel("País")
axs[1].set_ylabel("Número de imigrantes") 
axs[1].grid()


fig, axs = plt.subplots(2, 2, figsize=(16, 8))
axs[0][0].plot(dfAr["anoImiAr"], dfAr["qtdImiAR"], label="Argentina", color="blue")
axs[0][0].set_title("Argentina")
axs[0][0].set_xlabel("Ano")
axs[0][0].set_ylabel("Imigrantes")
axs[0][0].grid()

axs[0][1].plot(dfBra["anoImiBra"], dfBra["qtdImiBra"], label="Brasil", color="red")
axs[0][1].set_title("Brasil")
axs[0][1].set_xlabel("Ano")
axs[0][1].set_ylabel("Imigrantes")
axs[0][1].grid()

axs[1][0].plot(years, df.loc["Colômbia", years].values, label="Colômbia", color="green")
axs[1][0].set_title("Colômbia")
axs[1][0].set_xlabel("Ano")
axs[1][0].set_ylabel("Imigrantes")
axs[1][0].grid()

axs[1][1].plot(years, df.loc["Peru", years].values, label="Peru", color="purple")
axs[1][1].set_title("Peru")
axs[1][1].set_xlabel("Ano")
axs[1][1].set_ylabel("Imigrantes")
axs[1][1].grid()

for ax in axs.flat:
    ax.set_xticks(years[::5])
    ax.tick_params(axis='x', rotation=45)
    ax.legend(loc="best")





plt.tight_layout()
plt.show()

