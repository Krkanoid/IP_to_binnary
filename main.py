import time

class Main(object):
    def main(self):
        list = []
        for i in range(4):
            global unos
            unos = int(input("Unesi prvu točke IP-a:  "))
            if(unos > 255):
                print ("Error!")
                time.sleep(2)
                exit()
            else:
                list.append(unos)
        print("""
        
        """)
        for j in range(4):
            if(j == 3):
                print (list[j], end = " ")
                break
            else:
                print (list[j], end = "       .      ")
        print ("\n")
        for k in range(5):
            if(k == 0):
                print (" ↓", end = " ")
            elif(k > 1):
                for raz in range(15):
                    print (" ",end = "")
                print ("↓ ", end = "")
        print("\n")
        for r in range(4):
            if(r == 0):
                print ("", end = "")
                dec = list[j]
                print (bin(dec), end = " ")
            else:
                for razz in range(3):
                    print("  ", end = "")
                dec = list[j]
                print (bin(dec), end = " ")
 
if __name__ == '__main__':
    Main().main()
