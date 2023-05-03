#Clase encargada de La pagina Resolver Ecuacion
class PageOne(tk.Frame):
    def __init__(self, master):#Constructor
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7")
        tk.Label(self, text="Elige la gráfica a crear", font=('San Francisco', 20),width=50,height=1,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        tk.Button(self,text="Grafica dirigida",font=('San Francisco', 20),width=50,height=3,cursor="heart",bg="#2d424a",
            command=lambda: [master.switch_frame(Directed)]).pack()
        tk.Button(self,text="Grafica no dirigida",font=('San Francisco', 20),width=50,height=3,cursor="heart",bg="#5f6468",
            command=lambda: [master.switch_frame(NoDirected)]).pack()
        tk.Button(self, text="Regresar el menu Anterior",font=('San Francisco', 20),width=50,height=3,cursor="heart",bg="#b4786b",
                command=lambda: master.switch_frame(StartPage)).pack() 
def obtener(var2,inicio,rectatangente,cifras):#Son sinonimos para la asignacion
    global ec1
    global puntoinicio
    global derivada,redondeo
    redondeo=cifras
    ec1=var2
    puntoinicio=inicio
    derivada=rectatangente
def obtener2(ecuacion2,inicio1,inicio2,cifrass2):#Son sinonimos para la asignacion
    global ec2
    global puntoinicio1,puntoinicio2
    global cifras2
    ec2=ecuacion2
    puntoinicio1=inicio1
    puntoinicio2=inicio2
    cifras2=cifrass2
##Funcion que nos ayudara a darle valores a la funciones
def evaluadora(funcion,punto):
    sp.symbols("x")
    return(sp.sympify(funcion).subs("x",punto))

def createNewWindow(topventana,ecuacion2):
    global ec2
    ec2=ecuacion2
    listan=[]
    lista1=listan
    lista2=listan
    newWindow = tk.Toplevel(topventana)
    newWindow.title("Grafico")
    fig=plt.figure()

    ax = fig.add_subplot(2, 1, 1) # two rows, one column, first plot
    FIGURE=FigureCanvasTkAgg(fig,master=newWindow)
    FIGURE.get_tk_widget().grid(row=8,column=8)
    #Creamos un boton para realizar el grafico
    lista1=[]
    lista2=[]
    for i in range(100):
        lista1.append(i-100)
        lista2.append(evaluadora(ec2,str(i-100)))
    for i in range(100):
        lista1.append(i)
        lista2.append(evaluadora(ec2,str(i)))
    x=lista1
    y=lista2
    plt.plot(color="blue", linewidth=2.5, linestyle="-", label=("F(x)="+ec2))
    plt.plot(x,y)
    fig.canvas.draw()
    #Fm1=tk.Toplevel(topventana)
    for i in range(7):
        for j in range(3):
            if(i==0):
                if(j==0):
                    Label(newWindow,text="x",width=20,bg="gray").grid(row=i,column=j,sticky="NE",padx=5, pady=5)
                if(j==1):
                    Label(newWindow,text=("F(x)="+ec2),width=20,bg="gray").grid(row=i,column=j,sticky="NE",padx=5, pady=5)
            elif(i>0):
                if(j==0):
                    Label(newWindow,text=str(i-4),width=20,bg="gray").grid(row=i,column=j,sticky="NE",padx=5, pady=5)
                if(j==1):
                    Label(newWindow,text=str(evaluadora(ec2,str(i-4))),width=20,bg="gray").grid(row=i,column=j,sticky="NE",padx=5, pady=5)


""" class Newton(tk.Frame):

    def __init__(self, master):#Constructor
        global ec1,puntoinicio,derivada,ci
        ec1=StringVar()
        puntoinicio=StringVar()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7")
        tk.Label(self, text=des1,font=('San Francisco',11),width=100,height=2,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        E1=tk.Entry(self)
        E1.pack()
        tk.Label(self, text="Agregue por favor el punto de inicio",font=('San Francisco',11),width=100,height=2,bg="#A8C3B7").pack(side="top", pady=5)
        E2=tk.Entry(self,textvariable=puntoinicio)
        E2.pack()
        tk.Label(self, text="Ingresa la derivada para resolver con el metodo",font=('San Francisco',11,"bold"),width=100,height=2,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        E3=tk.Entry(self)
        E3.pack()
        #tk.Label(self, text="Ingresa cifras a redondear (Opcional, por defecto 5)",font=('San Francisco',11,"bold"),width=100,height=2,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        #E4=tk.Entry(self)
        #E4.pack()
        tk.Button(self,text="Presiona para Tabular la funcion escrita(solo la funcion)",height=2,cursor="hand2",command=lambda: [createNewWindow(self,E1.get())]).pack()
        tk.Button(self,text="Presentar iteraciones(Deben estar el punto y derivada)",height=2,cursor="hand2",command=lambda: [obtener(E1.get(),E2.get(),E3.get(),None),master.switch_frame(Tabulacion)]).pack()
        tk.Button(self,text=" Presiona Regresar",cursor="hand2",height=2,command=lambda: [master.switch_frame(StartPage)]).pack()
      """   



##Clase tabuladora la grafica dirigida

class Tabulacion(tk.Frame):
    global ec1,puntoinicio,derivada,cifras
    global rr
    rr=6
    def __init__(self, master):#Constructor
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7") 
        #"con derivada: "+derivada+"el primer punto evaluado es: "+str(evaluadora(ec1,puntoinicio)
        tk.Label(self, text=("La ecuacion ingresada fue: "+ec1+"\nCon punto inicio 1: "+puntoinicio+"\ny Con derivada "+derivada+"\nLa tabla de iteaciones es"),font=('San Francisco',11,"bold"),width=120,height=5,bg="#A8C3B7").pack(fill="x", pady=5)
        tk.Button(self,text=" Presiona para regresar al menu Principal",cursor="hand2",height=2,command=lambda: [self2.destroy(),master.switch_frame(PageOne)]).pack()
        self2=Frame(self)
        dicelementos={}
        xn1='xn1'
        efuncion='efuncion'
        ederivada='ederivada'
        error='error'
        x=10
        for i in range(0,x):
            for j in range(5):
                if(i==0):
                    if(j==0):
                        jj="Numero de iteracion"
                        label1=Label(self2,text=str(jj),width=25).grid(row=i,column=j,sticky="e")
                    if(j==1):
                        jj="xn+1=xn-(F(xn)/D(fxn))"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                    if(j==2):
                        jj="f(xn)"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                    if(j==3):
                        jj="D(fxn)"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                    if(j==4):
                        jj="Error"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                else:
                    if(j==0):
                        #Iteracion
                        label1=Label(self2,text=str(i),width=25).grid(row=i,column=j,sticky="e")
                    if(j==1):
                        #"xn+1=xn-(F(xn)/D(fxn))"
                        if(i==1):#Donde se pondra el punto de inicio
                            label1=Label(self2,text=str(puntoinicio),width=25).grid(row=i,column=j,sticky="e")
                            dicelementos[xn1]=round(float(puntoinicio),rr)
                        #Donde ya se genero el punto de inicio
                        elif(i>1):
                            tmp1=dicelementos[xn1]#Lo guardamos en un temporal para usarlo abajo
                            dicelementos[xn1]=round(float(tmp1-(dicelementos[efuncion]/dicelementos[ederivada])),rr)#Usamos el temporal para calcular el nuevo valor
                            label1=Label(self2,text=str(dicelementos[xn1]),width=25).grid(row=i,column=j,sticky="e")
                    if(j==2):
                        #F(xn)
                        dicelementos[efuncion]=round(float(evaluadora(ec1,dicelementos[xn1])),rr)
                        label1=Label(self2,text=str(dicelementos[efuncion]),width=25).grid(row=i,column=j,sticky="e")
                        
                    if(j==3):
                        #"D(fxn)"
                        dicelementos[ederivada]=round(float(evaluadora(derivada,dicelementos[xn1])),rr)
                        label1=Label(self2,text=str(dicelementos[ederivada]),width=25).grid(row=i,column=j,sticky="e")
                    if(j==4):
                        if(i==1):
                            tmp4=float(puntoinicio)
                            label1=Label(self2,text="------",width=25).grid(row=i,column=j,sticky="e")
                        #Error
                        elif(i>1): 
                            dicelementos[error]=round(abs(float((dicelementos[xn1]-tmp4)/dicelementos[xn1])),rr)
                            label1=Label(self2,text=str(dicelementos[error]),width=25).grid(row=i,column=j,sticky="e")
                            tmp4=dicelementos[xn1]
        self2.pack()

##Clase para la creacion de la grafica no dirigida
class Tabsecante(tk.Frame):
    global ec2
    global puntoinicio1,puntoinicio2
    def __init__(self, master):#Constructor
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7") 
        #"con derivada: "+derivada+"el primer punto evaluado es: "+str(evaluadora(ec1,puntoinicio)
        tk.Label(self, text=("La ecuacion ingresada fue: "+ec2+"\nCon 1er punto inicio : "+puntoinicio1+" Y segundo punto:"+puntoinicio2+"\nLa tabla de iteraciones es:"),font=('San Francisco',11,"bold"),width=120,height=5,bg="#A8C3B7").pack(fill="x", pady=5)
        tk.Button(self,text=" Presiona para regresar al menu Principal",cursor="hand2",height=2,command=lambda: [self2.destroy(),master.switch_frame(PageOne)]).pack()
        self2=Frame(self)
        dicelementos={}
        xi1='xi-1'
        xi='xi'
        xi11='xi+1'
        fxi='fxi'
        fxi1='fxi-1'
        fxi11='fxi+1'
        Xi='Xi-Xi-1'
        error='Error'
        for i in range(10):
            for j in range(6):
                if(i==0):
                    if(j==0):
                        jj="Numero de iteracion"
                        label1=Label(self2,text=str(jj),width=25).grid(row=i,column=j,sticky="e")
                    if(j==1):
                        jj="Xi"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                    if(j==2):
                        jj="F(Xi)"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                    if(j==3):
                        jj="F(Xi-1)"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                    if(j==4):
                        jj="(Xi-Xi-1)"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                    if(j==5):
                        jj="Error"
                        label1=Label(self2,text=jj,width=25).grid(row=i,column=j,sticky="e")
                else:
                    if(j==0):
                        #Iteracion
                        label1=Label(self2,text=str(i),width=25).grid(row=i,column=j,sticky="e")
                    
                    #---------------------Xi

                    if(j==1):
                        #Xi, valor que sera generado, los primeros 2 no lo seran 
                        if(i==1):#Donde se pondra el punto de inicio
                            dicelementos[xi1]=float(puntoinicio1)
                            label1=Label(self2,text=str(puntoinicio1),width=25).grid(row=i,column=j,sticky="e")

                        if(i==2):
                            dicelementos[xi]=float(puntoinicio2)
                            label1=Label(self2,text=str(puntoinicio2),width=25).grid(row=i,column=j,sticky="e")
                        #Donde ya se genero el punto de inicio
                        elif(i>2):
                            dicelementos[xi11]=float(dicelementos[xi]-((dicelementos[fxi]*dicelementos[Xi])/(dicelementos[fxi]-dicelementos[fxi1])))
                            label1=Label(self2,text=str(dicelementos[xi11]),width=25).grid(row=i,column=j,sticky="e")
                            #
                            '''dicelementos[xi1]=dicelementos[xi]
                            dicelementos[fxi1]=dicelementos[fxi]
                            dicelementos[xi]=dicelementos[xi11]'''
                    #Despues de las iteraciones con los 2 puntos entregables anteriormente

                    ##---------------------F(XI)
                    if(j==2):
                        if(i==1):
                            dicelementos[fxi1]=float(evaluadora(ec2,puntoinicio1))
                            label1=Label(self2,text=str(dicelementos[fxi1]),width=25).grid(row=i,column=j,sticky="e")
                        if(i==2):#Referente a la primera iteracion
                            dicelementos[fxi]=float(evaluadora(ec2,puntoinicio2))
                            label1=Label(self2,text=str(dicelementos[fxi]),width=25).grid(row=i,column=j,sticky="e")
                        if(i>2):
                            dicelementos[fxi11]=float(evaluadora(ec2,(dicelementos[xi11])))
                            label1=Label(self2,text=str(dicelementos[fxi11]),width=25).grid(row=i,column=j,sticky="e")
                    #---------------------F(Xi-1)
                    if(j==3):
                        if(i==1):
                            label1=Label(self2,text="------",width=25).grid(row=i,column=j,sticky="e")
                        if(i==2):
                            label1=Label(self2,text=str(dicelementos[fxi1]),width=25).grid(row=i,column=j,sticky="e")
                        
                        elif(i>2): 
                            label1=Label(self2,text=str(dicelementos[fxi]),width=25).grid(row=i,column=j,sticky="e")

                    #---------------------Xi-Xi-1
                            
                    if(j==4):
                        if(i==1):
                            label1=Label(self2,text="------",width=25).grid(row=i,column=j,sticky="e")
                        if(i==2):
                            dicelementos[Xi]=dicelementos[xi]-dicelementos[xi1]
                            label1=Label(self2,text=str(dicelementos[Xi]),width=25).grid(row=i,column=j,sticky="e")
                            #tmp11=dicelementos[xi]
                        if(i>2):
                            #QUEREMOS REFIRMAR QUE ESTE CASO EN EL SIGUIENTE CASO SERA EL ANTERIOR OSEA XN
                            #dicelementos[xi]=dicelementos[xi11]#La actual en la siguiente sera la anterior
                            dicelementos[Xi]=float(dicelementos[xi11]-dicelementos[xi])
                            label1=Label(self2,text=str(dicelementos[Xi]),width=25).grid(row=i,column=j,sticky="e")
                    if(j==5):
                        #Calculo del Error
                        if(i==1):
                            label1=Label(self2,text="------",width=25).grid(row=i,column=j,sticky="e")

                        elif(i==2):
                            #Solamente para la primera iteracion
                            dicelementos[error]=abs((dicelementos[xi]-dicelementos[xi1])/dicelementos[xi])
                            label1=Label(self2,text=str(dicelementos[error]),width=25).grid(row=i,column=j,sticky="e")
                        elif(i>2): 
                            #El primero es dicelementos[xi] porque en la iteracion anterior ya la cambiamos
                            #dicelementos[xi11]=dicelementos[xi]
                            dicelementos[error]=float(abs(dicelementos[xi11]-dicelementos[xi])/dicelementos[xi11])
                            label1=Label(self2,text=str(dicelementos[error]),width=25).grid(row=i,column=j,sticky="e")
                            #Actualizacion de variable, debido a que se acerca una nueva iteracion 
                            #Guardamos ya que vamos a sustituir
                            tmp22=dicelementos[xi]
                            dicelementos[xi]=dicelementos[xi11]
                            dicelementos[xi1]=tmp22
                            dicelementos[fxi1]=dicelementos[fxi]
                            dicelementos[fxi]=dicelementos[fxi11]#////////////////////////
        self2.pack()



def obtenermatriz(fila):
    global tecuaciones
    tecuaciones=fila
     
        
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7")
        tk.Label(self, text="Elige el metodo a Usar", font=('San Francisco', 20),width=50,height=1,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        tk.Button(self,text="Metodo de Gauus",command=lambda: [master.switch_frame(NewWindow)],font=('San Francisco', 20),width=50,height=2,cursor="heart",bg="#2d424a").pack()
        tk.Button(self, text="Regresar el menu Anterior",font=('San Francisco', 20),width=50,height=2,cursor="heart",bg="#612a11",
                command=lambda: master.switch_frame(StartPage)).pack()
class NewWindow(tk.Frame):
    global tecuaciones
    def __init__(self, master):#Constructor
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7")
        Label(self,text="Ingresa el numero de Ecuaciones\n").pack()
        fil1=Entry(self)
        fil1.pack()
        tk.Button(self,text="Presiona despues de ingresar",command=lambda: [obtenermatriz(fil1.get()),master.switch_frame(Matriz)]).pack()
        tk.Button(self, text="Regresar el menu Anterior",font=('San Francisco', 20),width=50,height=2,cursor="heart",bg="#612a11",
                command=lambda: master.switch_frame(PageTwo)).pack()

class Matriz(tk.Frame):
    global tecuaciones
    def __init__(self, master):#Constructor
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7")
        tk.Label(self, text=des3,font=('San Francisco',11),width=100,height=2,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        fem1=Frame(self)
        for i in range(int(tecuaciones)+1):
            for j in range(int(tecuaciones)+1):
                if(i>0 and j>0 and j%1==0 and i%1==0):
                    l1=Label(fem1,text="x"+str(i)+str(j)).grid(row=i,column=j)
                elif(i>0 and j>0 and j%2==0 and i%2==0):
                    e1=Entry(fem1).grid(row=i,column=j)
        fem1.pack()
