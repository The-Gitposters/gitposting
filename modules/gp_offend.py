# offend module

# for random numbers
import random
# adjectives
adj = [
    "dekadente",
    "arrogante",
    "ekelerregende",
    "großspurige",
    "ignorante",
    "maliziöse",
    "selbstgefällige",
    "selbstgerechte",
    "verlogene",
    "bekloppte",
    "verkackte",
    "gammelige",
    "verfickte",
    "hirnverrottete"
]

# gendering dictionary
genders = {
    "f":"",
    "m":"r",
    "n":"s"
}

# nouns prefixes
prefix = [
    "Sack",
    "Kack",
    "Wichs",
    "Scheiß",
    "Mist"
]

# nouns suffixes ()"noun":"gender" for gendering adjectives)
suffix = {
    "lappen": "m",
    "ratte":"f",
    "fotze":"f",
    "bratze":"f",
    "nagel":"m",
    "pfanne":"f",
    "sack":"m",
    "stöpsel":"m",
    "granate":"f",
    "birne":"f",
    "brett":"n",
    "tonne":"f"
}

# returns a randomly generated offense like <adjective> <prefi><suffix>
def be_mean():
    # generate list indices
    index_adj = random.randrange(len(adj))
    index_pre = random.randrange(len(prefix))
    index_suf = random.randrange(len(suffix))
    
    # concatenate parts with gendered adjective
    offense = adj[index_adj] + genders[suffix[list(suffix)[index_suf]]] + " " + prefix[index_pre] + list(suffix)[index_suf]

    return offense