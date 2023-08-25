# Pathfinder by Collins Kipepe

A robot starts on point marked 'A' on a rectangular grid of points.
The starting point is always the top left point on the grid (but this robot
is genius. The starting point can be anywhere). The robot can move left, right,
up or down, moving from one point to the next. By moving in steps going
left, right, up or down, the robot would like to reach a point marked 'B',
which is always the bottom right point in the grid.( Due to the robot's capabilities,
the end could also be anywhere.)

Sometimes, points are marked as 'X', and the robot is not allowed to visit
them at all. A robot is never allowed to visit a point more than once.

In how many ways can the robot move from A to B and visit all points along the way?

For example, in the following grid represented as a nested list
                    [['A', '.', '.'], ['.', '.', 'B']]

                        A   .   .
                        .   .   B

There is only one path from A to B (From A down, right, up, right, down(B)).

Update: While trying this robot, I found out there won't be too many simple
        grids that will have more than one path that touches all points. So to make
        this program more fun, I will include two modes. One that will find a path
        that touches all points(KNIGHT Mode) and one that will find a paths will
        reach point 'B' whether it touches all points or not. I will call it the BASIC Mode.
