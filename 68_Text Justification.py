class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        while len(words) > 0:
            length, count, cur_start, next_start = 0, 0, 0, 0
            idx = 1
            line = "" + words[cur_start]

            for i in range(len(words)):
                next_start = i
                if length + len(words[i]) <= maxWidth - count:
                    length += len(words[i])
                    count += 1
                else:
                    break

            if count == len(words):  # last line
                while idx <= count - 1:
                    line += (' ' + words[cur_start+idx])
                    idx += 1
                if length + count - 1 < maxWidth:
                    line += (' ' * (maxWidth - length - count + 1))
                res.append(line)
                break
            else:
                space_num = maxWidth - length
                if count == 1:
                    sepa_num = space_num
                    sepa = ' ' * sepa_num
                    line += sepa
                else:
                    sepa_num = space_num // (count - 1)

                    while space_num > 0:  # 左边空格多于右边
                        if space_num - sepa_num >= 0 and space_num - sepa_num * (count-idx) == 0:
                            sepa = ' ' * sepa_num
                            line += sepa
                            space_num -= sepa_num
                        elif space_num - sepa_num >= 0 and space_num - sepa_num * (count-idx) != 0:
                            sepa = ' ' * (sepa_num+1)
                            line += sepa
                            space_num -= (sepa_num+1)
                        else:
                            line += (' ' * space_num)
                        line += words[cur_start+idx]
                        idx += 1  # 已经在该行中的词的个数

                res.append(line)
                words = words[next_start:]

        return res

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

a = Solution()
res = a.fullJustify(words, maxWidth)
print(res)
