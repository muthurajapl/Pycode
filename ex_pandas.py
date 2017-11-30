# Import cars data
import pandas as pd
cars = pd.read_csv('cars1.csv', index_col = 0)
             
print (cars)

# Print out country column as Pandas Series
print (cars['country'])

# Print out country column as Pandas DataFrame
print (cars[['country']])

# Print out observation for Japan
print (cars.loc[2])

# Print out observations for Australia and Egypt
print (cars.loc[[1,6]])

# Print out drives_right value of Morocco
print (cars.loc[5,'drives_right'])

# Print sub-DataFrame
print (cars.loc[[4, 5],['country', 'drives_right']])