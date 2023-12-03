reaction_words = {
    "Coupling Reactions": {
        "Ullmann coupling": ["Ullmann", "Ullmann Coupling", "CHPR coupling", "C–C coupling" ],
        "Glaser coupling": ["Glaser coupling", "Glaser–Hay type coupling"],
        "Sonogashira coupling": ["Sonogashira coupling", "Sonogashira"],
        "Other C-C Homo-coupling": ["C-C Homo-coupling", "C-C Homo coupling", "C-C HomoCoupling",
                              "C-C HomoCouplings",
                              "Wurtz reaction", "Wurtz reactions", "carbon–carbon coupling",
                              "Dehalogenative homocoupling", "Dehalogenative homocouplings",
                              "Dehydrogenative homocoupling", "Dehydrogenative homocouplings",
                              ],
        "Other C-C Cross-coupling": ["C-C cross-coupling reaction", "C-C cross coupling reaction", "cross-coupling reaction", "cross-coupling reactions"
                                     "C–C bond coupling", "C–C coupling reaction"],
    },
    "Cyclization Reactions": {
        "Bergman cyclization": ["Bergman cyclization", "Bergman", "Enediyne Cyclization", "C1−C6 cyclization"],
        "Intramolecular Diels-Alder": ["Intramolecular Diels-Alder"],
        "Cyclotrimerization": ["Cyclotrimerization", "Polycyclotrimerization"],
        "Cyclodehydrofluorization":["cyclodehydrofluorization"],
        "Cyclodehydrogenation": ["Cyclodehydrogenation reaction", "intramolecular Cyclodehydrogenation", "Cyclodehydrogenation"],
        "Other cycloaddition": ["cycloaddition reactions", "cycloaddition reaction", "Radical Cyclization",
                                "C1−C5 cyclization", "hydroalkoxylation reaction"],
    },
    "Miscellaneous Reactions": {
        "Imine formation": ["Imine bond formation", "Imine", "Imine formation", "Imine-linked", "imine bonds", "imine interlinkages"],
        "Click reaction": ["Click reaction", "Click reactions"],
        "Dehydration of boronic acids": ["Dehydration of boronic acids"],
        "Ether formation": ["Formation of ethers", ],
        "Desulfonylation": ["Desulfonylation", "Desulfonylation Homocoupling"],
        "Skeletal rearrangements of polycyclic conjugated hydrocarbons": [
            "skeletal rearrangements",
            "ring-rearrangement reaction", "ring-rearrangement reactions",
            "ring rearrangement reactions", "ring rearrangement reaction",
            "rearrangement reactions", "rearrangement reaction"],
        "Decomposition reaction": ["Dealkylation reaction"],
        "Condensation of alcohol and acylchloride": ["condensation of alcohols and acylchlorides", "condensation of polyesters", "polyester condensation"],
        "Metathesis reaction": ["Metathesis reaction"],
        "Urea formation": ["urea linkage", "urea linkages"],
        "Heck reaction": ["Heck reaction"],
        "Si-Si bond formation": ["Si–Si bond formation"]
    }
}

element_definitions = {
    "H", "He", "Li",  "Be",  "B",  "C", "N", "O",  "F",  "Ne", "Na", "Mg",  "Al", "Si", "P",  "S", "Cl", "Ar", "K",
    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Ni", "Co", "Cu", "Zn",  "Ga", "Ge", "As", "Se", "Br",  "Kr", "Rb",
    "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "I", "Te", "Xe", "Cs", "Ba",
    "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re",
    "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb",  "Bi", "Th", "Pa", "U"
}

temperature_words = {"K", "°C"}

compounds_words = {
    "Bromo", "Chloro", "Fluoro", "Anisole", "Tetrahydrofuran", "oxane", "Acetal", "bromobenzene",
    "Methyl", "Ethyl", "Propyl", "Butyl", "Pentyl", "Hexyl", "Heptyl", "Octyl", "Nonyl", "Decyl",
    "Allyl", "Phenyl", "Benzo", "Amino", "Hydroxy", "Carboxy", "Keto", "Aldehyde", "Nitro", "Amide",
    "Sulfur", "Thiol", "Sulfonyl", "Iodo", "Cyano", "Methoxy", "Ethoxy", "Acetyl", "Oxo", "Phospho", "Hydroxyl",
    "Acyloxy", "Vinyl", "Aryl", "Naphthyl", "Furan", "Pyridine", "Thiophene", "azole", "Toluene", "Xylene",
    "Styrene", "Aniline", "Pyrrole", "pyran", "benzene", "Boron", "Sulfuric acid", "Boronic acid", "Boronic",
    "pyrene", "halogen", "methylene", "ethynylphenanthrene", "indenylidene", "Acetic acid",
    "Alkane", "Alkene", "Alkyne", "Ketone", "Carboxylic", "Ester", "Amine", "Ether", "biphenyl",
    "Nitrile", "Halide", "Thiol", "Sulfide",  "Nitro", "Azide", "Isocyanate", "Isothiocyanate", "Thioester",
    "Sulfonic", "chloride", "anhydride", "Imine", "Aziridine", "anthracene", "hydroxymethyl",
    "Pyrimidine", "Purine", "Lactone", "acetone", "Nitrone", "Isonitrile",  "Isoquinoline", "Porphyrin",
    "nanographenes", "tribromomethyl", "bromomethyl", "alkynes", "hydroxyoxirane", "polymer", "polymeric", "oligomer"
    "dimer", "trimer", "tetramer", "diimin", "fullerene"
    #"Hydro",  "Ether", "oxide",
}

compounds1_words = {"MTBE", "ETBE", "THF", "DME", "DMF", "DMA", "DEA", "TEA", "TMA",
                    "DBE", "DBP", "DCE", "DCM", "THB", "PEG", "PPG", "PBT", "PET", "PVP", "PVDF",
                    "PVC", "CHP", "BPDSC", "NGs", "COF-420", "COF", "COFs", "SCOFs"}

compounds2_words = {"Together", "Whether", "tethers"
                    }

compounds3_words = {"Boronic acid", "dimethyl alcohol", "Carboxylic acid", "Sulfonic acid", "Phosphonic acid", "Silicic acid"
                    "Hydrofluoric acid", "Nitric acid", "Hydrochloric acid", "Acetic acid", "Propionic acid", "fluoric acid",
                    "Nitric acid", "Hydrochloric acid", "Acetic anhydride", "Methyl acetate", "boxylic acid", "planar dendrimers",
                    "alkynyl bromide group", "polymeric chain", "dialdehyde molecule", "covalent network", "polymer chain",
                    "oligophenylene chain", "molecule network", "phenylene diisocyanate",
                    "disulfonyl dichloride", "graphene nanoribbon", "bromine group", "py group", "molecular chain", "supramolecular chain",
                    "polyaromatic chain", "bromophenyl porphyrin", "polymeric network", "aromatic trisalicylalde"
                    }

Product_form = {
    "1D": ["chains", "chain", "wires", "one-dimensional", "one dimensional", "1D",],
    "2D": ["networks", "rings", "ring", "network", "two-dimensional", "two dimensional", "2D"]
}