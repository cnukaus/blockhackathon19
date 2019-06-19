# about 90 minutes used
def balancedOrNot(expressions, maxReplacements):
    # Write your code here
    result=[]
    for index,exp_current in enumerate(expressions):
        result.append(check_replace(exp_current,maxReplacements[index]))
    print(result)
    return result


def getCount(exp_input):
    all_freq={}
    for i in exp_input: 
        if i in all_freq:
            all_freq[i]+=+1
        else:
            all_freq[i]=1
    
    #get count
    symbol1=all_freq["<"]
    symbol2=all_freq[">"]

    return symbol1,symbol2

def get_imbalance(exp_input):
    # 2 conditions in sequential scan: 1. "<" count >= ">" Count; 2. when scan ends, the count is equal
    # if True then it is balanced
    left_count=0
    right_count=0
    result=True
    for i,char in enumerate(exp_input):
        print(char)
        if char=="<":
            left_count+=1
        elif char==">":
            right_count+=1
        else:
            pass

        if left_count < right_count:
            result=False
    if left_count != right_count:
        result=False
    
    return result



def check_replace(exp_input,max_replace):
    # left count <= right count is the only possibility to make a balance by adjusting
    
    status_now=getCount(exp_input)
    while status_now[0] != status_now[1] and max_replace>0:
        max_replace=max_replace-1
        if status_now[0] > status_now[1]:
            return 0

        # remove paired and compare the remaining substring
        exp_input=exp_input.replace("<>","")

        #use the replace rule once
        exp_input=exp_input.replace(">","<>",1)
        print(exp_input,"max",max_replace)

        status_now=getCount(exp_input)
        print(status_now,"result")
    
    print(status_now,"_FNIAL")
    if get_imbalance(exp_input):
        return 1
    else:
        return 0
        
balancedOrNot(["<<>>","<<>>","<<<<><>>>>>>>","<<<<><>>>>>>>","<<>"],[0,5,1,8,11])