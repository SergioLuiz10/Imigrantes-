import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\sergi\\.vscode\\Python data\\imigrantes_canada.csv")
df.set_index("País", inplace=True)
years = list(map(str, range(1980, 2014)))
findyArgentina = df.loc["Argentina", years].values.tolist()
findyBrasil = df.loc["Brasil", years].values.tolist()
countrieArg= {"anoImiAr": years, "qtdImiAR": findyArgentina}.values.tolist()
countreiBra={"anoImiBra":years,"qtdImiBra":findyBrasil}.values.tolist()
dfAr = pd.DataFrame(countrieArg)
dfBra=pd.DataFrame(countreiBra)

plt.figure(figsize=(10,6))
plt.plot(dfAr["anoImiAr"], dfAr["qtdImiAR"], color="blue")
plt.plot(dfBra["anoImiBra"],dfBra["qtdImiBra"],color="red")
plt.title("Imigração Argentina e Brasil para o Canadá")
plt.xlabel("Ano de imigração")
plt.ylabel("Número de imigrantes") 
plt.xticks(["1980", "1985", "1990", "1995", "2000", "2005", "2010"])
plt.legend(loc="upper left")  # A legenda será exibida no canto superior esquerdo

plt.show()

