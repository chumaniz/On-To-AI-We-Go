import numpy as np
import matplotlib.pyplot as plt

bongani = (70, 50, 87, 15)
vusi = (80, 45, 88, 95)
sipho = (40, 95, 76, 89)

skills = ("Python", "Data Science", "Machine Learning", "Articicial Intelligence")

width = 0.2
index = np.arange(4)
plt.bar(index, bongani,
        width=width, label="Bongani")
plt.bar(index+width, vusi,
        width=width, label="Vusi")
plt.bar(index+width*2, sipho,
        width=width, label="Sipho")

plt.xticks(index + width, skills)
plt.ylim(0,100)
plt.title("Technology Stack Skills Bar Graph")
plt.ylabel("Skill Level Out Of 100")
plt.xlabel("Tech Stack Skill")
plt.legend(loc = 'upper left')
plt.show()
plt.savefig("techskillchart.jpg")