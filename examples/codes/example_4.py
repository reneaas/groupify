import groupify

classlist = "sample_class.txt"

groupify.create(
    classlist=classlist,
    group_size=2,
)

groupify.savefig(dirname="../figures/", fname="example_4.svg")

groupify.show()
