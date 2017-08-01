
# coding: utf-8

# OmirCoin
# Na OmirCoin os blocks são organizados da seguinte maneira:
# Hash anterior / usuário que paga / valor / usuário que recebe
# Obs.: O primeiro Hash será Zero.

# In[ ]:


import hashlib


# In[ ]:


quemPaga = input("Quem paga?")
valor = input("Valor?")
quemRecebe = input("Quem recebe?")
block001data = 0,quemPaga, valor,quemRecebe
block001data = str(block001data)
print(block001data)


# In[ ]:


block001 = hashlib.md5(block001data.encode('utf-8'))
print(block001.hexdigest())


# In[ ]:


quemPaga = input("Quem paga?")
valor = input("Valor?")
quemRecebe = input("Quem recebe?")
block002data = block001.hexdigest(),quemPaga, valor,quemRecebe
block002data = str(block002data)
print(block002data)


# In[ ]:


block002 = hashlib.md5(block002data.encode('utf-8'))
print(block002.hexdigest())


# In[ ]:


quemPaga = input("Quem paga?")
valor = input("Valor?")
quemRecebe = input("Quem recebe?")
block003data = block002.hexdigest(),quemPaga, valor,quemRecebe
block003data = str(block003data)
print(block003data)


# In[ ]:


print(block001data)
print(block002data)
print(block003data)

