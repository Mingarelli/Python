#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two ones added together.
#12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
# which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9.
#X can be placed before L (50) and C (100) to make 40 and 90.
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.

#Example 1:
#Input: s = "III"
#Output: 3
#Explanation: III = 3.

#Example 2:
#Input: s = "LVIII"
#Output: 58
#Explanation: L = 50, V = 5, III = 3.

#Example3:
#Input: s = "MCMXCIV"
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

#Constraints:
#1 <= s.length <= 15
#s contains only the characters('I', 'V', 'X', 'L', 'C', 'D', 'M').
#It is guaranteed that s is a valid roman numeral in the range[1, 3999].

#class Solution:
#    def romanToInt(self, s: str) -> int:

class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a lista de símbolos romanos e seus valores correspondentes.
        # Defines the list of Roman symbols and their corresponding values.
        symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value = [1, 5, 10, 50, 100, 500, 1000]

        # Inicializa a variável para armazenar a soma e o índice.
        # Initializes the variable to store the sum and the index.
        sum = 0
        j = 0

        # Inicia um loop infinito até que seja interrompido manualmente.
        # Starts an infinite loop until it is manually interrupted.
        while True:
            # Caso o índice j esteja na última posição, adiciona o valor correspondente ao símbolo à soma.
            # If the index j is at the last position, add the corresponding value of the symbol to the sum.
            if j == len(s) - 1:
                sum = value[symbol.index(s[j])] + sum

            # Caso o índice j não esteja na última posição.
            # If the index j is not at the last position.
            if j < len(s) - 1:
                # Verifica combinações específicas de símbolos romanos que têm valores subtraídos.
                # Checks specific combinations of Roman symbols that have subtracted values.
                if s[j] == "I" and s[j + 1] == "V":
                    sum = 4 + sum
                    j = j + 2
                elif s[j] == "I" and s[j + 1] == "X":
                    sum = 9 + sum
                    j = j + 2
                elif s[j] == "X" and s[j + 1] == "L":
                    sum = 40 + sum
                    j = j + 2
                elif s[j] == "X" and s[j + 1] == "C":
                    sum = 90 + sum
                    j = j + 2
                elif s[j] == "C" and s[j + 1] == "D":
                    sum = 400 + sum
                    j = j + 2
                elif s[j] == "C" and s[j + 1] == "M":
                    sum = 900 + sum
                    j = j + 2
                # Caso contrário, adiciona o valor correspondente ao símbolo à soma.
                # Otherwise, add the corresponding value of the symbol to the sum.
                elif s[j] in symbol:
                    sum = value[symbol.index(s[j])] + sum
                    j = j + 1
            else:
                break  # Interrompe o loop quando todos os caracteres foram processados.
                # Breaks the loop when all characters have been processed.

        return sum  # Retorna a soma final.
        # Returns the final sum.


if __name__ == '__main__':
    # Teste do método com três casos diferentes.
    # Testing the method with three different cases.
    print(Solution.romanToInt('Case 1','III'))  # Exemplo 1 / Example 1: 'III' should return 3
    print(Solution.romanToInt('Case 2','LVIII'))  # Exemplo 2 / Example 2: 'LVIII' should return 58
    print(Solution.romanToInt('Case 3','MCMXCIV'))  # Exemplo 3 / Example 3: 'MCMXCIV' should return 1994