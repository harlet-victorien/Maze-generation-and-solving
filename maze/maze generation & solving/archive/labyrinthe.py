
#* Labyrinthe                                                                   

#* Modules                                                                   
import pygame as p
import random 
import copy
import csv
import time





#* Setup de la fenêtre                                                            


p.init()
fenetre = p.display.set_mode((1600, 950))
backGroundColor=p.Color("LIGHTGREY")
fenetre.fill(backGroundColor)

#- 0=vide 1=mur 2=player 3=entrée 4=sortie
#- pour des cases de 20*20 on aurait 31*43 cases maximum

#* Setup des variables                                                          

#- Matrices de labyrinthes de test
L=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

L2=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

Limp=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

T = [[1,1,1,1,1,1,1,1,1],
[1,4,0,0,1,0,0,0,1],
[1,1,1,0,1,0,0,0,1],
[1,1,1,0,1,0,0,0,1],
[1,1,1,0,1,0,1,1,1],
[1,1,1,0,0,0,1,1,1],
[1,1,1,1,1,0,1,1,1],
[1,0,0,0,0,0,0,0,1],
[1,3,1,1,1,1,1,1,1]]

H = [(0, 0, 1, 0, 0, 0, 1, 4),
 (1, 0, 0, 0, 1, 0, 1, 0),
  (1, 0, 1, 1, 1, 0, 0, 0),
   (1, 0, 0, 1, 0, 0, 1, 1),
    (0, 1, 0, 1, 0, 1, 0, 1),
     (0, 0, 0, 1, 0, 1, 0, 1),
      (0, 1, 1, 1, 0, 0, 0, 0),
       (0, 0, 0, 0, 0, 0, 0, 0)]

#- police pour les numéros et ou textes

font1 = p.font.SysFont('sysfont', 1)
font2 = p.font.SysFont('sysfont', 1)
color='#%02x%02x%02x' % (213, 30, 250)
color2='#D922FD'










#* Toutes les fonctions                                                                 


#- Fonction de conversion de la matrice tiled

def conversionMatrice(file):
    with open(file,'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    for j in range (len(data)):
        for i in range(len(data[j])):
            if data[j][i]=='4999':
                data[j][i]=1
            if data[j][i]=='-1':
                data[j][i]=0
            if data[j][i]=='4954':
                data[j][i]=4
            if data[j][i]=='4904':
                data[j][i]=3
    return data

#- Fonction principale du test de labyrinthe

def labyPoss (L):
    global posSor
    global posDep
    
    
    for i in {0,len(L)-1}:
        for j in range (len(L[0])) :
            if L[i][j]==4:
                posSor=(i,j)
            if L[i][j]==3:
                posDep=(i,j)
    x,y=posDep[0]-1,posDep[1]
    R=[[(x,y)]]
    while len(R[0])>=1 :
        for C in R :
            x,y = C[len(C)-1]
            if x>=len(L) or y>=len(L[0])-1 or x<0 or y<0:
                return('no')
            if L[x][y]==4:
                return('yes',C)
            
            for i in range(4):
                if deplacement(L,x,y)[i]:
                    if i==0 and not((x-1,y) in C):
                        R=R+[C+[(x-1,y)]]
                    if i==1 and not((x,y+1) in C):
                        R=R+[C+[(x,y+1)]]
                    if i==2 and not((x+1,y) in C):
                        R=R+[C+[(x+1,y)]]
                    if i==3 and not((x,y-1) in C):
                        R=R+[C+[(x,y-1)]]
                    
                if len(R)==0:
                    return('no')
                    img1 = font1.render('IMPOSSIBLE', True, 'red')
                    fenetre.blit(img1, (100, 100)) 
                for K in range(len(R)):
                    if R[K]==C:
                        del(R[K])
                        break
    return('no')
    img1 = font1.render('IMPOSSIBLE', True, 'red')
    fenetre.blit(img1, (100, 100)) 



#- Check des directions de déplacements possibles

def deplacement(L,x,y):
    N,E,S,W = 1,1,1,1
    if L[x+1][y] in (1,3):
        S=0
    if L[x-1][y] in (1,3):
        N=0
    if L[x][y+1] in (1,3):
        E=0
    if L[x][y-1] in (1,3):
        W=0
    return(N,E,S,W)

#- Fonction de déplacement pour la création de labyrinthe

def deplacement_créa(L,x,y):
    N,E,S,W = 1,1,1,1
    #on vérifie si les cases sont dans le labyrinthe
    if x+1>=len(L) or L[x+1][y] ==1:
        S=0
    if x-1<0 or L[x-1][y] ==1:
        N=0
    if y+1>=len(L[0]) or L[x][y+1] ==1:
        E=0
    if y-1<0 or L[x][y-1] ==1:
        W=0
    return(N,E,S,W)

#- Affichage

def affichage (L):
    fenetre.fill(backGroundColor)
    for i in range (len(L)):
        img1 = font1.render(str(i), True, '#575757')
        fenetre.blit(img1, (28, 50+5*i))   
        for j in range (len(L[0])) :
            if i==0:
                img1 = font1.render(str(j), True, '#575757')
                fenetre.blit(img1, (52+5*j, 28))  
            if L[i][j]==1:
                p.draw.rect(fenetre, '#575757', (50+5*j, 50+5*i, 5, 5))
            if L[i][j]==3:
                p.draw.rect(fenetre, 'red', (50+5*j, 50+5*i, 5, 5))
            if L[i][j]==4:
                p.draw.rect(fenetre, 'green', (50+5*j, 50+5*i, 5, 5))
    p.display.flip()
#- Affichage en cours de création

def affichage_en_création (L):
    fenetre.fill(backGroundColor)
    for i in range (len(L)):
        img1 = font1.render(str(i), True, '#575757')
        fenetre.blit(img1, (28, 50+5*i))   
        for j in range (len(L[0])) :
            if i==0:
                img1 = font1.render(str(j), True, '#575757')
                fenetre.blit(img1, (52+5*j, 28))  
            if L[i][j]==1:
                p.draw.rect(fenetre, '#575757', (50+5*j, 50+5*i, 5, 5))
            if L[i][j]==3:
                p.draw.rect(fenetre, 'red', (50+5*j, 50+5*i, 5, 5))
            if L[i][j]==4:
                p.draw.rect(fenetre, 'green', (50+5*j, 50+5*i, 5, 5))
           
            if L[i][j]!=1:    
                img1 = font2.render(str(L[i][j]), True, '#ee5757')
                fenetre.blit(img1, (50+5*j, 50+5*i))  
    p.display.flip()

#- Affichage du tracé de la solution

def affichageSolution (S):
    
    colors_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    gradient = create_gradient(len(S)+2)
    print(gradient)
    for i in range (len(S)):
        P=S[i]
        if P==posSor :
            break
        
        p.draw.rect(fenetre, gradient[i], (50+5*P[1], 50+5*P[0], 5, 5))
        time.sleep(0.05)
        p.display.flip()

#- Affichage d'un chemin

def affichageChemin (C):
    c=255
    a=255
    b=0
    a1,b1,c1=1,1,1
    for P in C:
        if c>=5:
            c-=c1
        else:
            c=0
        if a>=5:
            a-=a1
        else:
            a=0
        if b<=250:
            b+=b1
        else:
            b=255
        color='#%02x%02x%02x' % (b, c, a)
        p.draw.rect(fenetre, color, (50+5*P[1], 50+5*P[0], 5, 5))

#- Création d'un labyrinthe aléatoire





def labyAlea (n,m):
    #L est le labyrinthe
    #C est la liste des chemins
    #M est la liste des murs
    #n et m sont les dimensions du labyrinthe
    #c est le numéro sur la case en commençant par 5
    #x et y sont les coordonnées de la case actuelle
    #N,E,S,W sont les directions de déplacement possibles
    #R est la liste des chemins possibles

    

    n=2*n//2+1
    m=2*m//2+1
    c=4
    L = [[1 for j in range(m)] for i in range(n)]
    #mettre des 1 sur les bords
    for j in range(m):  
        L[0][j]=1
        L[n-1][j]=1
    for i in range(n):
        L[i][0]=1
        L[i][m-1]=1
    #on affiche 
    for i in range(n):
        for j in range(m):
            if i%2!=0 and j%2!=0:
                c+=1
                L[i][j]=c

   
    C=labyChemins(L)
    Cobj=copy.deepcopy(C[:])
    
    for i in Cobj:
        i[1]=5

    while C!=Cobj :
        M=labyMurs(L)
        P=random.choice(M)
        
        x,y=P[0],P[1]

        if deplacement_créa(L,x,y)[0] and deplacement_créa(L,x,y)[2]:
        
            if L[x-1][y] != L[x+1][y]:
                if L[x-1][y] < L[x+1][y]:
                    update_values(L, L[x+1][y], L[x-1][y])
                else:
                    update_values(L, L[x-1][y], L[x+1][y])
                L[x][y] = 5
        

        elif deplacement_créa(L,x,y)[1] and deplacement_créa(L,x,y)[3]:
            
            
            
            if L[x][y-1] != L[x][y+1]:
                if L[x][y-1] < L[x][y+1]:
                    update_values(L, L[x][y+1], L[x][y-1])
                else:
                    update_values(L, L[x][y-1], L[x][y+1])
                L[x][y] = 5
      

        C=labyChemins(L)
        
     
    for i in L:
        for j in i:
            if j ==5 :
                j=0

   
       
    #mettre la sortie en haut à droite et l'entrée en bas à gauche
    
    y,z=random.randint(2,m-4),random.randint(2,m-4)
    y=y//2*2+1
    z=z//2*2+1
    L[0][z]=4
    L[1][z+1]=0
    L[1][z]=0
    L[1][z-1]=0
    L[2][z+1]=0
    L[2][z]=0
    L[2][z-1]=0


    L[n-1][y]=3
    L[n-2][y-1]=0
    L[n-2][y+1]=0
    L[n-2][y]=0
    L[n-3][y-1]=0
    L[n-3][y+1]=0
    L[n-3][y]=0


    return(L)


#- Création d'un labyrinthe aléatoire au ralenti




def labyAlea_ralenti (n,m):
    #L est le labyrinthe
    #C est la liste des chemins
    #M est la liste des murs
    #n et m sont les dimensions du labyrinthe
    #c est le numéro sur la case en commençant par 5
    #x et y sont les coordonnées de la case actuelle
    #N,E,S,W sont les directions de déplacement possibles
    #R est la liste des chemins possibles

    

    n=2*n//2+1
    m=2*m//2+1
    c=4
    L = [[1 for j in range(m)] for i in range(n)]
    #mettre des 1 sur les bords
    for j in range(m):  
        L[0][j]=1
        L[n-1][j]=1
    for i in range(n):
        L[i][0]=1
        L[i][m-1]=1
    #on affiche 
    for i in range(n):
        for j in range(m):
            if i%2!=0 and j%2!=0:
                c+=1
                L[i][j]=c

    #print(L)
    affichage_en_création(L)
    C=labyChemins(L)
    Cobj=copy.deepcopy(C[:])
    
    for i in Cobj:
        i[1]=5
    #print(Cobj)
    while C!=Cobj :
        M=labyMurs(L)
        P=random.choice(M)
        
        x,y=P[0],P[1]
        #print(x,y)
        #print(L[x][y])
        if deplacement_créa(L,x,y)[0] and deplacement_créa(L,x,y)[2]:
            

            if L[x-1][y] != L[x+1][y]:
                img1 = font2.render(str(L[x-1][y]), True, '#119911')
                fenetre.blit(img1, (50+5*y, 50+5*(x-1)))  
                img1 = font2.render(str(L[x+1][y]), True, '#119911')
                fenetre.blit(img1, (50+5*y, 50+5*(x+1)))  
                p.display.flip()
                #print(L[x-1][y], L[x+1][y])
                #time.sleep(1)
                if L[x-1][y] < L[x+1][y]:
                    update_values(L, L[x+1][y], L[x-1][y])
                else:
                    update_values(L, L[x-1][y], L[x+1][y])
                L[x][y] = 5
        

        elif deplacement_créa(L,x,y)[1] and deplacement_créa(L,x,y)[3]:
            
            if L[x][y-1] != L[x][y+1]:
                img1 = font2.render(str(L[x][y-1]), True, '#119911')
                fenetre.blit(img1, (50+5*(y-1), 50+5*(x)))  
                img1 = font2.render(str(L[x][y+1]), True, '#119911')
                fenetre.blit(img1, (50+5*(y+1), 50+5*(x)))  
                p.display.flip()
                #print(L[x][y-1], L[x][y+1])
                #time.sleep(1)
                if L[x][y-1] < L[x][y+1]:
                    update_values(L, L[x][y+1], L[x][y-1])
                else:
                    update_values(L, L[x][y-1], L[x][y+1])
                L[x][y] = 5
        #print(L)
        affichage_en_création(L)

        C=labyChemins(L)
        
        #time.sleep(1)

    for i in L:
        for j in i:
            if j ==5 :
                j=0

   
       
    #mettre la sortie en haut à droite et l'entrée en bas à gauche
    
    y,z=random.randint(2,m-3),random.randint(2,m-3)
    y=y//2*2+1
    z=z//2*2+1
    L[0][z]=4
    L[1][z+1]=0
    L[1][z]=0
    L[1][z-1]=0
    L[2][z+1]=0
    L[2][z]=0
    L[2][z-1]=0


    L[n-1][y]=3
    L[n-2][y-1]=0
    L[n-2][y+1]=0
    L[n-2][y]=0
    L[n-3][y-1]=0
    L[n-3][y+1]=0
    L[n-3][y]=0
    


    return(L)




#- Changer les grandes valeurs en petites
def update_values(L, old_val, new_val):
    """
    Updates all occurrences of old_val in the labyrinth L with new_val.
    """
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == old_val:
                L[i][j] = new_val


#- Création de la liste avec que les murs

def labyMurs (L):
    L2=[]
    for i in range (1,len(L)-1):
        for j in range (1,len(L[0])-1) :
            if (i+j)%2!=0 and L[i][j]==1:
                L2.append((i,j))
    return(L2)

#- Création de la liste avec que les chemins

def labyChemins (L):
    L2=[]
    for i in range (1,len(L)-1):
        for j in range (1,len(L[0])-1) :
            if i%2!=0 and j%2!=0:
                L2.append([(i,j),L[i][j]])
    return(L2)    


def encadrement_chemin(C,L):
    for P in C:
        x,y=P[0],P[1]
        if x-1>=0:
            if not((x-1,y) in C) and L[x-1][y]!=4 and L[x-1][y]!=3:
                L[x-1][y]=1
        if y+1<len(L[0]):
            if not((x,y+1) in C) and L[x][y+1]!=4 and L[x][y+1]!=3:
                L[x][y+1]=1
        if x+1<len(L):
            if not((x+1,y) in C) and L[x+1][y]!=4 and L[x+1][y]!=3:
                L[x+1][y]=1
        if y-1>=0:
            if not((x,y-1) in C) and L[x][y-1]!=4 and L[x][y-1]!=3:
                L[x][y-1]=1
        L[x][y]=0
    return(L)
                    
    
# def labyalea_mais2(n,m):
#     for i in range(n):

def rajouter_encadrement(M):#rajouter un encadrement de 1 autour d'un labyrinthe
    n=len(M)
    m=len(M[0])
    L=[[1 for j in range(m+2)] for i in range(n+2)]
    for i in range(n):
        for j in range(m):
            L[i+1][j+1]=M[i][j]

    return(L) 

#- Création du dégradé de couleur

def create_gradient(steps):
    """Crée un dégradé de couleurs à partir de quatre couleurs aléatoires."""
    
    # Choix de quatre couleurs aléatoires pour créer le dégradé
    colors = []
    for i in range(4):
        color = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)
        colors.append(color)

    # Ajout des couleurs de départ et d'arrivée à la liste de couleurs
    start_color, end_color = colors[0], colors[-1]
    colors.insert(0, start_color)
    colors.append(end_color)

    # Création du dégradé de couleurs
    gradient = []
    for i in range(steps):
        # Calcul de la position de couleur actuelle sur l'axe des couleurs
        pos = i / (steps - 1)

        # Interpolation linéaire des couleurs
        if pos <= 0:
            color = colors[0]
        elif pos >= 1:
            color = colors[-1]
        else:
            start = int(pos * 3)
            end = start + 1
            frac = (pos * 3) - start
            r = int((1 - frac) * colors[start][0] + frac * colors[end][0])
            g = int((1 - frac) * colors[start][1] + frac * colors[end][1])
            b = int((1 - frac) * colors[start][2] + frac * colors[end][2])
            color = (r, g, b)

        gradient.append(color)

    return gradient



#* Execution                                                                    


#-Labyrinthe à étudier

Liste_à_étudier = labyAlea(20,20)
#-Execution des fonctions

n=0

affichage(Liste_à_étudier)

#time.sleep(5)




poss = labyPoss(Liste_à_étudier)


""" while poss[0]=='yes':
    n+=1
    print(n)
    Liste_à_étudier = labyAlea(40,40)
    poss = labyPoss(Liste_à_étudier) """


if poss[0]=='yes':

    affichageSolution(poss[1])
else : 
    #afficher un message d'erreur dans la fenetre au milieu de l'écran
    img1=font1.render("Pas de solution",True,'#119911')
    fenetre.blit(img1,(200,200))
    p.display.flip()







#- Pour quitter la fenetre

continuer = 1
while continuer:

    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()



    p.display.flip()






#* Fin Du Code                    