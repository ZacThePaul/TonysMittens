cube_width = 100

vertice1 = (100, 100)
vertice2 = (300, 100)
vertice3 = (300, 300)
vertice4 = (100, 300)

# If you want to be able to rotate the cube, simple addition won't work here, it will always look the way it does now.
vertice5 = (vertice1[0] + cube_width, vertice1[1] + cube_width)
vertice6 = (vertice2[0] + cube_width, vertice2[1] + cube_width)
vertice7 = (vertice3[0] + cube_width, vertice3[1] + cube_width)
vertice8 = (vertice4[0] + cube_width, vertice4[1] + cube_width)


	pg.draw.line(screen, (0, 30, 255), (vertice1), (vertice2), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice2), (vertice3), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice3), (vertice4), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice4), (vertice1), 3)

	pg.draw.line(screen, (0, 30, 255), (vertice5), (vertice6), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice6), (vertice7), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice7), (vertice8), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice8), (vertice5), 3)

	pg.draw.line(screen, (0, 30, 255), (vertice1), (vertice5), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice2), (vertice6), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice3), (vertice7), 3)
	pg.draw.line(screen, (0, 30, 255), (vertice4), (vertice8), 3)
