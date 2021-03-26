class Termin_2: 

    def aufgabe_1(self): 
        a = [3, 1, 4, 2, 5]
        for i in range(1, len(a)): 
            key = a[i] 
            j = i-1
            while j >=0 and key < a[j]: 
                a[j+1] = a[j] 
                j -= 1
            a[j+1] = key
        return a

    def aufgabe_2(self): 
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        b = [2, 4, 6, 8, 10]
        return [elem for elem in a if elem in b]
        
    def aufgabe_3(self): 
        a, b = 2, 4
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for item in items[a:b]:
            items.remove(item)
        return items

    def aufgabe_4(self):
        n = 5
        top = '-' * (2*n+3)
        middle = f"|{ '-'*n }+{ '-'*n }|"
        glasses = [f"|{ '.'*n }|{ '.'*n }|"] * n
        return '\n'.join([top, *glasses, middle, *glasses, top])

    def aufgabe_5(self): 
        n = 3
        return n + (5 - n) % 5

    def aufgabe_6(self): 
        result = []
        n = [89, 695]
        p = [1, 2]
        for n,p in zip(n, p):
            m = 0
            for i,c in enumerate(str(n)):
                m += pow(int(c),p+i)
            result.append((n, m/n, m))
        return result
    
    def aufgabe_7(self):
        n = [1,2,3,4,5,6,7]
        v = 0
        for i in n: 
            v = (v + 3) % i
        return v + 1
        
    def aufgabe_8(self):
        hex = "#FF9933" 
        rgb = (tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
        return {'r':rgb[0], 'g':rgb[1], 'b':rgb[2]}

print(Termin_2().aufgabe_6())