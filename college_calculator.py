import matplotlib.pyplot as plt

starting_balance = float(raw_input('Input Opening Account Balance: '))

interest_rate = float(raw_input('Input Interest Rate: '))

annual_contribution = float(raw_input('Input Annual Contribution: '))

years = int(raw_input('Input Years Till High School Graduation: '))

starting_year = 0

def ending_balance(starting_balance, interest_rate, annual_contribution, years):
    year_end_balance = [starting_balance,]
    for year in range(0,years):
        current_year = annual_contribution + year_end_balance[year] + (year_end_balance[year] + annual_contribution) * interest_rate
        year_end_balance.append(current_year)
    return year_end_balance


balance = ending_balance(starting_balance, interest_rate, annual_contribution, years)

print balance

plt.plot(balance)
plt.xlabel('Years Since Opening Account')
plt.ylabel('Amount ($)')
plt.title('Fund Balance at Graduation')
plt.show()