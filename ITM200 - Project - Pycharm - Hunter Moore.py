import csv
import calendar
import matplotlib.pyplot as plt

file = open("stats.txt", "w")

with open('Data.csv', mode='r') as fileCSV:
    fCSV = csv.reader(fileCSV)

# Question 1
    for line in fCSV:
        print(line)

# Question 2
    year = []
    total_sale = []
    fileCSV.seek(0)  # have to do this to read the file again
    for line in fCSV:
        sum = 0
        if line[0].isnumeric():
            year.append(line[0])
            for i in range(1, 13):
                sum += int(line[i])
            total_sale.append(sum)
            file.write("Year " + line[0] + " Total Sales: " + str(sum) + "\n")

# Question 3
    plt.figure(1)
    plt.bar(year, total_sale)

    plt.title("Total Sales by Year") # Writing plot title
    plt.xlabel("Year")      # Writing x-axis label
    plt.ylabel("Total Sale in Dollars")  # Writing y-axis label

    plt.show()

# Question 4
    sale_2021 = 0.0
    sale_2022 = 0.0
    fileCSV.seek(0)
    for line in fCSV:
        sum = 0.0
        if line[0].isnumeric():
            for i in range(1, 7):
                sum += float(line[i])
            if line[0] == "2021":
                sale_2021 = sum
                sale_2021_list = line
            elif line[0] == "2022":
                sale_2022 = sum
    #Calculate SGR
    sgr = (sale_2022 - sale_2021) / (sale_2021 * 100.0)

    file.write("Sales Growth Rate: " + str(sgr) + "\n")

    est_data_2022 = []
    month_name = []
    for i in range(7, 13):
        est_2022 = float(sale_2021_list[i]) + float(sale_2021_list[i]) * sgr
        est_data_2022.append(est_2022)
        month_name.append(calendar.month_name[i])
        file.write("Estimated Sales For " + calendar.month_name[i] + ": " + str(est_2022) + "\n")

# Question 5
    plt.figure(1)
    plt.barh(month_name, est_data_2022)

    plt.title("Estimated Sales by last 6 months for 2022")
    plt.xlabel("Estimated Sale in Dollars")
    plt.ylabel("Month")
    plt.grid()                  # Showing grids on the plot

    plt.show()

file.close()

