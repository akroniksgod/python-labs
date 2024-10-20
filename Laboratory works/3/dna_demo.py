import random
import string
import sys
from DNACompressor import DNACompressor

'''
Исходная строка ДНК из 1000 нуклеотидов.
'''
DEFAULT_DNA: str = f'ataagactccccctcaagcgttcgtggggatgctctgtttactgggcagttatcctagca\
cccggggcccgaacgaagttcaacgctagctaccttccactgatgtgaaaaggatgagat\
aatccctgtcagacgcattaagtgaatgtgtgaatgacgccactacacgctggcaagcgc\
gggcgatcgcaggttcttcttgtgaggcgactacaggctcgccattcgtcgtttcttcaa\
tggttagcctatcagaaacacggctccaatacttctgacgtctcgacgggccagcggtca\
gcaccgctgtcgatattaatcgcagctgggaactaacagaaacctaaagaaaaattcgtc\
cggttctgattatataccgggagtataatcactctcacagcccgagtacatacacgcacg\
actttacaacaagcagagctcagtctgggcctcgccatttcccgttttaagcgcgggtga\
aactgggtttaaggggcggtgtacggacaattaatcgcatttttcgataggtcatgatcg\
tcaagttttgagatctcaaacctttagtaataatgttcgcctagaatctgggggctattg\
gagaacgaaccttccatcggtcgcgataccgcataccaagccgcttatctttaaagtgca\
aatctgggaatccccatgccctaagaggtcattaagagaacctatgtttagcagctactc\
tcgtagaatgcacgtttaagggacgccgtcaccacggattccggtgcatatagttgcata\
gctagatccggtctctctctatgggataaagcgtcacaagtcgcgttcatctttctacat\
tgtaacgccattcaatcaaagtgatcgggatctgctctgctcatgatacacgctgagata\
gattcggcataaggaacggcttgctcgaatcggtaatccccgaggatcatgtcgatttgc\
atcaacagtgacgcggcaggtaccatgacaaccaaatggc'


'''
Гененрирует последовательность ДНК из нуклеотидов a, c, g, t.
'''
def generate_dna_sequence(dna_length: int = 1000):
    return DEFAULT_DNA \
        if dna_length == 1000 \
        else ''.join(random.choices('acgt', k=dna_length))


'''
Проводит тест на сгенерированной последовательности ДНК по переданной длине ДНК.
'''
def run_test_dna_sequence_of_length(dna_length: int = 1000) -> None:
    print(f'Длина последовательности: {dna_length}')

    dna_sequence: str = generate_dna_sequence(dna_length)
    compressed_dna_str = DNACompressor(dna_sequence)
    print(f'Исходная строка: {sys.getsizeof(dna_sequence)} байтов')
    print(f'Сжатая строка: {sys.getsizeof(compressed_dna_str.get_compressed_dna_sequence())} байтов')

    is_sequence_same: bool = dna_sequence == compressed_dna_str.get_decompressed_dna_sequence()
    print(f'Совпало ли после распаковки? {'Да!' if is_sequence_same else 'Нет!'}')
    print()


if __name__ == '__main__':
    sys.set_int_max_str_digits(999999999)
    run_test_dna_sequence_of_length()
    run_test_dna_sequence_of_length(10_000)
    run_test_dna_sequence_of_length(100_000)
    run_test_dna_sequence_of_length(1_000_000)
    run_test_dna_sequence_of_length(10_000_000)
