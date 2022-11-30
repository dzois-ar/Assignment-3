import abc
#create an interface for the strategy
class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def doT_Shirt(self, color, size, fabric):
        pass


#create concrete strategy classes
class T_ShirtCredit(Strategy):
    def doT_Shirt(self, color, size, fabric ):
        return  f"{color} Size:{size} Fabric:{fabric} and pay with: Creadit / Debit cards"

class T_ShirtMoney(Strategy):
    def doT_Shirt(self, color, size, fabric ):
         return   f"{color} Size:{size} Fabric:{fabric} and pay with: Money / Bank Transfer"

class T_ShirtCash(Strategy):
    def doT_Shirt(self, color, size, fabric):
        return  f"{color} Size:{size} Fabric:{fabric} and pay with: Cash"    


#create context(transportation strategy)
class T_Shirt:
    def __init__(self,strategy):
        self.strategy=strategy
        


    def executeStrategy(self, color, size, fabric):
        return self.strategy.doT_Shirt( color, size, fabric)        



#Main-Client and control input to main
if __name__=="__main__":
    
    #  control input  to variation color 
    menu="""    1) Press 1 select RED color
    2) Press 2 to select ORANGE color
    3) Press 3 to select YELLOW  color 
    4) Press 4 to select GREEN  color 
    5) Press 5 to select BLUE  color 
    6) Press 6 to select INDIGO  color 
    7) Press 1 to select VIOLET  color 
    8) Press 8 to EXIT 
    """
    while True:
        print(menu)                                                                 
        color_choice = int(input("Select one Color:"))

        if color_choice not in range(1,8):
            print("Select one  Number from list ")
       
        if color_choice == 1:
            color =  "RED"
            break

        if color_choice == 2:
            color =  "ORANGE" 
            break

        if color_choice == 3:
            color =  "YELLOW" 
            break 


        if color_choice == 4:
            color =  "GREEN " 
            break 

        if color_choice == 5:
            color =  "BLUE"
            break     

        if color_choice == 6:
            color =  "INDIGO"  
            break 

        if color_choice == 7:
            color =  "VIOLET" 
            break         

        if color_choice == 8:
            break    

    print("_"*100)
    print("_"*100) 
     
     #  control input  to variation size
    menu1="""    1) Press 1 select XS size
    2) Press 2 to select S size
    3) Press 3 to select M size
    4) Press 4 to select L size
    5) Press 5 to select XL size
    6) Press 6 to select XXL size
    7) Press 7 to select XXXL size
    8) Press 8 to EXIT
    """
    
    while True:
        print(menu1)                                                                  
        size_choice = int(input("Select one Size:"))

        if size_choice not in range(1,8):
            print("Select one  Number from list ")
       
        if size_choice == 1:
            size =  "XS"
            break

        if size_choice == 2:
            size =  "S" 
            break

        if size_choice == 3:
            size =  "M" 
            break 


        if size_choice == 4:
            size =  "L " 
            break 

        if size_choice == 5:
            size =  "XL"
            break     

        if size_choice == 6:
            size =  "XXL"  
            break 

        if size_choice == 7:
            size =  "XXXL" 
            break         

        if size_choice == 8:
            break    
    

    
    print("_"*100)
    print("_"*100)  

     #  control input  to variation  fabric
    menu2="""    1) Press 1 select WOOL fabric
    2) Press 2 to select COTTON fabric
    3) Press 3 to select POLYESTER fabric
    4) Press 4 to select RAYON fabric
    5) Press 5 to select LINEN fabric
    6) Press 6 to select CASHMERE fabric
    7) Press 7 to select SILK fabric
    8) Press 8 to EXIT
    """
    
    while True:
        print(menu2)                                                                  
        fabric_choice = int(input("Select one Fabric:"))

        if fabric_choice not in range(1,8):
            print("Select one  Number from list ")
       
        if fabric_choice == 1:
            fabric =  "WOOL "
            break

        if fabric_choice == 2:
            fabric =  "COTTON" 
            break

        if fabric_choice == 3:
            fabric =  "POLYESTER" 
            break 


        if fabric_choice == 4:
            fabric =  "RAYON " 
            break 

        if fabric_choice == 5:
            fabric =  "LINEN"
            break     

        if fabric_choice == 6:
            fabric =  "CASHMERE"  
            break 

        if fabric_choice == 7:
            fabric =  "SILK" 
            break         

        if fabric_choice == 8:
            break

    print("_"*100)
    print("_"*100)
    
    print('The order is:')
    context=T_Shirt(T_ShirtCredit())
    print("The T-Shrit to choose has Color:" +str (context.executeStrategy(color, size, fabric)))

    context=T_Shirt(T_ShirtMoney())
    print("The T-Shrit to choose has Color:" +str (context.executeStrategy(color, size, fabric)))

    context=T_Shirt(T_ShirtCash())
    print("The T-Shrit to choose has Color:" +str (context.executeStrategy(color, size, fabric)))
  

   
    