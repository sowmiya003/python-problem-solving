a="stone";
b="paper";
c="scissor";
d=input("enter the input");
e=input("enter the input");
if(d=="stone" and e=="paper"):
    print("paper wins")
elif(d=="paper" and e=="scissor"):
    print("scissor wins")
elif(d=="scissor" and e=="stone"):
    print("stone wins")
else:
    print("draw match")
