import rospy
from find_object_2d.msg import ObjectsStamped

class NesneTanima():
    def __init__(self):
        rospy.init_node("nesne_tanima_oret")
        rospy.Subscriber("objectsStamped",ObjectsStamped,self.nesneTani)
        rospy.spin()
        

    def nesneTani(self,mesaj):
        try:
            self.nesne_id = mesaj.objects.data[0]
            if (self.nesne_id == 1):
                print("Sola Donulmez")
            if (self.nesne_id == 2):
                print("Sola Mecburi")
            if (self.nesne_id == 3):
                print("Saga Mecburi")
            if (self.nesne_id == 4):
                print("Saga Donulmez")        
 
            if (self.nesne_id == 5):
                print("Durak")
            if (self.nesne_id == 6):
                print("Girisi Olmayan Yol")
            if (self.nesne_id == 7):
                print("Engelli Park")
            if (self.nesne_id == 8):
                print("Park")
            if (self.nesne_id == 9):
                print("Park Yasak")
           
           # if (self.nesne_id == 10):
            #    print("Ada Etrafinda Don")
            #if (self.nesne_id == 11):
             #   print("Kirmizi İsik")
            #if (self.nesne_id == 12):
             #   print("Yesil İsik")
            
        except IndexError:
            print("HATA: Obje bulunamadi!")



NesneTanima()
