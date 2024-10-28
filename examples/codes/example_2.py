import groupify

classlist = "sample_class.txt"

absent = [
    "Einstein",  # Busy dreaming about light
    "Feynman",  # Busy pick-locking government secrets
    "Hilbert",  # Busy trying to one-up Einstein on GR
    "Schrödinger",  # Uncertain if he's here or not – we'll exlude him to be sure
]

groupify.create(
    classlist=classlist,
    group_size=4,
    absent=absent,  # Removes them from the list before creating the groups
)

groupify.savefig(dirname="../figures/", fname="example_2.svg")

groupify.show()
