#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#
# （题倒是不难，就是代码有点逻辑性太强）
# 解法1(T89% S75%): 维护一个队列，把适量的第一个数字对应的字母一个个的入队，再一个一个出队和第二个数字对应的字母一个个的合并再入对
#   看似简单，但核心是“适量”是多少？比如“27”，总共结果应该有3*4=12个，所以首先把4个a、4个b、4个c入队，然后再出队4个a，后面依次放上pqrs再入队…；所以要维护之前所有的数量(total_before)，即应该出队多少个
# 
# 我们来看237这个🌰
#    1. 首先计算结果总数 3*3*4=36个
#    2. 循环1: 把3*4个a、3*4个b、3*4个c分别入队
#    3. 循环2: 对于total_before=3个字母(a b c)，对于我的3个字母def，分别取出并组合4份
#    4. 循环3: 对于total_before=3*3=9个组合(ad ae af bd...)，对于我的四个字母pqrs，分别取出并组合1份

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        alphas = []
        total = 1
        for digit in digits:
            letters = phone[int(digit)-1]
            alphas.append(letters)
            total *= len(letters)

        queue = []

        for i in range(len(alphas)):
            total_before = 1
            for k in range(i-1, -1, -1):
                total_before *= len(alphas[k])

            for _ in range(total_before):
                for letter in alphas[i]:
                    for _ in range(total // len(alphas[i])):
                        if i == 0:
                            queue.append(letter)
                        else:
                            queue.append(queue.pop(0)+letter)
            total //= len(alphas[i])

        return queue
# @lc code=end

