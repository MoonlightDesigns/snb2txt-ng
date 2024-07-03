'''
REFERENCIAS:
    https://realpython.com/command-line-interfaces-python-argparse/
    https://www.w3schools.com/python/showpython.asp?filename=demo_file_open

    https://stackoverflow.com/questions/2900035/changing-file-extension-in-python

    https://www.geeksforgeeks.org/working-zip-files-python/

    https://www.w3schools.com/python/python_regex.asp
    
    https://blog.enterprisedna.co/python-write-to-file/

'''




# Passo 1: Criar tela de comandos com o argumento -h

import sys, os, re, shutil

from zipfile import ZipFile


if (len(sys.argv)) == 1:
    print('Insira um argumento !')
    sys.exit()
   
elif(len(sys.argv)) < 9:
    
    if sys.argv[1] == '-h' or sys.argv[1] == '-help':
        print('Copie o arquivo .snb para a mesma pasta do script e digite\n python snb2txt-ng.py -i <nome-do-arquivo.snb> -o <nome-do-arquivo> <formatacao> -f [y OU n] <sistema-operacional> -so [ win ou unix ]')
 
        sys.exit()

    else:
        print('Argumentos insuficientes, digite -h para ajuda ..')
        sys.exit()
    
else:
    #print('Erro ! argumentos incompativeis, digite -h para ajuda ..')
    pass
    
    
    
    
    
# Passo 2: Alterar o formato de arquivo de snb para zip, navegar no zip e ir para a pasta aonde o arquivo se encontra


#VARIAVEIS

# print(sys.argv[1]) --> snb2txt-ng.py
file_snb = sys.argv[2]  # -->  -i <nome-do-arquivo.snb>
file_txt = sys.argv[4] # -->  -o <nome-do-arquivo>
fmt_opt = sys.argv[6] # --> formatacao do texto
os_plat = sys.argv[8] # --> Sistema operacional

# print('\n')
# print(file_snb)
# print(file_txt)
# print(fmt_opt)

#print(list(sys.argv))

base = os.path.splitext(file_snb)[0]
extens = os.path.splitext(file_snb)[1]

#print(base)
#print(extens)

if extens != '.snb':
    print('Anquivo nao e do tipo [ .snb ]')

else:
    os.rename(file_snb, base + '.zip')
    #pass

with ZipFile(base +'.zip', 'r') as zip:
    #zip.printdir()

    zip.extract('snote/snote.xml')
    
    file_xml = open('snote/snote.xml', 'r').read()





# Passo 3: Fazer o regex da pagina, removendo todo o conteudo que se encontra entre as tags <?>

file_xml_edit = re.sub('\<[^\>]+\>','',file_xml)





#Passo 4: Salvar o resultado do regex em um arquivo txt no mesmo diretorio presente


if fmt_opt == 'n':
    #print(file_xml_edit)
    #print('\n')
    
    if os_plat != 'unix':
        data_txt = open(f"{file_txt}.txt", "w", newline="\r\n")
    
    else:
        data_txt = open(f"{file_txt}.txt", "w", newline="\n")
        
    data_txt.write(file_xml_edit)
    data_txt.close()

        # with open(f"{file_txt}.txt", "w") as f:
            # print(file_xml_edit, file=f)
            
        # f.close()


elif fmt_opt == 'y':
    data_list = [s.strip() for s in file_xml_edit.split("\t") if len(s) > 0]
    print(*data_list)

    if os_plat != 'unix':
        data_txt = open(f"{file_txt}.txt", "w", newline="\r\n")
        
    else:
        data_txt = open(f"{file_txt}.txt", "w", newline="\n")
    
    data_txt.write(*data_list)
    data_txt.close()

        # with open(f"{file_txt}.txt", "x") as f:
            # print(*data_list, file=f)
            
        # f.close()

else:
    print('Insira a formatacao do texto ! { -f (y OU n) }')



# Opcional Passo 5: Deletar o conteudo remanescente ( zip, snb, etc...)

os.remove(base + '.zip')
shutil.rmtree('snote')