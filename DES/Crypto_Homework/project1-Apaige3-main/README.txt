Project 1: DES simulation

Due: 1:50pm, Thursday, 2/3/2022


1. DES_Simultion
   - Main simulation engine
   - Completed (do not modify)
   
2. Conversion
   - Provides utility functions for conversion between a string 
     of characters and a binary string
   - Not part of DES
   - Completed (do not modify)

3. DES
   - Includes encryption and decryption algorithms
   - Completed (do not modify)


3. IP
   - Initial permutation
   - Complete *permute()*

4. FeisteNetwork
   - Consists of 16 rounds. 
   - This class includes the f-function with four steps: Expansion, Xor, S-box substitution, Permutation 
   - Complete *iterate()*, *xor()*, *expansion()*, *sBoxes()*, *pPermutation()* 


5. IPinverse
   - Final permutation, inverse of the initial permutation
   - Complete *permute()*  

6. KeySchedule
  - Includes key scheduling algorithms for both encryption and decryption
  - Complete *pc_1()*, *p_2()*, *generateSubkeysForDecryption()*

7. To run the DES_Simulation class, provide two command line arguments 
   for a file name for plaintext and another file name for the key
   To run, type “python3 DES_Simulation.py plaintext.txt key.txt”
   
   With the given txt files, expected output after completion is:

ciphertext: 1101001111100010001000011001111011010111100110110111111000000111
Successful
recovered Text: Hi World


8. .txt files are included:
   - The plaintext.txt file contains exactly 8 characters which fit in a block of 64 bits. 
   - The key.txt file contains a key of 64 bits.
   - You may create your own plaintext and keys.
 
 
   
    
