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
	r,c,D,T,weight = [int(x) for x in raw_input().split()]
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

	dist_order_warehouse = [0]*C
	warehouse_order = [0]*W

	for i in xrange(len(order_pos)):
		dist_order_warehouse[i] = []
		for j in xrange(len(warehouses)):
			dist_order_warehouse[i] += [[euc(order_pos[i], warehouses[j]),j]]
		dist_order_warehouse[i].sort()
		if warehouse_order[dist_order_warehouse[i][0][1]] == 0:
			warehouse_order[dist_order_warehouse[i][0][1]] = []
		warehouse_order[dist_order_warehouse[i][0][1]] += [[order_products[i], i]]
		print 'dist_irder_warehouse[i]: {}'.format(dist_order_warehouse[i])

	for i in xrange(W):
		print 'warehouse_order[i]: {}'.format(warehouse_order[i])
