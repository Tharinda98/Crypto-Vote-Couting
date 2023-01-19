from phe import paillier


pub_key, priv_key = paillier.generate_paillier_keypair()

#encrypt each value in a list
def encrypt_list(pub_key,list):
    encrypted_list=[]
    for i in list:
        encrpted_i=pub_key.encrypt(i)
        encrypted_list.append(encrpted_i)
    return encrypted_list


#decrypt each value in a list
def decrypt_list(priv_key,list):
    decrypted_list=[]
    for i in list:
        decrypted_i=priv_key.decrypt(i)
        decrypted_list.append(decrypted_i)
    return decrypted_list


#get the encrypted sum of a 2d array
def sumOfArrayList(array_list):
    sum_list=[]
    l=len(array_list[1])
    for i in range(l):
        temp_sum=array_list[0][i]
        
        for j in range(1,len(array_list)):
            temp_sum = temp_sum+array_list[j][i]
        sum_list.append(temp_sum)
    return sum_list
        
#votes       
num1 = [1,0,0]
num2 = [1,0,0]

#encrypted votes
num1=encrypt_list(pub_key,num1)
num2 = encrypt_list(pub_key, num2)

#making a encrypted vote list
array_list=[]
array_list.append(num1)
array_list.append(num2)

#sum of the encrypted votes
sum=sumOfArrayList(array_list)
#decrypt the sum
result=decrypt_list(priv_key,sum)
print(result)
