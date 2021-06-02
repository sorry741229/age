driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入"有/沒有"')
	raise SystemExit

age = input('請問你的年齡? ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('通過測驗')
	else:
		print('奇怪?你怎麼會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('超過18歲了，怎麼沒去考駕照')
	else:
		print('再過一陣子就可以去考駕照了')