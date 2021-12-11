from datetime import datetime

my_date = datetime.now()
print(my_date)
my_str = my_date.strftime("%d/%m/%Y")
print(f"Fecha España {my_str}")
my_str = my_date.strftime("%m/%d/%Y")
print(f"Fecha USA {my_str}")