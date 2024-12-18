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
ax.plot(dfAr["anoImiAr"], dfAr["qtdImiAR"], label="Argentina", color="blue", marker='o')
ax.plot(dfBra["anoImiBra"], dfBra["qtdImiBra"], label="Brasil", color="red", marker='o')
ax.set_title("Imigração Argentina e Brasil para o Canadá")
ax.set_xlabel("Ano de imigração")
ax.set_ylabel("Número de imigrantes")
ax.set_xticks(years[::5]) 
ax.tick_params(axis='x', rotation=45)  

plt.show()

