import asyncio;
import pygame;
import random;
from collections import deque;

NUM_ROW=40;
NUM_COL=40;
ROW = 600;
COL = 600;
STEP = 15;
pygame.init();
pygame.display.set_caption("BFS-Snake-Game");

grid = [['*']*NUM_COL for _ in range(NUM_ROW)];

class Node:
  def __init__(self,x,y,parent=None):
    self.x = x;
    self.y = y;
    self.parent = parent;
  
  def __eq__(self,node):
    if not isinstance(node,Node):
      return NotImplemented
    return self.x == node.x and self.y == node.y;

  def set_pos(self,x,y):
    self.x = x;
    self.y = y;

  def set_parent(self,parent):
    self.parent = parent;

  def draw(self,Game,color):
    pos = pygame.Rect(STEP*self.y,STEP*self.x,STEP,STEP);
    pygame.draw.rect(Game,color,pos);

class Snake:
  body = [];
  tail = None;
  def __init__(self,x,y):
    self.x = x;
    self.y = y;
    self.head = Node(x,y);
    self.body.append(self.head);

  def move_snake(self):
    self.tail = snake.body[-1];
    for i in range(len(self.body)-1,0,-1):
      self.body[i]=self.body[i-1];

  def draw_snake(self,Game,color):
    for i in range(len(self.body)-1,0,-1):
      self.body[i].draw(Game,color);

  def grow(self):
    self.body.append(self.tail);

obs = [Node(1,1),Node(1,2),Node(1,3),Node(1,4),Node(1,5),Node(1,6),Node(1,7),Node(1,8),Node(1,9),Node(1,10),Node(2,1),Node(2,2),Node(2,3),Node(2,4),Node(2,5),Node(2,6),Node(2,7),Node(2,8),Node(2,9),Node(2,10),Node(3,1),Node(3,2),Node(3,3),Node(3,4),Node(3,5),Node(3,6),Node(3,7),Node(3,8),Node(3,9),Node(3,10),Node(5,1),Node(5,2),Node(5,3),Node(5,4),Node(5,5),Node(5,6),Node(5,7),Node(5,8),Node(5,9),Node(5,10),Node(5,11),Node(5,12),Node(5,13),Node(5,14),Node(5,15),Node(5,16),Node(5,17),Node(5,18),Node(5,19),Node(5,20),Node(5,22),Node(5,23),Node(5,24),Node(5,27),Node(5,28),Node(5,29),Node(5,30),Node(5,31),Node(5,32),Node(5,33),Node(6,22),Node(7,22),Node(8,22),Node(9,22),Node(10,22),Node(11,22),Node(12,22),Node(13,22),Node(14,22),Node(15,22),Node(30,2),Node(30,3),Node(30,4),Node(30,5),Node(30,6),Node(30,7),Node(30,8),Node(30,9),Node(30,10),Node(30,11),Node(29,11),Node(28,11),Node(27,11),Node(26,11),Node(25,11),Node(20,15),Node(20,16),Node(20,17),Node(20,18),Node(20,19),Node(20,20),Node(20,21),Node(20,22),Node(20,23),Node(20,24),Node(20,25),Node(20,26),Node(20,27),Node(30,28),Node(30,29),Node(29,30),Node(28,31),Node(27,32),Node(26,33),Node(2,34),Node(26,34),Node(37,2),Node(37,3),Node(37,4),Node(37,5),Node(37,6),Node(37,7),Node(37,8),Node(37,9),Node(37,10),Node(38,10),Node(39,10),Node(34,16),Node(34,17),Node(34,18),Node(34,19),Node(34,20),Node(34,21),Node(34,22),Node(34,23),Node(34,24),Node(34,25),Node(34,26),Node(34,27),Node(34,28),Node(34,29),Node(34,30),Node(34,31),Node(34,32),Node(34,33),Node(34,34),Node(34,35),Node(34,36),Node(34,37),Node(34,38),Node(34,39)];

def gen_random(s):
  while True:
    x=random.randrange(NUM_COL-1);
    y=random.randrange(NUM_ROW-1);
    available = [] + obs + s;
    if len(list(filter(lambda z:z.x==x and z.y==y,available)))>0:
      continue;
    else:
      break;
  return (x,y);

def valid(x,y):
  v_x = x>=0 and x<=NUM_COL-1;
  v_y = y>=0 and y<=NUM_ROW-1;
  return v_x and v_y;

def set_init():
  for i in obs:
    grid[i[0]][i[1]] = '#';
  
def print_arr():
  set_init();
  for i in grid:
    print(i);
    
def bfs(start,end,body):
  q = deque();
  l = []+obs+body[1:len(body)];
  curr = Node(-1,-1);
  q.append(end);
  while len(q) > 0 and (curr!=start):
    curr = q.popleft();
    if valid(curr.x-1,curr.y):
      left = Node(curr.x-1,curr.y,curr);
      if not left in l:
        l.append(left);
        q.append(left);
    if valid(curr.x,curr.y+1):
      top = Node(curr.x,curr.y+1,curr);
      if not top in l:
        l.append(top);
        q.append(top);
    if valid(curr.x+1,curr.y):
      right = Node(curr.x+1,curr.y,curr);
      if not right in l:
        l.append(right);
        q.append(right);
    if valid(curr.x,curr.y-1):  
      bottom = Node(curr.x,curr.y-1,curr);
      if not bottom in l:
        l.append(bottom);
        q.append(bottom);  
  return curr;

def draw(Game):
  Game.fill((0,0,30));
  d.draw(Game,(0,255,0));
  c.draw(Game,(255,255,255));
  snake.draw_snake(Game,(255,255,255));
  
  for t in obs:
    rec = pygame.Rect(STEP*t.y,STEP*t.x,STEP,STEP);
    pygame.draw.rect(Game,(255,0,0),rec);
    #r = pygame.Rect(food[1]*STEP,food[0]*STEP,STEP,STEP);
    #pygame.draw.rect(Game,(0,255,0),r);
  pygame.display.update();

async def main():
  global c,d,snake;
  GAME = pygame.display.set_mode((ROW,COL));
  run = True;
  clock = pygame.time.Clock();
  snake = Snake(39,22);
  rand = gen_random(snake.body);
  d = Node(rand[0],rand[1]);
  c = bfs(snake.body[0],d,snake.body);
  sl = [1,2,3];
  while run:
    clock.tick(17);
    if c!= d:
      snake.move_snake();
      c=c.parent;
      snake.body[0] = c;
    elif c==d:
      snake.grow(); 
      rand = gen_random(snake.body);
      d = Node(rand[0],rand[1]);   
      c = bfs(c,d,snake.body);
     # print(c.x);
    draw(GAME);
    if len(snake.body)==30:
      snake.body = snake.body[0:1];
    asyncio.sleep(0);    
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        run = False;
  pygame.quit();
  
if __name__ == "__main__":
  asyncio.run(main());