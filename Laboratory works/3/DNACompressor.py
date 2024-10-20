
'''
Словарь бинарных кодов по коду ДНК.
'''
DNA_BINARY_CODES: dict[str, bin] = {
    'a': 0b00,
    'c': 0b01,
    'g': 0b10,
    't': 0b11,
}

'''
Коды ДНК по бинарным кодам.
'''
DNA_CODES: dict[bin, str] = {
    0b00: 'a',
    0b01: 'c',
    0b10: 'g',
    0b11: 't',
}

'''
Класс сжатия и распаковки ДНК.
'''
class DNACompressor:
    '''
    Сжатая последовательность ДНК.
    '''
    __compressed_dna_sequence: bin

    '''
    Длина исходной последовательности.
    '''
    __original_length: int

    '''
    Инициализирует ДНК.
    '''
    def __init__(self, dna_sequence: str) -> None:
        self.__compressed_dna_sequence = self._compress(dna_sequence)
        self.__original_length = len(dna_sequence)

    '''
    Возвращает сжатую ДНК в виде строки.
    '''
    def __str__(self) -> str:
        return str(self.__compressed_dna_sequence)

    '''
    Выполняет сжатие ДНК.
    '''
    def _compress(self, dna_sequence: str) -> bin:
        compressed = 0
        for nucleotide in dna_sequence:
            compressed <<= 2
            compressed |= DNA_BINARY_CODES[nucleotide]
        return compressed

    '''
    Выполняет распаковку ДНК.
    '''
    def _decompress(self) -> str:
        dna_sequence = []
        compressed = self.__compressed_dna_sequence
        for _ in range(self.__original_length):
            nucleotide_bits = compressed & 0b11
            dna_sequence.append(DNA_CODES[nucleotide_bits])
            compressed >>= 2
        return ''.join(dna_sequence[::-1])

    '''
    Возвращает сжатую последовательность ДНК.
    '''
    def get_compressed_dna_sequence(self) -> str:
        return self.__str__()

    '''
    Возвращает сжатую последовательность ДНК.
    '''
    def get_decompressed_dna_sequence(self) -> str:
        return self._decompress()
