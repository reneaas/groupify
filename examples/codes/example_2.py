import groupify

classlist = "sample_class.txt"

groupify.create(
    classlist=classlist,
    group_size=3,
)

groupify.savefig(dirname="../figures/", fname="example_2.svg")

groupify.show()
