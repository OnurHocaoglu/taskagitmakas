class game():
    def main(gir):
        taskagitmakas= ["taş","kağıt","makas"]
        import random
        tas = taskagitmakas[0]
        kagit = taskagitmakas[1]
        makas = taskagitmakas[2]
        pckazandi=0
        benkazandim=0
        pcsetkazandi=0
        setkazandim=0
        while True:
            gir = input("Taş mı Kağıt mı Makas mı ? : ")
            a =random.choice(taskagitmakas)
            print("bilgisayar", a, "seçti")
            if gir ==kagit:
                if kagit==a:
                    print("berabere kaldınız")
                elif tas==a:
                    print("kazandınız")
                    benkazandim += 1
                elif makas ==a:
                    print("kaybettiniz")
                    pckazandi +=1
            elif gir== tas:
                if tas== a:
                    print("berabere kaldınız")
                elif  kagit==a:
                    print("kaybettiniz")
                    pckazandi += 1
                elif makas ==a:
                    print("kazandınız")
                    benkazandim +=1
            elif gir == makas:
                if makas ==a:
                    print("berabere kaldınız")
                elif tas ==a:
                    print("kaybettiniz")
                    pckazandi +=1
                elif kagit ==a:
                        print("kazandınız")
                        benkazandim+=1
            if (pckazandi==2):
                print("SEti Pc Kazandi")
                pcsetkazandi+=1
                pckazandi=0
                benkazandim=0
            elif (benkazandim==2):
                print("Tebrikler Seti Kazandınız")
                setkazandim+=1
                benkazandim=0
                pckazandi=0
            if (pcsetkazandi==2):
                print("""
            -------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------                                   
            -----------------------------------GAME OVER-----------------------------------------
            -------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------""")
                break
            elif (setkazandim==2):
                print("""
            -------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------                                   
            ------------------------------TEBRİKLER OYUNU KAZANDINIZ-----------------------------
            -------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------""")
                break
        
print("""
          -------------------------------------------------------------------------------------
          -------------------------------------------------------------------------------------                                   
          -------------------------Taş Kağıt Makas Oyununa HoşGeldiniz-------------------------
          -------------------------------------------------------------------------------------
          -------------------------------------------------------------------------------------""")

oyunabasla = input("Oyuna Başlamak İçin Bir Tuşa Basın")
game.main(oyunabasla)