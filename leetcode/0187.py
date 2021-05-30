class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        dup = set()
        sample = s[:10]
        pointer = 10
        dna_length = len(s)
        while True:
            if sample in seen:
                dup.add(sample)
            else:
                seen.add(sample)
            if pointer >= dna_length:
                break
            pointer += 1
            sample = s[pointer - 10: pointer]
        return dup
