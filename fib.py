class fib: # Useful fibonacci functions
    
    def fib_to_dic(n): # Houses the fibonacci sequence onto a dictionary with index
        fib_dic = {'0' : 0, '1' : 1}
        for i in range(1,n):
            fib_dic[str(i+1)] = fib_dic[str(i)] + fib_dic[str(i-1)]
        return fib_dic

    def fib_to_list(n): # Makes list of fibonacci numbers
        fib_list = [0,1]
        for i in range(1, n):
            fib_list.append(fib_list[(i-1)]+fib_list[i])
        return fib_list

    def get_fib(n): # Gets the fibonacci number at the given index
        a, b = 0, 1
        for i in range(0, n):
            a, b = b, a + b
        return a