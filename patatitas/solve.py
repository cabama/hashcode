

if __name__ == '__main__':
	print 'Patatitas!'

	r,c,D,T,weight = [int(x) for x in raw_input().split()]
	P = int(raw_input())
	
	products = [int(x) for x in raw_input().split()]

	W = int(raw_input())
	warehouses = []
	stock = []
	for i in xrange(W):
		warehouses += [[int(x) for x in raw_input().split()]]
		stock += [[int(x) for x in raw_input().split()]]

	C = int(raw_input())
	order_pos = []
	order_products = []
	for i in xrange(C):
		order_pos += [[int(x) for x in raw_input().split()]]
		_ = int(raw_input())
		order_products += [[int(x) for x in raw_input().split()]]

	print products
	print warehouses
	print stock
	print order_pos
	print order_products

