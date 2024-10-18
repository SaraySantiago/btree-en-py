#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe
class bnodo: 
    __info = None
    __de = None
    __iz = None

def __init__(self,info = None ) -> None: 
    self.__info = info

def __str__(self) -> str:
    answ = "("
    if self.__iz == None:
        answ += "(.)"
    if self.__de == None:
        answ += "(.)"
    answ += str (self.__info) 
    answ += ")"
    return answ 

if __name__ == "__main__":
    bn0 = bnodo ()
    print (bn0)