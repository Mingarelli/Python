#Given an integer x, return true if x is a palindrome, and false otherwise.

#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.

#Example 2:
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
#Therefore it is not a palindrome.

#Example 3:
#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    # Método que verifica se um número é um palíndromo
    # Method that checks if a number is a palindrome
    def isPalindrome(self, x: int) -> bool:
        # Converte o número para uma string para facilitar a comparação dos caracteres
        # Converts the number to a string to easily compare characters
        texto = str(x)

        # Variável para armazenar o resultado do teste de palíndromo
        # Variable to store the result of the palindrome test
        teste = False

        # Loop para percorrer cada caractere da string
        # Loop to iterate through each character in the string
        for i in range(len(texto)):
            # Verifica se o caractere atual é igual ao caractere correspondente do final da string
            # Checks if the current character is equal to the corresponding character from the end of the string
            if texto[i] == texto[len(texto) - 1 - i]:
                # Se os caracteres são iguais, continua testando
                # If the characters are equal, continue testing
                teste = True
            else:
                # Se algum par de caracteres não for igual, retorna False (não é palíndromo)
                # If any pair of characters is not equal, return False (not a palindrome)
                return False

        # Retorna True se todos os caracteres corresponderem, indicando que é um palíndromo
        # Returns True if all characters match, indicating it is a palindrome
        return teste


# Testa o método isPalindrome com diferentes exemplos
# Tests the isPalindrome method with different examples
if __name__ == '__main__':
    # Deve retornar True, pois 121 é um palíndromo
    # Should return True because 121 is a palindrome
    print(Solution.isPalindrome('Exemplo1', 121))

    # Deve retornar False, pois -121 não é um palíndromo (devido ao sinal de menos)
    # Should return False because -121 is not a palindrome (due to the negative sign)
    print(Solution.isPalindrome('Exemplo2', -121))

    # Deve retornar False, pois 10 não é um palíndromo
    # Should return False because 10 is not a palindrome
    print(Solution.isPalindrome('Exemplo3', 10))
