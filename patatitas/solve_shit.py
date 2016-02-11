# -*- coding: utf-8 -*-

from math import sqrt

def euc(a,b):
	return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

if __name__ == '__main__':
	print 'Patatitas!'
	# T: Tiempo
	# D: numero de drones
	#weight : peso maximo de los drones
	# r,c numero filas y columnas
	r,c,D,T,max_weight = [int(x) for x in raw_input().split()]
	P = int(raw_input())
	
	# Peso de los productos
	products_weight = [int(x) for x in raw_input().split()]

	# Numero de almacenes
	W = int(raw_input())

	# Warehouse  posiciones de los almacenes // Stock lo que tiene cada almacen
	warehouses = []
	stock = []
	for i in xrange(W):
		warehouses += [[int(x) for x in raw_input().split()]]
		stock += [[int(x) for x in raw_input().split()]]

	# C : numero de pedidos
	C = int(raw_input())
	pedidos = []
	order_pos = [] # Posicion de los pedidos
	order_products = [] # Pedido en si
	for i in xrange(C):
		order_pos += [[int(x) for x in raw_input().split()]]
		_ = int(raw_input())
		order_products += [[int(x) for x in raw_input().split()]]

	# Metemos los pedidos en una sola lista
	for numero, pedido in enumerate(order_pos):
		pedidos.append({"posicion":order_pos[numero], "pedido":order_products[numero]})

	#print products
	print warehouses
	print stock
	print order_pos
	print order_products
	print "PEDIDO LISTA {}".format(pedidos)

	drone_busy = 0
	drone_position = [0]*D
	drone_load = []
	for i in xrange(D):
		drone_load.append([0]*P)
	print "drone_pos: {}".format(drone_position)

	output = ""
	for i in xrange(C):
		for j in xrange(D):
			# drone j reparte pedido i
			prod_count = [0]*P
			for item in pedidos[i]['pedido']:
				prod_count[item] += 1

		for item in xrange(len(prod_count)):
			if item > 0:
				while stock[drone_position[j]][item] > 0 and (sum(drone_load[j]) + products_weight[item]) < max_weight:
					stock[drone_position[j]][item] -= 1
					drone_load[j][item] += 1
			
	

