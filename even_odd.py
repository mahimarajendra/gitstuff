pass
        os=0
        es=0
        l=len(input2)
        if l==3:
            while input1>0:
                x=input1%10
                if x%2!=0:
                    os=os+x
                input1=input1//10 
            return os
        else:
            while input1>0:
                x=input1%10
                if x%2==0:
                    es=es+x
                input1=input1//10
            return es       
