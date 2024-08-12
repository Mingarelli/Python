#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]

#Example 3:

#Input: nums = [3,3], target = 6
#Output: [0,1]

class Solution:
    # Método que encontra dois números em uma lista que somam um valor alvo
    # Method that finds two numbers in a list that sum to a target value
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Inicializa uma lista vazia para armazenar os índices dos números que somam o alvo
        # Initializes an empty list to store the indices of the numbers that sum to the target
        output = []

        # Verifica se a lista tem pelo menos dois elementos
        # Checks if the list has at least two elements
        if (len(nums) >= 2):
            # Percorre a lista a partir do primeiro elemento
            # Iterates through the list starting from the first element
            for j in range(0, len(nums), 1):
                # Percorre a lista a partir do elemento seguinte a j
                # Iterates through the list starting from the element after j
                for i in range(j + 1, len(nums), 1):
                    # Verifica se a soma dos elementos em j e i é igual ao alvo
                    # Checks if the sum of the elements at j and i equals the target
                    if (nums[j] + nums[i] == target):
                        # Adiciona os índices de j e i à lista de saída
                        # Adds the indices of j and i to the output list
                        output.append(j)
                        output.append(i)
            # Retorna a lista de índices que somam o alvo
            # Returns the list of indices that sum to the target
            return output


# Testa o método twoSum com diferentes exemplos
# Tests the twoSum method with different examples
if __name__ == '__main__':
    # Deve retornar [0, 1], pois nums[0] + nums[1] = 2 + 7 = 9
    # Should return [0, 1] because nums[0] + nums[1] = 2 + 7 = 9
    print(Solution.twoSum('Exemplo1', [2, 7, 11, 15], 9))

    # Deve retornar [1, 2], pois nums[1] + nums[2] = 2 + 4 = 6
    # Should return [1, 2] because nums[1] + nums[2] = 2 + 4 = 6
    print(Solution.twoSum('Exemplo2', [3, 2, 4], 6))

    # Deve retornar [0, 1], pois nums[0] + nums[1] = 3 + 3 = 6
    # Should return [0, 1] because nums[0] + nums[1] = 3 + 3 = 6
    print(Solution.twoSum('Exemplo3', [3, 3], 6))




