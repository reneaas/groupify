import groupify

classlist = "sample_class.txt"

groupify.create(
    classlist=classlist,
    group_size=4,
)

groupify.savefig(dirname="../figures/", fname="example_1.svg")

groupify.show()
