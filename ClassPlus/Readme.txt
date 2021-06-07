Input

The first line contains two space-separated integers: n, the number of universes and m, the number of
portals.
Then m lines follow, i

th line contains three integers, universe ai and bi, connected through the i
th portal

and ci, the travelling time between the mentioned universes.
Then n lines follow, ith line contains ki, number of time instances when the demons are patrolling the
i
th universe. Then ki space separated integers tij follow in sorted order. tij means that at this timestamp
some demon was patrolling on the i

th universe and the spiderman had to wait for this second (if he is at

this universe at this timestamp).


Example

4 4 5
1 2 3
1 3 2
2 4 2
3 4 3
0
1 4
2 2 3
0
