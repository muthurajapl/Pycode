def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print ("You have %d cheese" % cheese_count)
    print ("You have %d boxes of crackers" % boxes_of_crackers)
    print ("Man that's enough for a party!\nGet a blanket")
	
print ("We can just give the function numbers directly")
cheese_and_crackers (20,30)

print ("Or we can use variables from the script:")
cheese_count1 = 10
boxes_of_crackers1 = 50

cheese_and_crackers (cheese_count1, boxes_of_crackers1)

print ("We can do math inside too")
cheese_and_crackers (20+5, 30+10)

print ("And we can combine the two - variables and math.")
cheese_and_crackers (cheese_count1+100, boxes_of_crackers1+1000)

def day_of_week (day):
    print ("Today is %s.\nHave a great day!" % day)

str1 = 'Wednes'
str2 = 'day'
str3 = '28-10-2017'

day_of_week (str1+str2)
day_of_week (str3)
day_of_week ('Thurs'+'day')
day_of_week ('Satur'+str2)
day_of_week (input('>')+str2)

cheese_and_crackers (int(input("enter no "))+100, boxes_of_crackers1+1000)