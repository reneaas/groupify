import groupify

classlist = "sample_class.txt"

absent = ["Einstein", "Cantor", "Hilbert"]

groupify.create(
    classlist=classlist,
    group_size=4,
    absent=absent,  # Removes them from the list before creating the groups
)

groupify.savefig(dirname="../figures/", fname="example_2.svg")

groupify.show()
