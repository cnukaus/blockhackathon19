import re


#print(locate_time("Mo45+2 Y"))



def locate_time(str):
    return re.search(r"([0-9]+)[+]?([0-9]+)", str).start(),re.search("([0-9]+)[+]?([0-9]+)", str).end()

def sort_by_time(timepart):
	# truncate things after +
    return timepart[:timepart.find("+")]

def parse_line(line):
    # 3 parts: Name(may have space), time, Type and possible typeS Name2
    pos1,pos2=locate_time(line)
    return line[:pos1].strip(),line[pos1:pos2],line[pos2:],sort_by_time(line[pos1:pos2])



def store_result(arr):


   
    ranked_line=[]
    for line in arr:
        result=parse_line(line)
        ranked_line.append(result)
    ranked_line.sort(key=lambda x : x[3] )

    print(ranked_line)
        
        


store_result(["Mo45+2 Y","Mo Sa 44+2 Y"])