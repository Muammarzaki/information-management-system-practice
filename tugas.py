
# inisialisi inp (input) dan expr (expresi) 
inp = "2 / 3"
#potong inp dengan delimeter blank atau spasi disimpan kedalam expr dengan type list
expr = inp.split(" ")

# jika expressi tidak berukuran 3 maka berhenti
if not len(expr) == 3:
    print("pattern cant be use")
    #paksa keluar dari python 
    exit(0)

# check bentuk expresi biner agar dapat di proses dengan operator yang sesuai
if(expr.__contains__("+")):
    # ubah operan1 dan operan2 ketype int lalu ditambah
    inp = int(expr[0]) + int(expr[2])
elif(expr.__contains__("-")):
    # dikurang
    inp = int(expr[0]) - int(expr[2])
elif(expr.__contains__("/")):
     #dibagi
     inp = int(expr[0]) / int(expr[2])
elif(expr.__contains__("*")):
     #dikali
     inp = int(expr[0]) * int(expr[2])
else:
    print("pattern cant be use")

#jika hasil keluaran proses bertype int atau float maka print hasil operasi adalah ... 
if(type(inp)==int or float):
    print(f"hasil operasi adalah {inp}")
#jika hasil keluaran proses bertype selain int atau float maka print operasi gagal
else:
    print(f"operasi gagal")
