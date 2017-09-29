u=0
a=-g=9.8
def function(t):
    if t == '-1' or t == '11':
        return
    t_sum = 0
    for i in range(0,len(t)):
        t_sum = t_sum + int(t[i:i+1])
    print('zip(' + t + ')=' , t_sum)
    function(str(t_sum))
if __name__ == '__main__':
    t = input('enter a number:')
    function(v)
