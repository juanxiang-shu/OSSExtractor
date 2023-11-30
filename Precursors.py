import re
from Compounds import find_words

def extract_precursors(paragraph):
    precursors = set()
    sentences = paragraph.split(".")
    molecule_pattern = r'\b(molecule\s+\d|precursor\s+\d|monomer\s+\d)\b'
    Scheme_pattern = r'\b(Scheme 1|(Scheme 1)|Figure 1|(Figure 1)|As the first step|Figure 1 a|Fig)\b'
    reactant_pattern = r'\b(molecular precursors|molecular precursor|SCOF-1|SCOF-2)\b'
    prefix_pattern = re.compile(r'^(oligo|dimers|trimers|diimine|tetramer|trimeric|COF|cyano-groups|para-alkyny'
                                r'|2D-polyester|acylchlorides|tert-butyl|dialdehyde'
                                r'|dimethyl|polymers|polymeric|imidazole|1-azadibenzo(.)d,k(.)ullazine|dibenzoazaullazine'
                                r'|NGs|halides|alkenes|polymer chains|polymer chain|nitrogen|covalent networks|polyphenylene'
                                r'|polyalkyne|biphenylsilanes|phenylsilane|diaryldisilanediyl|ethers|graphene nanoribbon|SCOFs'
                                r'|COFs|1,2-diphenylethyne|molecular chains|molecular chain|polymeric network|trisalicylaldehyde)')

    for sentence in sentences:
        sentence = sentence.strip()
        if re.search(molecule_pattern, sentence, re.IGNORECASE):
            result = find_words(sentence)
            precursors |= set(result["Compounds"])
        if re.search(Scheme_pattern, sentence, re.IGNORECASE):
            result = find_words(sentence)
            precursors |= set(result["Compounds"])
        if re.search(reactant_pattern, sentence, re.IGNORECASE):
            result = find_words(sentence)
            precursors |= set(result["Compounds"])
    compounds_to_remove = [compound for compound in precursors if re.match(prefix_pattern, compound)]

    for compound in compounds_to_remove:
        precursors.remove(compound)

    return precursors