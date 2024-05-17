import string
import sys
morse={'A':'.-','B':'-...','C':'-.-.','Ç':'-.-..','CH':'----','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','Ñ':'--.--','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',".":".-.-.-",",":"--..--","?":"..--..","\"":".-..-.","/":"-.."}
llM=string.ascii_letters+string.digits+'chCHñÑ.,?"/ '

def cesar(i):
    """
    >>> cesar('Bon dia')
    Escriu la clau: 'Dqp fkc'
    """
    clau=int(input("Escriu la clau: "))
    fi=""
    p=string.ascii_lowercase*2
    f=[]
    for k in p:
        f+=k
    F=[]
    P=string.ascii_uppercase*2
    for j in P:
        F+=j
    for y in i:
        if y in f:
            fi+=f[clau+f.index(y)]
        elif y in F:
            fi+=F[clau+F.index(y)]
        else:
            fi+=y

    return fi

def asci(text):
    """
    >>> asci('Bon dia')
    '66 111 110 32 100 105 97 '
    """
    #text to ascii
    #f=[]
    fi=""
    for j in text:
        #if j in string.ascii_letters:
        fi+=str(ord(j))+" "

    
    return fi

def icsa(num):
    """
    >>> icsa('66 111 110 32 100 105 97')
    'Bon dia'
    """
    #ascii to text
    chars =num.split()
    text = ''.join(chr(int(char)) for char in chars)
    return text

def llegirFitxer():
    text = ""
    fitxer = input("Entra nom del fitxer per llegir: ")
    while True:
        try:
            with open(fitxer + ".txt", "r") as f:
                for linia in f:
                    text += linia
            break  # Si se encuentra el archivo, salir del bucle
        except FileNotFoundError:
            print("El fitxer no existeix. Torna a provar.")
            fitxer = input("Entra un altre nom del fitxer per llegir: ")
    return text


def escriureFitxer(text):
    fitxer=input("Entra nom del fitxer per escriure: ")
    f=open(fitxer+".txt","w")
    f.write(text)
    f.close()

def rasec(i):
    """
    >>> rasec('Anm chz')
    Anm chz
    <BLANKLINE>
    1.Si
    2.No
    Es correcte gramaticalment la frase anterior? Bon dia
    <BLANKLINE>
    1.Si
    2.No
    Es correcte gramaticalment la frase anterior? 'Bon dia'
    """
    clau=0
    Correcte=False
    while not Correcte:
        fi=""
        p=string.ascii_lowercase*2
        f=[]
        for k in p:
            f+=k
            F=[]
            P=string.ascii_uppercase*2
        for j in P:
            F+=j
        for y in i:
            if y in f:
                fi+=f[clau+f.index(y)]
            elif y in F:
                fi+=F[clau+F.index(y)]
            else:
                fi+=y
        print(fi)
        l='0'
        while l!='2':
            l=input("\n1.Si\n2.No\nEs correcte gramaticalment la frase anterior? ")
            if l=='1':
                return fi
            elif l=='2':
                clau+=1

def crearFitxer():
    text=input("Escriu el contingut del fitxer: ")
    fitxer=input("Entra nom del fitxer per escriure: ")
    f=open(fitxer+".txt","w")
    f.write(text)
    f.close()

    
def MorseToText(txt):
    morse= {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J','-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T','..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z','-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9','/': ' '}
    palabras = txt.split(' / ')
    texto = ''
    for palabra in palabras:
        letras = palabra.split()
        for letra in letras:
            if letra in morse:
                texto += morse[letra]
            else:
                texto += '?'  # Caracter de interrogación si no se reconoce el código Morse
        texto += ' '  # Espacio entre palabras
    return texto.strip()

def TextToMorse(y):
    texto=y.upper()
    mors=''
    for caracter in texto:
        if caracter in morse:
            mors += str(morse[caracter] + ' ')
        else:
            mors += str('/ ')  # Caracter de espacio si no se encuentra el caracter en el diccionario
    return mors.strip()

def menu1():
    y=5
    while y!='1' and y!='2' and y!='3':
        y=input("\n1.Fer servir fitxer d'entrada/sortida\n2.No fer servir fitxer d'entrada/sortida\n3.Sortir\nEscull opcio: ")
    if y=='3':
        print("Tancant programa...")
        sys.exit()
    return y

def menu2(y):
    x=9
    while x!=7:
        x=input("\n1.Encriptar a ascii\n2.Desencriptar des de ascii\n3.Encripta a cesar\n4.Desencriptar des de cesar\n5.Encriptar a Morse\n6.Desencriptar des de Morse\n7.Crear un fitxer\n8.Sortir\nEscull opcio: ")
        if x=="1":
            if y=='1':
                text=llegirFitxer()
                t=asci(text)
                escriureFitxer(t)
            else:
                text=input("Introdueix text: ")
                print(asci(text))
        elif x=="2":
            if y=='1':
                text=llegirFitxer()
                t=icsa(text)
                escriureFitxer(t)
            else:
                text=input("Introdueix text: ")
                print(icsa(text))
        elif x=="3":
            if y=='1':
                text=llegirFitxer()
                t=cesar(text)
                escriureFitxer(t)
            else:
                text=input("Introdueix text: ")
                print(cesar(text))
        elif x=="4":
            if y=='1':
                text=llegirFitxer()
                t=rasec(text)
                escriureFitxer(t)
            else:
                text=input("Introdueix text: ")
                print(rasec(text))
        elif x=='5':
            if y=='1':
                text=llegirFitxer()
                t=TextToMorse(text)
                escriureFitxer(t)
            else:
                text=input("Introdueix text: ")
                print(TextToMorse(text))
        elif x=='6':
            if y=='1':
                text=llegirFitxer()
                t=MorseToText(text)
                escriureFitxer(t)
            else:
                text=input("Introdueix text: ")
                print(MorseToText(text))
        elif x=='7':
            crearFitxer()
        elif x=='8':
            print("Tancant programa...")
            break
    return x
if __name__=='__main__':
    r=menu1()
    j=menu2(r)
    while j=='8':
        r=menu1()
        j=menu2(r)
