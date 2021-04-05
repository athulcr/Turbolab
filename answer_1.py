def findProcessors(start, stop, n):
    s=0
    for i in range(0,n-1):
        if (stop[i]>start[i+1]):
            s=s+1 
    return(s)

 

start=[900,940,950,1000,1500,1600]
stop=[910,1020,1010,1015,1620,1700]
n = len(start)
print("Minimum Number of Processors Required = ", findProcessors(start, stop, n))
