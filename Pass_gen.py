from random import randint, choice, shuffle


class Password:

    def __init__(self):
        self.s_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.c_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def pass_gen(self):
        pass_letters = [choice(self.s_letters) + choice(self.c_letters) for _ in range(randint(4, 6))]
        pass_numbers = [choice(self.numbers) for _ in range(randint(2, 4))]
        pass_symbols = [choice(self.symbols) for _ in range(randint(2, 4))]

        pass_list = pass_letters + pass_numbers + pass_symbols
        shuffle(pass_list)
        return "".join(pass_list)
