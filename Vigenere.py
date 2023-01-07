import string
Operation = int(input("You Have {Cipher and Key or Paintext and Key} or {PainText an Cipher}? (0/1)  :  "))
print("\n---------------------Vignere---------------------\n")

# 0
if Operation == 0:

    try :

        #input Cipher and Key
        Cipher = input("Enter the Cipher/PainText : ")
        Key = input("Enter your key for encrypting : ")

        # Convert letters to numbers
        nCipher = []
        nKey = []
        list1 = string.ascii_lowercase
        
        for i in range(0,len(Key)):
            
            for j in range(0,26):
                if Key[i] == list1[j]:
                    nKey.append(j)

                if Cipher[i] == list1[j]:
                    nCipher.append(j)
                    
        # Subtract Key from Cipher to create Paintex 
        nPainText = []

        for i in range(0,len(Key)):
            nk = nKey[i]
            nc = nCipher[i]
            nPainText.append(nk-nc)


        # Convert numberical list to wordlist
        PainText = []

        for i in range(0,len(nPainText)):
            a = nPainText[i]
            PainText.append(list1[a])


        print("\nUnencrypted/Encrypted massage : { ",''.join(PainText)," }")

    except:
        print("ERROR")

#1
elif Operation == 1:
    try:
        # Input Cipher and PainText
        PainText = input("Enter the Paintext :")
        Cipher = input("Enter the Cipher : ")

        # Convert letters to numbers
        nCipher = []
        nPainText = []
        list1 = string.ascii_lowercase
                
        for i in range(0,len(PainText)):
                    
            for j in range(0,26):
                if PainText[i] == list1[j]:
                    nPainText.append(j)

                if Cipher[i] == list1[j]:
                    nCipher.append(j)

        # Subtract 26 from Paintext and add to Cipher to create Paintex 
        nKey = []

        for i in range(0,len(PainText)):
            nk = nPainText[i]-26
            nc = nCipher[i]
            nKey.append(nk+nc)

        # Convert numberical list to wordlist
        Key = []

        for i in range(0,len(nPainText)):
            a = nKey[i]
            Key.append(list1[a])

        print("\nUnencrypted/Encrypted massage : { ",''.join(Key)," }")

    except :
        print("ERROR")

else:
    print("ERROR")

