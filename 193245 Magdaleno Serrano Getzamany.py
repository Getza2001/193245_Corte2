
import threading
import time

cola = []
class TenedorFilosofo(threading.Thread):
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        self.datoTemporal =  (self.filosofosNum + 1) % 5
    
    def hilosFilosofos(self):
        
        print("filosofos ", self.filosofosNum)
        #print("dato temporal: ", self.datoTemporal)
   
        ban = True

        while ban:
            
            if not self.filosofosNum in cola:
                cola.append(self.filosofosNum)
                ban=False  
                
                print("Filosofo iniciando", self.filosofosNum)
                print("Filosofo ", self.filosofosNum, "pasando tenedor del lado izquierdo")
                self.tenedores[self.filosofosNum].acquire()
            
                print("Filosofo ", self.filosofosNum, "recoge tenedor del lado derecho")
                self.tenedores[self.datoTemporal].acquire()

                print("Filosofo ", self.filosofosNum, "libre derecho")
                self.tenedores[self.datoTemporal].release()
            
                print("Filosofo ", self.filosofosNum, "libre izquierdo")
                self.tenedores[self.filosofosNum].release()


           # time.sleep(2)
            
    def run(self):
        self.hilosFilosofos()


tenedorArray = [1,1,1,1,1]

for i in range(0,5):
    tenedorArray[i] = threading.BoundedSemaphore(1)

for i in range(0,5):
    total = TenedorFilosofo(tenedorArray, i)
    total.start()
    time.sleep(2)