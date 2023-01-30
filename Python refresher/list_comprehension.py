numbers = [1,2,3,4,5,6,7,8,10,12,16,17,23]

doubled = []

## complicated method
for num in numbers:
    doubled.append(2*num)

## with list comprehension
doubled_comprehend = [2*x for x in numbers]
print(numbers, '\n', doubled, '\n', doubled_comprehend)

friends = ["Rolf", "Sam", "Sebastian", "Benjamin", "Peter", "Santiago", "Jesus", "Judas"]

## tedious way
starts_s = []
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

## with list comprehension
starts_s_comprehend = [friend for friend in friends if friend.startswith('S')]
print(starts_s, '\n', starts_s_comprehend)

#starts_s = [name for name in ]