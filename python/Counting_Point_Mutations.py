def hit_count(str1, str2):
    counter = 0
    str1.split()
    str2.split()
    for i in range (len(str1)):
        for j in range (len(str2)):
            if str1[i]==str2[j] and i==j:
                counter=counter+1
    return counter
str1 = "GCGTCTATAGCACAGGTCGGCCTAAATGTTTGCATCTACCCTGAAGCTAGGAACTATGGGCTCGGTCGGCAGTTGTGTTCGCCTTCTCTCATGAAGCCAATAGCGACGAGAGAGCCCCCTGCACACCCAAACGTCGCCGATCCGTATGCCGCCCCGCGATGTTAGACTAGAAAGACCGGTAGGCTTAAAAGCCGAATCCCCTCACGTTCAGTTCGCACAGTCCCACTCTGGCCCACAATCCTAGCCTACGACAATGACAGAAAGCCATTTCAAGTGCTCCTGTTTAAGCCACCTACCTTGAAGACACTGCTCGCAAGGTAGTTTCGTTGTCACCGTCAGCGCAAGGTCGAACAAATAATTTGCTCTAAACCCTCTGCTCTCTCTTTACGGCGCACGCCAACGCTAGATTCCATAAGGCGAGCTCTCGTCACCCCTCGGGCCAAAAAGATTGGTCCCGAGCTATCAGCTCGAATGGCGATAACAGAGGTAGCGTAGGGTCGTTACCTTCTTTAGACGGTTATATTACACATCGAGCAAGAGGTTGGAATCCCGTAAGTGAGCCAGCTTGGGTAAGGATGTGAGCAACATGTCCGCACGGGATAGGGTGCGAGCTTAACGAGGAGCGTAGGAAAGCGGAGGCGTGTTTCATTTTAAAAAAGCGTTTGAGCTACTCCGGCAGATAAGGTCAACGGCTGCGTGCTTTTGCCGACACAGCATTAATAAACTTGTAGACGCTGCGTTGATTAGGTACCCGCTTTGGTGGTGCAGTAGGAACTACTTTTCATAGACGCCGTGTACGAGGCCGTTAATCCGGTACGCCCCCGCATTCCACATTCTTGATCAAACGAGGGCTAAGAGTTCCTAAGCTGTTTCGTTGCGGGGCGTTGTTCGTACCGAGAACAGTCAGTGGAACCTTGTATCTACTGCAAAG"
str2 = "TCTCCTAGAATACGAGCCCGTCTATTCGTGGTGGTATGCCATGGGCCTCGGCAGCATAACCCCGGTGAAACTCCTTAACCGGATTTTCTCAAGACCGTAACAAGCAGGGGCAACCCCTAAGCCCAGGGGTACATTGCATGACGCAGGGTGGCCTTTTAAATGGGCATTAGAGTGACCGCCTCGCATCATGGCGGAGGTGCCAAAGGTTCGGGCCAAACAGTGCACACCTCGGCTGCCATCGTAGGGAGGCAGAGTGTGGATCTGTCCTTAGAAACGTTGGTGTCAATGAGATCTAACTTGAATACACATCTTGTAAGTCCGGCACGGTGGGCGACTCAACGCAAGTCCCAACACAGTAGCGTCCCTTATCGTTTTGCATTGAACGTAAGGCTTATGCTGTCGTACGAGTTCCCATGCCGAGCTATTATATCCTCCCTGCAGAATAAGATTTCGTCCTAGCAAGCCGTTGGTGAGCAGGTTCCAGCCGGATAGAGCGCTTGTAAACTGCCTTAGCCCATACAGGACGTGAGTAATAGCCAGCATTGCTTAGATCGACTGAGCCACCCTGGGAACCGCATTGCGTAAAATAGACGAATGTGATATAGGGCCTGGTGGACTAGTGCCTCGATAACAAGTTCATTTTTAAAATATTAAACAGGTACATGCTCGTCAGCGACAGCTAATGTCCACGAACGCAATCCTCTCACCAGACTGGCTTTACATAAATACCTAGATTGCGATAATTGGGTACCCTCCTTGGTTGTGCAGCACTCCGCAAATGTCCTAAGCGCCACGTACATAACCGTTACTGCGACGACTTCCGTGATTGCAAGATGTTGATGTAAAGATCCTAGGTGTATGACCCTCTGTTTAGTAGCTGTCCTTTGTTTCCCCTGAGGCAATTACGGGGGACTTTATATCTGCGTCATAG"
lenght_of_strings = len(str1)
hamming_distance = lenght_of_strings-hit_count(str1, str2)
print(hamming_distance)