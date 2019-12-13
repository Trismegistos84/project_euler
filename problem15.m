% Starting in the top left corner of a 2×2 grid, and only being able to move 
% to the right and down, there are exactly 6 routes to the bottom right corner.

routes = prod(21:40) / prod(1:20)
printf("%f\n", routes)

