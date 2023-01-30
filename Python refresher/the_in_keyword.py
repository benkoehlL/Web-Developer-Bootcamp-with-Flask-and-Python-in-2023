friends = ["Benjamin", "Peter", "Richard", "Uwe"]
print("Peter" in friends)
print("Jen" in friends)

movies_watched = {"good will hunting", "her", "stalker", "oppenheimer"}
user_movie = input("Enter a movie you watched: ").lower()
if(user_movie in movies_watched):
    print("Wow, I have seen {} too!".format(user_movie))
else:
    print("Oh, I am sorry, I have not watched {}.".format(user_movie))