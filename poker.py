CORRECT_HAND = ["H3", "H2", "H4", "H5"]

def test_input(val1, val2):
    return if val1 in CORRECT_HAND and val2 in CORRECT_HAND

def test_states(vals): # vals is the input hand [H3, H2, HA, H4]
    # Return list of all the cards and their states [P, P, Y, Gr, Gr, Gy, Gr]
    if val = straight_flush(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]

    if val = quads(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]

    if val = boat(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]

    if val = flush(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]
    
    if val = straight(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]

    if val = trips(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]

    if val = two_pair(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]

    if val = pair(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]

    if val = high_card(vals); val[0]: # (True, [(HK, Gr), (S3, Gy), Gr, Gy, Gr])
        return val[1]

    return 

def not_valid():
    if vals is None:
        return True

def main():
    game_won = False
    while not game_won:
        vals = None
        while not_valid(vals):
            vals = input("Please write your inputs in csv format").split(",")
        first_card, second_card = vals[0], vals[1]
        print(f"first: {first_card}, second: {second_card}")
        
        game_won = test_input(first_card, second_card)
        get_states = test_states(first_card, second_card)
        
        color_cards(get_states)
        # temp for console output
        print(get_states) # [Gr, Gy, Gr, Gy, Gr]


if __name__ == "__main__":
    main()
        
