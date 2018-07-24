def anim_sound(anim,sound):
    print ("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print ("And on the farm he had a",anim+", Ee-igh, Ee-igh, Oh!")
    print ("With a "+sound+", "+sound+" here and a "+sound+", "+sound+" there.")
    print ("Here a "+sound+", there a "+sound+" everywhere a "+sound+", "+sound+".")
    print ("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def song():
    anim_sound(anim="pig", sound="oink")
    print ("")
    anim_sound(anim="cow", sound="moo")
    print ("")
    anim_sound(anim="duck", sound="quack")
    print ("")
    anim_sound(anim="chicken", sound="b-caw")
    print ("")
    anim_sound(anim="frog", sound="ribbit")

song()
