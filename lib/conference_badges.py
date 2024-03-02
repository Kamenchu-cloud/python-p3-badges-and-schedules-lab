def badge_maker(name):

    # if name is not None:
    #     badge = f"Hello, my name is {name}."
    #     return badge
    # else:
    #     return None
    
    return f"Hello, my name is {name}." if name is not None else None
    
def batch_badge_creator(names):

    # badges = []
    # for name in names:
    #     badges.append(f"Hello, my name is {name}.")
    # return badges

    badges = [f"Hello, my name is {name}." for name in names]
    return badges

def assign_rooms(names):

    # room_assignment = []
    # for room_number, name in enumerate(names, start=1):
    #     message = f"Hello, {name}! You'll be assigned to room {room_number}!"
    #     room_assignment.append(message)
    
    # return room_assignment

    return [f"Hello, {name}! You'll be assigned to room {room_number}!" for room_number, name in enumerate(names, start=1)]

def printer(names):
    # Generate badge messages
    badges = batch_badge_creator(names)
    
    # Generate room assignment messages
    room_assignments = assign_rooms(names)

    # Print badge messages
    for badge in badges:
        print(badge)

    # Print room assignment messages
    for assignment in room_assignments:
        print(assignment)
