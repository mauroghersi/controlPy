import control
import matplotlib.pyplot as plt
import numpy as np

l = np.random.laplace(0,1,10)
print(l)

#declaracao funcao de transferencia 25/(s^2 + 3s + 25)
s = control.system.TransferFunction([25],[1,3,25])

print(s)

#root locus plot
control.rootlocus(s,gain_range=10)
plt.grid(True, linestyle='-.', color="LightGray")

plt.xlim(0,10)
plt.ylim(0,1.5)

#resposta ao degrau unitario em malha aberta
s.response("step", 10, 0.05, False, True)


#funcao pid 
d = control.PID(0.7,0.05,0.1,s)

plt.grid(True, linestyle='-.', color="LightGray")

plt.xlim(0,10)
plt.ylim(0,1.5)

#resposta ao degrau unitario do controlador PID em malha fechada
d.response("step", 10, 0.05, True, True)

#verifica se o sistema é estavel
iSstable = s.stability()

print(iSstable)
