import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS', 'Amdocs']
recruitments = [120, 150, 180, 90, 110, 140, 80, 100]

plt.bar(companies, recruitments)
plt.title("Company Recruitment Data")
plt.xticks(rotation=30)
plt.show()

plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

explode = [0, 0.1, 0, 0, 0, 0, 0, 0]  # highlight Google
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Customized Pie Chart")
plt.show()

plt.pie(recruitments, labels=companies)
centre_circle = plt.Circle((0,0),0.70)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

labels = ['IBM', 'Amdocs']
values = [90, 100]

plt.bar(labels, values)
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.show()