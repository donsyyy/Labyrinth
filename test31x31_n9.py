import random, pygame

L = [
    [False]*15 + [True] + [False]*15,
    [False] + [True]*3 + [False] + [True]*5 + [False] + [True]*3 + [False] + [True]*5 + [False] + [True]*5 + [False] + [True]*3 + [False],
    [False] + [True] + [False] + [True] + [False]*3 + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False]*3 + [True] + [False] + [True] +[False] + [True] + [False]*3 + [True] + [False] + [True] +[False] + [True] + [False],
    [False] + [True] + [False] + [True]*3 + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True]*5 + [False] + [True] + [False] + [True] + [False] + [True]*3 + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False]*3 + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False]*7 + [True] + [False] + [True] + [False] + [True] + [False]*3 + [True] + [False]*3,
    [False] + [True]*3 + [False] + [True]*3 + [False] + [True]*3 + [False] + [True]*5 + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True]*3 + [False],
    [False] + [True] + [False] + [True] + [False]*9 + [True] + [False]*3 + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False] + [True]*5 + [False] + [True]*3 + [False] + [True]*3 + [False] + [True]*3 + [False] + [True] + [False] + [True]*3 + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False] + [True] + [False]*3 + [True] + [False] + [True] + [False]*3 + [True] + [False]*7 + [True] + [False]*5 + [True] + [False],
    [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True]*3 + [False] + [True]*5 + [False] + [True]*3 + [False] + [True]*3 + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False] + [True] + [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False],
    [False] + [True] + [False] + [True]*3 + [False] + [True] + [False] + [True]*3 + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True]*3 + [False] + [True]*3 + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False]*5 + [True] + [True]*3 + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True]*5 + [False] + [True] + [False] + [True]*2 +[True] + [True] + [True] + [True] + [True] + [False] + [True]*5 + [False] + [True]*3 + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False]*3 + [True] + [False] + [True] + [False] + [True]*5 + [False] + [True] + [False]*7 + [True] + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True]*3 + [False] + [True]*5 + [False] + [True] + [False] + [True]*7 + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False]*3 + [True] + [False]*5 + [True] + [False]*3 + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False] + [True]*3 + [False] + [True]*3 + [False] + [True] + [False] + [True]*3 + [False] + [True]*5 + [False] + [True] + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False] + [True] + [False] + [True] + [False]*3 + [True] + [False]*5 + [True] + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True]*3 + [False] + [True]*7 + [False] + [True]*3 + [False] + [True] + [False] + [True]*5 + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False]*3 + [True] + [False]*5 + [True] + [False]*5 + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True]*3 + [False] + [True]*3 + [False] + [True] + [False] + [True]*7 + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False]*3 + [True] + [False] + [True] + [False] + [True] + [False] + [True] + [False]*9 + [True] + [False]*3 + [True] + [False] + [True] + [False],
    [False] + [True] + [False] + [True]*5 + [False] + [True] + [False] + [True] + [False] + [True]*3 + [False] + [True]*5 + [False] + [True]*5 + [False] + [True] + [False],
    [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False] + [True] + [False]*3 + [True] + [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False]*3 + [True] + [False],
    [False] + [True]*3 + [False] + [True]*3 + [False] + [True]*5 + [False] + [True] + [False] + [True]*3 + [False] + [True]*3 + [False] + [True]*3 + [False] + [True] + [False],
    [False] + [True] + [False] + [True] + [False]*3 + [True] + [False]*5 + [True] + [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False]*5 + [True] + [False],
    [False] + [True] + [False] + [True]*3 + [False] + [True] + [False] + [True]*3 + [False] + [True]*5 + [False] + [True] + [False] + [True]*3 + [False] + [True]*5 + [False],
    [False] + [True] + [False]*3 + [True] + [False]*3 + [True] + [False] + [True] + [False] + [True]*5 + [False]*3 + [True] + [False]*3 + [True] + [False]*5,
    [False] + [True]*3 + [False] + [True]*5 + [False] + [True]*9 + [True] + [True]*9 + [True],   #Startingpoint
    [False]*31
]

#parameters
trys = 10
Paths = []
delai = (10**6)       #visible delay = 10**7        to slow the ball movement
delai_1 = delai_2 = delai   
q3 = delai
cols, rows = len(L[0]), len(L)
jk = True
color_ball, color_passage, color_limit, dots_1, dots_2 = 'red', 'light blue', 'black', 'blue', 'red'

for _ in range(trys):
    print(_+1)
    cond = True
    while cond:
        #parametres
        done, track, el, amd = False, True, True, True
        m_down, m_up, m_right, m_left = False, False, False, False
        s, one_time = True, True        # s for first move (to avoid an error later)
        
        pygame.init()       # simulation init
                
        infoObject = pygame.display.Info()      # screen dimensions
        screen_width = infoObject.current_w
        screen_height = infoObject.current_h
        
        r_x, r_y = screen_width//cols, screen_height//rows      # longueur/largeur des rectangles
        radius = min(r_x, r_y) / 2      # rayon de la boule
        
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Maze Solving")      # titre de la simulation
        
        finals = [(r_x*(15.5), r_y*(0.5))]      # zone cible
        x_1, y_1 = finals[-1]
        x, y = r_x*(30.5), r_y*(29.5)       # coordonnees du depart
        
        while not done:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
                    done = True
            
            def make_maze():        # creation du labyrinthe
                def square(B,i,j):
                    if B: clr = color_passage
                    else: clr = color_limit
                    pygame.draw.rect(screen, clr, pygame.Rect(j*r_x, i*r_y, r_x, r_y))
                    
                for j in range(cols):
                    for i in range(rows):
                        square(L[i][j],i,j)
            
            def check(d,a,b):       # wall detection
                k, l = int(a//r_x), int(b//r_y)
                if d == 'DOWN': return L[l+1][k]
                elif d == 'UP': return L[l-1][k]
                elif d == 'RIGHT': return L[l][k+1]
                elif d == 'LEFT': return L[l][k-1]
            
            make_maze()
            pygame.draw.rect(screen, 'blue', pygame.Rect(x_1-r_x*0.5, y_1-r_y*0.5, r_x, r_y))
            
            def draw_circle(latence):
                for i in range(latence): pass         # loop to slow the ball movement
                pygame.draw.circle(screen, color_ball, (x,y), radius, width = 0)
                pygame.display.flip()
                pygame.draw.circle(screen, color_passage, (x,y), radius, width = 0)
            
            if amd:
                draw_circle(delai)
                amd = not amd
            if s:            #first move
                draw_circle(delai)
                x -= r_x
                draw_circle(delai)
                s = not s
            
            def only_move(move):
                if move == 'DOWN': return (0,r_y)
                elif move == 'UP': return (0,-r_y)
                elif move == 'RIGHT': return (r_x,0)
                elif move == 'LEFT': return (-r_x,0)
            
            def opp(m):
                if m == 'RIGHT': return 'LEFT'
                elif m == 'LEFT': return 'RIGHT'
                elif m == 'UP': return 'DOWN'
                elif m == 'DOWN': return 'UP'
            
            M, Last_move, Last_checkpoint, Deleted = ['DOWN', 'UP', 'LEFT', 'RIGHT'], [['RIGHT', x, y]], [], []
            '''checkpoint: box with more than one possible movement,
               deleted: a possible path from a checkpoint leading to a dead end or a previous checkpoint'''
            
            def movement():
                dx = x - x_1
                dy = y - y_1
                if dx >= 0 and dy >= 0:
                    H = ['UP', 'LEFT']
                    random.shuffle(H)
                    return H + ['RIGHT', 'DOWN']
                elif dx <= 0 and dy >= 0:
                    H = ['RIGHT', 'UP']
                    random.shuffle(H)
                    return H + ['LEFT', 'DOWN']
                elif dx <= 0 and dy <= 0:
                    H = ['RIGHT', 'DOWN']
                    random.shuffle(H)
                    return H + ['LEFT', 'UP']
                elif dx >= 0 and dy <= 0:
                    H = ['LEFT', 'DOWN']
                    random.shuffle(H)
                    return H + ['RIGHT', 'UP']
            
            a = False
            while (x,y) not in finals:
                count = 0
                if a:
                    count += 1
                    a = not a
                C0 = False
                while True and (x,y) not in finals:
                    if _ > 0:
                        M = movement()
                    elif _ == 0:
                        M = ['DOWN', 'UP', 'LEFT', 'RIGHT']
                        random.shuffle(M)
                    Q = [i for i in M if check(i,x,y)==True and i != Last_move[-1][0]]
                    #mouvements possibles autre que revenir en arriere
                    if len(Q)>1:        #2 ou 3 mouvements possibles
                        if True in [(x,y)==C[:-2] for C in Last_checkpoint + Deleted]:
                            ch = Last_checkpoint[-1]
                            for i in range(count):
                                p = Last_move.pop()
                                f = only_move(p[0])
                                x += f[0]
                                y += f[1]
                                draw_circle(q3)
                            ch[2].pop(0)
                        else:
                            Last_checkpoint.append((x,y,Q,count))
                        C0 = True
                        break
                    elif len(Q)==1:     # un seul mouvement possible
                        Last_move.append([opp(Q[0]), x, y])
                        f = only_move(Q[0])
                        x += f[0]
                        y += f[1]
                        count += 1
                        draw_circle(q3)
                    elif len(Q)==0:     # dead end -> return to last checkpoint
                        ch = Last_checkpoint[-1]
                        for i in range(count):
                            p = Last_move.pop()
                            f = only_move(p[0])
                            x += f[0]
                            y += f[1]
                            draw_circle(q3)
                        ch[2].pop(0)
                        C0 = True
                        break
                if C0:
                    if Last_checkpoint[-1][2]!= []:
                        f = only_move(Last_checkpoint[-1][2][0])
                        L_q = Last_checkpoint[-1][2][0]
                        Last_move.append([opp(L_q), x, y])
                        x += f[0]
                        y += f[1]
                        a = True
                        draw_circle(q3)
                    else:
                        T = Last_checkpoint.pop()
                        Deleted.append(T)
                        wee = T[-1]
                        for i in range(wee):
                            p = Last_move.pop()
                            f = only_move(p[0])
                            x += f[0]
                            y += f[1]
                            draw_circle(q3)
            
            def new_addition(i,j):
                if i > 0 and j == 0: return 'RIGHT'
                elif i < 0 and j == 0: return 'LEFT'
                elif i == 0 and j > 0: return 'DOWN'
                elif i == 0 and j < 0: return 'UP'
            
            def reduce(Q):      # optimiser le chemin trouve, supprimer les passages inutiles
                RET = []
                for j in range(1,len(Q)+1):
                    for i in range(len(Q)-j,1,-1):
                        x1 = Q[i][1]
                        x2 = Q[-j][1]
                        y1 = Q[i][2]
                        y2 = Q[-j][2]
                        dx = x1 - x2
                        dy = y1 - y2
                        dr = j - i
                        if (abs(dx) == r_x and abs(dy) == 0 or abs(dx) == 0 and abs(dy) == r_y) and dr > 2:
                                RET += Q[i+1:j]
                                rtt = new_addition(dx,dy)
                                Q[i] = [rtt, x1, y1]    # depends on how many moves were deleted
                Q = [i for i in Q if i not in RET]
            
            if (x,y) in finals:     # arriver a la zone cible
                if el:
                    print(len(Last_move))
                    el = not el
                pygame.draw.circle(screen, dots_2, (x,y), radius, width = 0)
                if one_time:
                    pygame.draw.circle(screen, color_passage, (x,y), radius, width = 0)
                    for i in Last_move[::-1]:
                        f = only_move(i[0])
                        x += f[0]
                        y += f[1]
                        draw_circle(q3)
                    for i in Last_move:
                        f = only_move(opp(i[0]))
                        x += f[0]
                        y += f[1]
                        draw_circle(delai_1)
                        pygame.draw.circle(screen, dots_1, (x,y), radius/2, width = 0)  #blue
                    for i in Last_move[::-1]:
                        f = only_move(i[0])
                        x += f[0]
                        y += f[1]
                        draw_circle(q3)
                    
                    def inter_vide(A,B):
                        st_1 = set(tuple(i) for i in A)
                        st_2 = set(tuple(i) for i in B)
                        st = st_1.union(st_2)
                        if len(st) == len(A) + len(B): return True
                        else: return False
                    
                    RET, N_A, skip = [], [], 0
                    for j in range(len(Last_move)-1, 1, -1):    # block de reduction du chemin
                        if skip != 0:
                            skip -= 1
                            continue
                        for i in range(j):
                            x1 = Last_move[i][1]
                            x2 = Last_move[j][1]
                            y1 = Last_move[i][2]
                            y2 = Last_move[j][2]
                            dx = x1 - x2
                            dy = y1 - y2
                            dr = j - i
                            if (abs(dx) == r_x and abs(dy) == 0 or abs(dx) == 0 and abs(dy) == r_y) and dr > 2:
                                TN = Last_move[i+1:j]
                                RET += TN
                                skip = len(TN)
                                rtt = new_addition(dx,dy)
                                N_A.append((i,[rtt, x1, y1]))
                                print('TN: ',TN)
                                print('RET: ',RET)
                    for C in N_A:
                        Last_move[C[0]] = C[1]
                    Last_move = [i for i in Last_move if i not in RET]
                    
                    for i in Last_move:
                        f = only_move(opp(i[0]))
                        x += f[0]
                        y += f[1]
                        draw_circle(delai_2)
                        pygame.draw.circle(screen, dots_2, (x,y), radius/2, width = 0)  #red
                    
                    if Last_move not in [C[0] for C in Paths]:
                        Paths.append([Last_move, len(Last_move), _+1])
                        print(_+1, len(Last_move))
                        if _ < trys - 1:
                            cond = not cond
                            done = not done
                    else:
                        done = not done
                    
                    one_time = not one_time
                    if jk and _ == trys - 1:
                            print([C[1:][::-1] for C in Paths])
                            print(min([C[1] for C in Paths]))
                            print()
                            jk = not jk
print(min([len(i) for i in Paths]))

'''
20/12/2023 00:05  _First succes at solving a single path maze (maze_num_1, difficulty 0).
28/12/2023 19:42  _First succes at slowing ball movement.
__________ 23:34  _First succes at solving different mazes with multiple paths (maze_num_2, difficulty 1).
30/12/2023 11:41  _Succes with any type of maze, now into reducing the path taken to finish line.
__________ 22:24  _Succes with reducing path taken to finish line.
25/02/2024 15:15  _Fixing a few bugs: ready for any kind of maze.
__________ 15:30  _Testing different mazes (16x16, 32x32). Works perfectly.
'''
