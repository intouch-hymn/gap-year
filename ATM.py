

money = 10000

print('กด1 : ถอนเงิน')
print('กด2 : เช็คยอดเงิน')
print('กดQ : ออกจากระบบ')
print('--------------')
menu = input('กรุณาเลือกเมณู: ') #user เลือกแล้วเราจะเก็บเมณูไว้

while menu != 'q':
	if menu == '1':
	print('<<<<ถอนเงิน>>>>')                                                                    
	withdraw = int(input('กรุณากรอกจำนวนเงิน: '))
	while withdraw > money:
		print('เงินในบัญชีไม่พอ กรุณากรอกยอดเงินให้ถูกต้อง')
		withdraw = int(input('กรุณากรอกจำนวนเงิน: '))
	print('กรุณารับเงิน {} บาท'.format(withdraw))
	money = money - withdraw # เอาจำนวนเงินที่มีลบกับที่ถอน
	print('คุณมีเงินเหลือ: {} บาท'.format(money))

	elif menu == '2':
		print('ยอดเงินคงเหลือของคุณคือ: {} บาท'.format(money))
	print('--------------')
	print('กด1 : ถอนเงิน')
	print('กด2 : เช็คยอดเงิน')
	print('กดQ : ออกจากระบบ')

print('ขอบคุณที่ใช้บริการ กรุณารับบัตรคืน')
	
	