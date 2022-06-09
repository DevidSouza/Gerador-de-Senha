from tkinter import *
from random import choice
from tkinter import ttk
from tkinter import messagebox

cor1 = '#225077' # azul escuro
cor2 = '#0e0f0f' # preto
cor3 = '#f9f9f9' # branco
cor4 = '#1b59b7' # azul claro
cor5 = '#02a6d8' # azul bebe
cor6 = '#36bc3b' # verde claro
cor7 = '#eada2c' # amarelo
cor8 = '#d34d43' # vermelho

jan = Tk()
jan.title('GERADOR DE SENHA')
jan.geometry('320x380')
jan.resizable(width=False, height=False)
# carregando imagem
imagem = PhotoImage(file='imagens/senha.png')

# definindo estilo da janela
estilo = ttk.Style(jan)
estilo.theme_use('alt')

# variáveis necessárias para o funcionamento do prograna
quanti_caracteres = 0
alfa_maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfa_minuscula = 'abcdefghijklmnopqrstuvwxyz'
numeros = '1234567890'
simbolos = '[}-_.,;(:@{#$]%\)/'
senha = ''

senha_gerada = '- - -'
valor_selecionado1, valor_selecionado2, valor_selecionado3, valor_selecionado4 = StringVar(), StringVar(), StringVar(), StringVar()
valor_selecionado1.set(False), valor_selecionado2.set(False), valor_selecionado3.set(False), valor_selecionado4.set(False)

# criando funções
def gerarsenha():
    global senha_gerada, senha, alfa_minuscula, alfa_maiuscula, numeros, quanti_caracteres
    quanti_caracteres = int(spin.get())

    alfa_maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfa_minuscula = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '1234567890'
    simbolos = '[}-_.,;(:@{#$]%\)/'
    senha = ''

    #looping
    while True:
        if '1' == valor_selecionado1.get():
            maiu = choice(alfa_maiuscula)
            senha += maiu
            if len(senha) == quanti_caracteres:
                break

        if '2' == valor_selecionado2.get():
            minu = choice(alfa_minuscula)
            senha += minu
            if len(senha) == quanti_caracteres:
                break

        if '3' == valor_selecionado3.get():
            num = choice(numeros)
            senha += num
            if len(senha) == quanti_caracteres:
                break

        if '4' == valor_selecionado4.get():
            sim = choice(simbolos)
            senha += sim
            if len(senha) == quanti_caracteres:
                break
        if '1' != valor_selecionado1.get() and '2' != valor_selecionado2.get()\
                and '3' != valor_selecionado3.get() and '4' != valor_selecionado4.get():
            senha = '- - -'
            break

    senha_gerada = senha
    label_senha['text'] = senha_gerada

def copiarsenha():
    global senha_gerada
    frame_corpo.clipboard_append(senha_gerada)

    messagebox.showinfo('Informação copiada', 'Informação copiada com sucesso!')
    frame_corpo.clipboard_clear()

# criando frames
# frame título
frame_titulo = Frame(jan, width=320, height=50, bg=cor3)
frame_titulo.grid(row=0, column=0)

# exibindo imagem no frame do título
imagem_titulo = Label(frame_titulo, image=imagem, bg=cor3)
imagem_titulo.place(x=8, y=8)

# texto do frame título
label_titulo = Label(frame_titulo, text='GERADOR DE SENHA', font=('Arial 18 bold'), fg=cor1, bg=cor3)
label_titulo.place(x=46, y=8)

# frame linha separador
frame_linha = Frame(jan, width=320, height=10, bg=cor7)
frame_linha.grid(row=1, column=0)

# frame corpo
frame_corpo = Frame(jan, width=320, height=320, bg=cor3)
frame_corpo.grid(row=2, column=0)

# a seguir, uma das maneiras de alterar a borda de uma label através de frames:
# passo 1: defina uma variável. crie um frame nela (este frame deve se situar numa janela ou noutro frame
# que exibirá a label com a borda), sem definir tamanho, apenas a cor que se deseja para a borda;
# passo 2: através da função place, dê as coordenadas de onde deseja que a o frame apareça;
# passo 3: crie uma label e defina seus atributos;
# passo 4: utilize a função pack para definir a espessura da borda.
# veja a seguir >
cor_borda_label = Frame(frame_corpo, bg=cor1)
cor_borda_label.place(x=5, y=10)

cor_borda_botao1 = Frame(frame_corpo, bg=cor1)
cor_borda_botao1.place(x=230, y=10)

# criando label que exibirá a senha
label_senha = Label(cor_borda_label, text=senha_gerada, width=25, height=2, pady=2, fg=cor1, font=('Arial 10 bold'))
label_senha.pack(padx=2, pady=2)

# criando botao de copiar senha
botao_copiar = Button(cor_borda_botao1, command=copiarsenha, text='Copiar', width=10, height=2, pady=2, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
botao_copiar.pack(padx=1, pady=1)

# criando label 'Número total de caracteres na senha'
label_texto = Label(frame_corpo, text='Número total de caracteres na senha', width=30, height=1, fg=cor1, bg=cor3, font=('Arial 10 bold'))
label_texto.place(x=2, y=58)

# criando uma Spinbox
spin = Spinbox(jan, from_=4, to=20, width=5)
spin.place(x=9, y=143)

# criando chackbuttons
check_botao1 = Checkbutton(frame_corpo, pady=10, bg=cor3, activebackground=cor3, variable=valor_selecionado1, onvalue='1', offvalue=OFF)
check_botao1.place(x=5, y=100)

check_botao2 = Checkbutton(frame_corpo, pady=10, bg=cor3, activebackground=cor3, variable=valor_selecionado2, onvalue='2', offvalue=OFF)
check_botao2.place(x=5, y=140)

check_botao3 = Checkbutton(frame_corpo, pady=10, bg=cor3, activebackground=cor3, variable=valor_selecionado3, onvalue='3', offvalue=OFF)
check_botao3.place(x=5, y=180)

check_botao4 = Checkbutton(frame_corpo, pady=10, bg=cor3, activebackground=cor3, variable=valor_selecionado4, onvalue='4', offvalue=OFF)
check_botao4.place(x=5, y=220)

# criando labels dos checkbuttons
label_check1 = Label(frame_corpo, text='ABC Letras maiúsculas', width=20, height=1, fg=cor1, font=('Arial 10 bold'), bg=cor3)
label_check1.place(x=25, y=110)

label_check2 = Label(frame_corpo, text='abc Letras minúsculas', width=20, height=1, fg=cor1, font=('Arial 10 bold'), bg=cor3)
label_check2.place(x=25, y=150)

label_check3 = Label(frame_corpo, text='123 Números', width=12, height=1, fg=cor1, font=('Arial 10 bold'), bg=cor3)
label_check3.place(x=25, y=190)

label_check4 = Label(frame_corpo, text='(*# Símbolos', width=12, height=1, fg=cor1, font=('Arial 10 bold'), bg=cor3)
label_check4.place(x=25, y=230)

botao_gerar_senha = Button(frame_corpo, command=gerarsenha, text='Gerar senha', width=42, height=2, padx=4, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
botao_gerar_senha.place(x=5, y=275)

jan.mainloop()
