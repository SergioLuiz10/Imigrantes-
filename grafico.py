import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\sergi\\.vscode\\Python data\\imigrantes_canada.csv")
df.set_index("País", inplace=True)
years = list(map(str, range(1980, 2014)))
findyArgentina = df.loc["Argentina", years].values.tolist()
findyBrasil = df.loc["Brasil", years].values.tolist()
countrieArg = {"anoImiAr": years, "qtdImiAR": findyArgentina}
countreiBra = {"anoImiBra": years, "qtdImiBra": findyBrasil}
dfAr = pd.DataFrame(countrieArg)
dfBra = pd.DataFrame(countreiBra)

plt.figure(figsize=(10, 6))
plt.plot(dfAr["anoImiAr"], dfAr["qtdImiAR"], label="Argentina", color="blue")
plt.plot(dfBra["anoImiBra"], dfBra["qtdImiBra"], label="Brasil", color="red")
plt.title("Imigração Argentina e Brasil para o Canadá")
plt.xlabel("Ano de imigração")
plt.ylabel("Número de imigrantes")
plt.xticks(["1980", "1985", "1990", "1995", "2000", "2005", "2010"])
plt.legend(loc="upper left")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dfAr["anoImiAr"], dfAr["qtdImiAR"], label="Argentina", color="blue")
ax.plot(dfBra["anoImiBra"], dfBra["qtdImiBra"], label="Brasil", color="red")
ax.set_title("Imigração Argentina e Brasil para o Canadá \n 1980 a 2013")
ax.set_xticks(["1980", "1985", "1990", "1995", "2000", "2005", "2010"])
ax.set_xlabel("Ano de imigração")
ax.set_ylabel("Número de imigrantes")
ax.legend(loc="upper left")

fig, axs = plt.subplots(1, 2, figsize=(14, 6))
axs[0].plot(dfAr["anoImiAr"], dfAr["qtdImiAR"], label="Argentina", color="blue")
axs[0].plot(dfBra["anoImiBra"], dfBra["qtdImiBra"], label="Brasil", color="red")
axs[0].set_title("Imigração Argentina e Brasil para o Canadá \n 1980 a 2013")
axs[0].set_xticks(["1980", "1985", "1990", "1995", "2000", "2005", "2010"])
axs[0].set_xlabel("Ano de imigração")
axs[0].set_ylabel("Número de imigrantes")
axs[0].legend(loc="upper left")
axs[0].grid()

axs[1].boxplot([dfAr["qtdImiAR"], dfBra["qtdImiBra"]], tick_labels=["Argentina", "Brasil"])
axs[1].set_title("Distribuição de Imigrantes (1980-2013)")
axs[1].set_xlabel("País")
axs[1].set_ylabel("Número de imigrantes")
axs[1].grid()

fig, axs = plt.subplots(2, 2, figsize=(16, 8))

axs[0][0].plot(dfAr["anoImiAr"], dfAr["qtdImiAR"], label="Argentina", color="blue", lw=3, marker='o')
axs[0][0].set_title("Argentina", fontsize=12)
axs[0][0].set_xlabel("Ano", fontsize=12)
axs[0][0].set_ylabel("Imigrantes", fontsize=12)
axs[0][0].yaxis.set_tick_params(labelsize=12)
axs[0][0].grid()

axs[0][1].plot(dfBra["anoImiBra"], dfBra["qtdImiBra"], label="Brasil", color="red", lw=3, marker='o')
axs[0][1].set_title("Brasil", fontsize=12)
axs[0][1].set_xlabel("Ano", fontsize=12)
axs[0][1].set_ylabel("Imigrantes", fontsize=12)
axs[0][1].yaxis.set_tick_params(labelsize=12)
axs[0][1].grid()

axs[1][0].plot(years, df.loc["Colômbia", years].values, label="Colômbia", color="green", lw=3, marker='o')
axs[1][0].set_title("Colômbia", fontsize=12)
axs[1][0].set_xlabel("Ano", fontsize=12)
axs[1][0].set_ylabel("Imigrantes", fontsize=12)
axs[1][0].yaxis.set_tick_params(labelsize=12)
axs[1][0].grid()

axs[1][1].plot(years, df.loc["Peru", years].values, label="Peru", color="purple", lw=3, marker='o')
axs[1][1].set_title("Peru", fontsize=12)
axs[1][1].set_xlabel("Ano", fontsize=12)
axs[1][1].set_ylabel("Imigrantes", fontsize=12)
axs[1][1].yaxis.set_tick_params(labelsize=12)
axs[1][1].grid()

for ax in axs.flat:
    ax.set_xticks(years[::5])
    ax.tick_params(axis='x', rotation=45, labelsize=12)
    ax.legend(loc="best")

yMin = 0
yMax = 7000

for ax in axs.ravel():
    ax.set_ylim(yMin, yMax)

fig, ax = plt.subplots(figsize=(12, 4))
cores = []
americaSul = df.query('Região=="América do Sul"')
americasul_sort = americaSul.sort_values(["Total"], ascending=True)
for País in americasul_sort.index:
    if País == "Brasil":
        cores.append("green")
    else:
        cores.append("silver")

for i, v in enumerate(americasul_sort["Total"]):
    ax.text(v + 20, i, str(v), va='center', fontsize=10, color='black')

ax.barh(americasul_sort.index, americasul_sort["Total"], color=cores)
ax.set_title("Brasil é o 4 maior país com em número de imigrantes para o Canáda \n entre 1980 a 2013", loc="left", fontsize=12)
ax.set_xlabel("Total de Imigrantes", fontsize=12)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
fig.savefig("gráficotes.png", transparent=False)
plt.tight_layout()


sns.set_theme()
valor_top10 = df.sort_values('Total', ascending=False).head(10)
sns.barplot(data=valor_top10, y=valor_top10.index, x="Total", orient="h")
plt.title("Top 10 Países com Mais Imigrantes para o Canadá (1980-2013)", fontsize=12)
plt.xlabel("Total de Imigrantes", fontsize=12)
plt.ylabel("País", fontsize=12)
plt.tight_layout()
plt.show() 