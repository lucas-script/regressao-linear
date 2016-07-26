import numpy as np
import statsmodels.api as sm

from statsmodels.formula.api import ols

from statsmodels.sandbox.regression.predstd import wls_prediction_std

import matplotlib.pyplot as plt
import pylab

ipca = [1.24, 1.22, 1.32, 0.71, 0.74, 0.79, 0.62, 0.22, 0.54, 0.82, 1.01, 0.96]
igp =           [0.67, 0.53, 1.21, 0.92, 0.40, 0.68, 0.58, 0.40, 1.42, 1.76, 1.19, 0.44]

ipa =           [0.23, 0.41, 0.37, 1.11, 0.19, 0.43, 0.61, 0.44, 2.02, 2.38, 1.41, 0.33]

incc =          [0.92, 0.31, 0.62, 0.46, 0.95, 1.84, 0.55, 0.59, 0.22, 0.36, 0.34, 0.10]
cestaBasicaSP = [371.22, 378.86, 379.35, 387.05, 402.05, 392.77, 395.83, 386.04, 383.21, 382.13, 399.21, 412.12]
ipc =           [1.62, 1.22, 0.70, 1.10, 0.62, 0.47, 0.85, 0.56, 0.66, 0.88, 1.06, 0.82]

dividaLiqSetorPublico = [188500887803209, 187706333799174, 184765806823815, 189770327088739, 190366605999196, 196280910757371, 195081778811247, 192992932469232, 190601887177971, 197251356355572, 20275100009607, 2136888008451]
indiceBovespa =         [46907.68, 51583.09, 51150.16, 56229.38, 52760.47, 53080.88, 50864.77, 46625.50, 45059.30, 45868.80, 45120.40, 43350.00]
m1 =                    [358633825, 327077519, 326107712, 323948694, 314677519, 304345416, 314876743, 305896812, 303714606, 305882251, 306011809, 311288444]
m2 =                    [2127290700, 2130760374, 2127134051, 2135910116, 2151857157, 2154232444, 2161920644, 2163406036, 2167463562, 2200853919, 2220285504, 2285721020]
m3 =                    [4335516207, 4347972711, 4370433264, 4406195377, 4475353974, 4479849781, 4507204991, 4518764301, 4540725113, 4624608482, 4656424458, 4759312267]
m4 =                    [5049003232, 5065307768, 5140845555, 5167891374, 5247207985, 5277126340, 5278779444, 5313940526, 5319375997, 5385785478, 5443887255, 5554332896]

dividaLiqExternaSetorPublico =      [-13.74, -14.88, -16.49, -15.4, -16.28, -15.83, -17.21, -18.51, -20.15, -19.53, -19.32, -19.51]
exportacoesFob =                    [13704.044559, 12092.23067, 16978.968634, 15156.274767, 16769.183205, 19628.438412, 18533.065548, 15485.353065, 16148.183035, 16048.986692, 13806.364678, 16783.231319]
indicePrecosImportacoes =           [127.42, 123.67, 119.06, 122.99, 122.22, 120.3, 119.42, 119.87, 117.36, 117.56, 113.59, 115.48]
reservasInternacionais =            [372167.128898913, 372147.395674487, 371044.344296695, 372973.213854484, 371696.713298483, 372168.440273058, 370751.898427197, 370559.079615524, 370600.395148097, 370959.968888696, 368975.918604929, 368738.680174398]
taxaCambioRealEfetivaExportacoes =  [112.451019639423, 119.237052881333, 129.825052598383, 125.895973624719, 126.523178360907, 127.939361180313, 130.216990879643, 139.002105731094, 150.125546391424, 145.081417655015, 137.043131925227, 136.708569197281]
taxaCambioRealEfetivaImportacoes =  [113.146773201727, 119.820835388654, 130.239241076894, 126.183787399064, 126.848098711942, 128.379005737714, 130.612733968817, 139.622888524739, 150.720500514073, 145.879342604443, 137.62323426857, 137.893569494428]
taxaCambioComercialCompra =         [2.633619048, 2.815838889, 3.138863636, 3.042595, 3.061075, 3.11112381, 3.222508696, 3.513695238, 3.905809524, 3.879504762, 3.7758, 3.870495455]
taxaCambioComercialVenda =          [2.634228571, 2.81645, 3.139477273, 3.04322, 3.061715, 3.111738095, 3.223143478, 3.514304762, 3.906457143, 3.880138095, 3.77646, 3.871136364]

# x = np.column_stack((ipa,incc,cestaBasicaSP,ipc,dividaLiqSetorPublico,indiceBovespa,m1,m2,m3,m4,dividaLiqExternaSetorPublico,exportacoesFob,indicePrecosImportacoes,
# reservasInternacionais,taxaCambioRealEfetivaImportacoes,taxaCambioRealEfetivaExportacoes,taxaCambioComercialCompra,taxaCambioComercialVenda))

y=cestaBasicaSP
x = np.column_stack((indicePrecosImportacoes,taxaCambioComercialVenda,taxaCambioComercialCompra,taxaCambioRealEfetivaImportacoes,
	taxaCambioRealEfetivaExportacoes,exportacoesFob))

x = sm.add_constant(x, prepend=True) 

res = sm.OLS(y,x).fit() 

# data=[x.igp]
# res = ols('y~x',data).fit()

print res.params
print res.bse
print res.summary()

print('Parameters: ', res.params)
print('R2: ', res.rsquared)

# prstd, iv_l, iv_u = wls_prediction_std(res)

# fig, ax = plt.subplots(figsize=(8,6))

# ax.plot(x, y, 'o', label="data")
# ax.plot(x, y, 'b-', label="True")
# ax.plot(x, res.fittedvalues, 'r--.', label="OLS")
# ax.plot(x, iv_u, 'r--')
# ax.plot(x, iv_l, 'r--')
# ax.legend(loc='best');

#PLOTAGEM INFLUENCIA
# fig, ax = plt.subplots(figsize=(12,8))
# fig = sm.graphics.influence_plot(res, ax=ax, criterion="cooks")

#PART REGRESS
# fig = plt.figure(figsize=(12,8))
# fig = sm.graphics.plot_partregress_grid(res, fig=fig)

#LEVERAGE RESID 2
# fig, ax = plt.subplots(figsize=(8,6))
# fig = sm.graphics.plot_leverage_resid2(res, ax=ax)


#FIT PLOT
# fig, ax = plt.subplots(figsize=(12, 8))
# fig = sm.graphics.plot_fit(res, "x1", ax=ax)

# ou



# fig, ax = plt.subplots()
# fig = sm.graphics.plot_fit(res, 2, ax=ax)

#COMPONENT COMPONENT
# fig, ax = plt.subplots(figsize=(12, 8))
# fig = sm.graphics.plot_ccpr(res, "x1", ax=ax)


# prstd, iv_l, iv_u = wls_prediction_std(res)

# fig, ax = plt.subplots(figsize=(8,6))

# ax.plot(x, y, 'o', label="Data")
# ax.plot(x, y, 'b-', label="True")
# ax.plot(x, res.fittedvalues, 'r--.', label="Predicted")
# ax.plot(x, iv_u, 'r--')
# ax.plot(x, iv_l, 'r--')
# legend = ax.legend(loc="best")
	
# ax.set_ylabel("Y LABEL")
# ax.set_xlabel("X LABEL")
# ax.set_title("Regression PLOT")


# plt.scatter(x,y)
X_plot = np.linspace(0,1,100)
plt.plot(X_plot, X_plot*res.params[0] + res.params[1])


plt.show()

