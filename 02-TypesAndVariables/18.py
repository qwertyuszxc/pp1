side_a = int(input('Write down A-side size '))
side_b = int(input('Write down B-side size '))
side_c = int(input('Write down C-side size '))
half_p = (side_a + side_b + side_c)/2
print(((half_p* (half_p - side_a) * (half_p - side_b) * (half_p - side_c)))**0.5)