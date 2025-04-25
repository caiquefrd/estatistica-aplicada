from leitor.main import leitor
from medidas_estatisticas.main import medidas_estatisticas
from medidas_dispersao.main import medidas_dispersao
from quartil.main import quartil
from percentil.main import percentil
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

#instanciando as classes
data = leitor.retornar_data()
calc_med_estatisticas = medidas_estatisticas(data)
calc_dispersao = medidas_dispersao(data)
calc_quartil = quartil(data)
calc_percentil = percentil(data)

#calculando
media = calc_med_estatisticas.media()
print({"media": media})

moda = calc_med_estatisticas.moda()
print({"moda": moda})

mediana = calc_med_estatisticas.mediana()
print ({"mediana": mediana})

desvio_padrao = calc_dispersao.desvio_padrao()
print ({"desvio_padrao": desvio_padrao})

variancia = calc_dispersao.variancia()
print ({"variancia": variancia})

prim_quartil = calc_quartil.primeiro_quartil()
print ({"primeiro_quartil": prim_quartil})

seg_quartil = calc_quartil.segundo_quartil()
print ({"segundo_quartil": seg_quartil})

ter_quartil = calc_quartil.terceiro_quartil()
print ({"terceiro_quartil": ter_quartil})

percentil_5 = calc_percentil.percentil(5)
print ({"percentil_5": percentil_5})

percentil_95 = calc_percentil.percentil(95)
print ({"percentil_95": percentil_95})

dados = [percentil_5, prim_quartil, seg_quartil, ter_quartil, percentil_95]
plt.boxplot(dados, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title('Box Plot Temperaturas')
plt.xlabel('Valores')
plt.grid(True)

plt.show()
