# Seven different symbols represent Roman numerals with the following values:
#Symbol	Value
#I	1
#V	5
#X	10
#L	50
#C	100
#D	500
#M	1000
#Roman numerals are formed by appending the conversions of decimal place values from highest to
#lowest. Converting a decimal place value into a Roman numeral has the following rules:
#If the value does not start with 4 or 9, select the symbol of the maximal value that can be
#subtracted from the input, append that symbol to the result, subtract its value, and convert the
#remainder to a Roman numeral.
#If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted
#from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1(I) less than
#10(X): IX.Only the following subtractive forms are used: 4(IV), 9(IX), 40(XL), 90(XC),
#400(CD) and 900(CM).
#Only powers of 10(I, X, C, M) can be appended consecutively at most 3 times to represent
#multiples of 10. You cannot append 5(V), 50(L), or 500(D) multiple times.If you need to
#append a symbol 4 times use the subtractive form.
#Given an integer, convert it to a Roman numeral.

#Example 1:
#Input: num = 3749
#Output: "MMMDCCXLIX"
#Explanation:
#3000 = MMM as 1000(M) + 1000(M) + 1000(M)
#700 = DCC as 500(D) + 100(C) + 100(C)
#40 = XL as 10(X) less of 50(L)
#9 = IX as 1(I) less of 10(X)
#Note: 49 is not 1(I) less of 50(L) because the conversion is based on
#decimal places

#Example 2:
#Input: num = 58
#Output: "LVIII"
#Explanation:
#50 = L
#8 = VIII

#Example 3:
#Input: num = 1994
#Output: "MCMXCIV"
#Explanation:
#1000 = M
#900 = CM
#90 = XC
#4 = IV

#Constraints:
#1 <= num <= 3999

class Solution:
    def intToRoman(self, num: int) -> str:
        # Define uma lista de valores inteiros correspondentes aos símbolos dos numerais romanos
        # Define a list of integer values corresponding to Roman numeral symbols
        value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        # Define uma lista de símbolos romanos que correspondem aos valores inteiros acima
        # Define a list of Roman numeral symbols that match the integer values above
        symbol = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        # Inicializa uma string vazia para armazenar o numeral romano resultante
        # Initialize an empty string to store the resulting Roman numeral
        roman = ''

        while True:
            # O loop continua enquanto o número for maior que 0
            # The loop continues as long as the number is greater than 0
            if num > 0:
                # Itera sobre cada valor na lista
                # Iterate over each value in the list
                for j in value:
                    # Verifica se o número atual é maior ou igual ao valor j
                    # Check if the current number is greater than or equal to the value j
                    if num >= j:
                        # Caso especial para o maior valor (1000)
                        # Special case for the largest value (1000)
                        if j == 1000:
                            # Subtrai o valor do número e adiciona o símbolo correspondente ao resultado
                            # Subtract the value from the number and add the corresponding symbol to the result
                            num = num - value[value.index(j)]
                            roman = roman + symbol[value.index(j)]
                    else:
                        # Subtrai o valor anterior do número e adiciona o símbolo correspondente ao resultado
                        # Subtract the previous value from the number and add the corresponding symbol to the result
                        num = num - value[value.index(j) - 1]
                        roman = roman + symbol[value.index(j) - 1]
                        break
            else:
                break
        # Retorna o numeral romano resultante
        # Return the resulting Roman numeral
        return roman

# Casos de teste para validar a solução
# Test cases to validate the solution
if __name__ == '__main__':
    print(Solution.intToRoman('Case 1', 3749))  # Saída esperada: "MMMDCCXLIX"
                                                # Expected output: "MMMDCCXLIX"
    print(Solution.intToRoman('Case 2', 58))    # Saída esperada: "LVIII"
                                                # Expected output: "LVIII"
    print(Solution.intToRoman('Case 3', 1994))  # Saída esperada: "MCMXCIV"
                                                # Expected output: "MCMXCIV"