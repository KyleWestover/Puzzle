# Puzzle

You are given a 2-D puzzle of size MxN, that has N rows and M column (M and N can be 
different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by 
‘-’ (hyphen) and the one with a barrier is marked by ‘#’. You are given two coordinates from 
the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to reach (x,y). You can 
move only in the following directions.

L: move to left cell from the current cell

R: move to right cell from the current cell

U: move to upper cell from the current cell

D: move to the lower cell from the current cell

You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal 
is to reach the destination cells covering the minimum number of cells as you travel from the 
starting cell. 
