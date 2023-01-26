from copy import copy, deepcopy
        
def pr1():
    l = [1,[2,4],5,[5,5,7]]
    l1 = l + []
    
    l1[0] = 7
    print "pr1-1-l", l
    print "pr1-1-l1", l1

    l1[1][0] = 8
    print "pr1-2-l", l
    print "pr1-2-l1", l1

def pr2():
    l = [1,[2,4],5,[5,5,7]]
    l1 = copy(l)
    
    l1[0] = 7
    print "pr2-1-l", l
    print "pr2-1-l1", l1

    l1[1][0] = 8
    print "pr2-2-l", l
    print "pr2-2-l1", l1



def pr3():
    l = [1,[2,4],5,[5,5,7]]
    l1 = deepcopy(l)
    
    l1[0] = 7
    print "pr3-1-l", l
    print "pr3-1-l1", l1

    l1[1][0] = 8
    print "pr3-2-l", l
    print "pr3-2-l1", l1
    
def main():
    pr1()
    pr2()
    pr3()

    
main()

