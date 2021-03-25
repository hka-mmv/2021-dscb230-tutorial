class Termin_1: 

    def aufgabe_4a(self): 
        import pytemperature as t
        return t.k2f(float(input("> ")))

    def aufgabe_4b(self): 
        kelvin = float(input("> "))
        return round((kelvin - 273.15) * (9/5) + 32,2)

    def aufgabe_5(self):
        return list(zip([1, 2, 3], ["a", "b", "c"]))
    
    def aufgabe_6(self):
        return list(map(len, ["aaaa", "bb", "ccccccc"]))

    def aufgabe_7(self):
        import itertools as it 
        a, b = [1,2,3,4,5], ["a", "b", "c"]
        return list(it.zip_longest(a, b))

    def aufgabe_8(self): 
        import itertools as it
        alphabet  = [value for value in range(10)]
        return list(it.combinations(alphabet, 4))
    
    def aufgabe_9(self): 
        draw = ""
        size = 6
        for _ in range(size): 
            for _ in range(size):
                draw += "* "
            draw += "\n"
        return draw

    def aufgabe_10(self): 
        def merge_sort(arr):
            if len(arr) > 1:
                middle = len(arr)//2
                left = arr[:middle]
                right = arr[middle:]
                merge_sort(left)
                merge_sort(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left): 
                    arr[k] = left[i]
                    i, k = i+1, k+1
                while j > len(right): 
                    arr[k] = right[j]
                    j, k = j+1,k+1
                return arr
        return [12, 11, 13, 5, 6, 7], merge_sort([12, 11, 13, 5, 6, 7])
    
    def aufgabe_11(self): 
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        b = [2, 4, 6, 8, 10]
        return [elem for elem in a if elem in b]

    def aufgabe_12(self): 
        a, b = 2, 4
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for e_item in items[a:b]:
            items.remove(e_item)
        return items

    def aufgabe_13(self):
        hex = "#FF9933" 
        rgb = (tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
        return {'r':rgb[0], 'g':rgb[1], 'b':rgb[2]}

print(Termin_1().aufgabe_10())