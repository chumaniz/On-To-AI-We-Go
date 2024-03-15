profile_Amy = {
    "name" : "Amy",
    "age"  : 18,
    "power1": "Reality-Manipulation", 
    "power2" : "Mind-Control",
    "weakness": "cake",
}

profile_Amy2 = {

}

profile_Jamal = {
    "name" : "Jamal",
    "age"  : 17,
    "power1": "Geoleaping",
    "power2": "Memory-Plastering",
    "weakness": "rain",
}

# This will print out the values of the dicctionaries.
# profile_Amy2 was initially empty but will now have profile_Amy's values and keys.

profile_Amy2.update(profile_Amy)

for values in profile_Jamal.values():
    print(values)

print()

for values in profile_Amy.values():
    print(values)

print()

for values in profile_Amy2.values():
    print(values)

print()