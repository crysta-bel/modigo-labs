def compare_hobbies(person1_hobbies, person2_hobbies):
    # TODO: use set operations to find shared, only_person1, and only_person2 hobbies
    shared = person1_hobbies.intersection(person2_hobbies)
    only_person_one = person1_hobbies.difference(person2_hobbies)
    only_person_two = person2_hobbies.difference(person1_hobbies)

    return {"shared": shared, "only_person1": only_person_one,
    "only_person2": only_person_two}

print(compare_hobbies({"reading", "coding"}, {"coding", "gaming"}))