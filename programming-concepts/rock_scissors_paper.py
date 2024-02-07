while True:
    inputs = input("Enter signs separated with space(s, r, p): ").split(' ')  # r r -> [r, r]
    print(inputs)
    inputs = set(inputs)
    print(inputs)
    signs_list = list(inputs)
    if len(inputs) == 3 or len(inputs) == 1:
        print("Draw")
    elif signs_list[0] == "s":
        if signs_list[1] == "p":
            print("S won this game")
        else:
            print("R won this game")
    elif signs_list[0] == "p":
        if signs_list[1] == "r":
            print("P won this game")
        else:
            print("S won this game")
    elif signs_list[0] == "r":
        if signs_list[1] == "s":
            print("R won this game")
        else:
            print("P won this game")