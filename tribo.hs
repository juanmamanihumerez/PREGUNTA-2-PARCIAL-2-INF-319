Prelude> fibo a b c = a:fibo b c (a+b+c)
Prelude> take 7 (fibo 0 1 1)
[0,1,1,2,4,7,13]

