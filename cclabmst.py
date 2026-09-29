class Solution(object):
    def letterCombinations(self, digits):
        arr2 = ("a", "b", "c")
        arr3 = ("d", "e", "f")
        arr4 = ("g", "h", "i")
        arr5 = ("j", "k", "l")
        arr6 = ("m", "n", "o")
        arr7 = ("p", "q", "r", "s")
        arr8 = ("t", "u", "v")
        arr9 = ("w", "x", "y", "z")
        arr = {
            "2": arr2,
            "3": arr3,
            "4": arr4,
            "5": arr5,
            "6": arr6,
            "7": arr7,
            "8": arr8,
            "9": arr9,
        }

        if not digits:
            return []

        n = len(digits)
        if n == 1:
            return list(arr[digits[0]])
        if n == 2:
            a, b = arr[digits[0]], arr[digits[1]]
            return [x + y for x in a for y in b]
        if n == 3:
            a, b, c = arr[digits[0]], arr[digits[1]], arr[digits[2]]
            return [x + y + z for x in a for y in b for z in c]
        if n == 4:
            a, b, c, d = arr[digits[0]], arr[digits[1]], arr[digits[2]], arr[digits[3]]
            return [w + x + y + z for w in a for x in b for y in c for z in d]
        return []