moves=eval("["+open("d9.txt").read().replace("R","[(0,1),").replace("L","[(0,-1),").replace("D","[(-1,0),").replace("U","[(1,0),").replace("\n","],")+"]]")
head=(0,0)
tail=(0,0)
snake=[(0,0)]*10
positions={(0,0)}
positions_snake={(0,0)}
for move in moves:
    for _ in range(1,move[1]+1):
        # part 1
        new_head=(head[0]+move[0][0],head[1]+move[0][1])
        if abs(new_head[0]-tail[0])>1 or abs(new_head[1]-tail[1])>1:
            tail=head
            positions.add(tail)
        head=new_head

        # part 2
        new_snake = [tuple(i) for i in snake] # deep copy
        new_snake[0]=(snake[0][0]+move[0][0],snake[0][1]+move[0][1]) # new snake head
        for i in range(len(snake)-1):
            if abs(new_snake[i][0]-snake[i+1][0])>1 or abs(new_snake[i][1]-snake[i+1][1])>1:
                if abs(new_snake[i][0]-snake[i+1][0]) == abs(new_snake[i][1]-snake[i+1][1]): # check if diagonal
                    print("Diagonal") # never enters, why???
                else:
                    new_snake[i+1]=snake[i]
        positions_snake.add(snake[-1])
        snake=new_snake
print(len(positions)) # part 1
print(len(positions_snake))