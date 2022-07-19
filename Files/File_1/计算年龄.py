from time import strftime
year = int(input("请输入你的出生年："))
month = int(input("请输入你的出生月："))
now_year = int(strftime("%Y"))
now_month = int(strftime("%m"))
month_difference = now_month - month
if month_difference < 0:
    your_age = now_year - year - 1
else:
    your_age = now_year - year
print("你的年龄是：",your_age)
