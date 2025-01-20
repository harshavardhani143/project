def remove_match_char(list1, list2):
 
    for i in range(len(list1)):
        for j in range(len(list2)):
 
           
            if list1[i] == list2[j]:
                c = list1[i]
 
                list1.remove(c)
                list2.remove(c)
 

                list3 = list1 + ["*"] + list2
 

                return [list3, True]
 

    list3 = list1 + ["*"] + list2
    return [list3, False]
 
 
if _name_ == "_main_":
 
    p1 = input("Player 1 name : ")
 
    p1 = p1.lower()
 
    p1.replace(" ", "")
 
    p1_list = list(p1)
 
    p2 = input("Player 2 name : ")
    p2 = p2.lower()
    p2.replace(" ", "")
    p2_list = list(p2)
 
    # taking a flag as True initially
    proceed = True
 
    # keep calling remove_match_char function
    # until common characters is found or
    # keep looping until proceed flag is True
    while proceed:
 
        # function calling and store return value
        ret_list = remove_match_char(p1_list, p2_list)
 
        # take out concatenated list from return list
        con_list = ret_list[0]
 
        # take out flag value from return list
        proceed = ret_list[1]
 
        # find the index of "*" / border mark
        star_index = con_list.index("*")
 
        # list slicing perform
 
        p1_list = con_list[: star_index]
 
        p2_list = con_list[star_index + 1:]
 
    count = len(p1_list) + len(p2_list)
 
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result) > 1:
 
        split_index = (count % len(result) - 1)
 

        if split_index >= 0:
 
            right = result[split_index + 1:]
            left = result[: split_index]
 
            result = right + left
 
        else:
            result = result[: len(result) - 1]
 
    print("Relationship status :", result)
