1.
get original_price
discount=original_price *0.2
new_price=original_price-discount
display=new_price

DISCOUNT_RATE=0.2
original_price = float(input("Original price: $"))
discount = original_price*DISCOUNT_RATE
new_price = original_price-DISCOUNT_RATE
print("The new_price is $", new_price, sep="")

2.
get distance in kilometers
distance in miles=distance in kilometers*0.62
display distance in miles


CONVERSION_RATE=0.62
distance_in_kilometres=float(input("Enter the distance to be converted"))
converted_distance=distance_in_kilometres*CONVERSION_RATE
print("The distance in miles is: ",converted_distance,sep="")

3.
get daily_food cost,Activity_costs,number_of_days_staying
total_cost = (daily_food_cost+daily_activity_cost+75)*number_of_days_staying
display total_cost

HOTEL_COST=75
Daily_Food_Cost=float(input("Daily Food Cost:"))
Daily_Activities_Cost=float(input("Daily Activities Cost:"))
Number_Of_Days_Staying=int(input("Number of days staying:"))
Total_Cost=(Daily_Food_Cost+Daily_Activities_Cost+HOTEL_COST)*Number_Of_Days_Staying
print("The total cost",Total_Cost)

4.
get total_sleep,deep_sleep
deep_sleep_in_minutes=deep_sleep//60
deep_sleep_in_seconds=deep_sleep%60
display deep_sleep_in_minute, deep_sleep_in_second
totalsleep_in_minutes=total_sleep//60
totalsleep_in_seconds=total_sleep%60
display totalsleep_in_minutes,totalsleep_in_seconds
Percentage_of_deep_sleep=(deep_sleep/total_sleep)*100
display Percentage_of_deep_sleep


Total_Sleep=int(input("Total sleep in seconds:"))
Deep_Sleep=int(input("Deep sleep in seconds:"))
Deep_Sleep_in_minutes=Deep_Sleep//60
Deep_Sleep_in_seconds=Deep_Sleep%60
Total_Sleep_in_minutes=Total_Sleep//60
Total_Sleep_in_seconds=Total_Sleep%60
print("Deep sleep :",Deep_Sleep_in_minutes,"m",Deep_Sleep_in_seconds,"s")
print("Total sleep :",Total_Sleep_in_minutes,"m",Total_Sleep_in_seconds,"s")
Percentage_of_Deep_Sleep=(Deep_Sleep/Total_Sleep)*100
print("Percentage : ",Percentage_of_Deep_Sleep)

