marks = int(input("Please enter your marks?"))
#totalmarks = 0
if marks >= 89:
    print("Congratulation, you got first position with grade A.")
elif marks >= 79 and marks < 89:
    print("You are passed with grade B.")
elif marks >= 69 and marks < 79:
    print("You got garde C.")
elif marks >= 59 and marks < 69:
    print("You got grade D.") 
elif marks >= 49 and marks < 59:
    print("you got grade E.")       
else:
    print("Unfortunately, you are failed.")    