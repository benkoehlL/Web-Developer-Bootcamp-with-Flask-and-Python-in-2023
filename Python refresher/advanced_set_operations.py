friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local = {"Rolf"}

local_friends = friends.difference(abroad)
print(local_friends)

total_friends = local.union(abroad)
if(total_friends == friends):
    print("Total friends is the union of abroad and local friends!")

art_friends = {"Pascal", "Sophia", "Claude", "Richard", "Lev"}
science_friends = {"Albert", "Marie", "Richard", "Lev"}

art_and_science_friends = art_friends.intersection(science_friends)
faithful_art_friends = art_friends.difference(science_friends)
faithful_science_friends = science_friends.difference(art_friends)
print(art_and_science_friends, " are friends of both science and arts")
print(faithful_art_friends, " are friends of arts but not science")
print(faithful_science_friends, " are friends of science but not arts")
