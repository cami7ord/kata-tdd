class StringProcessor:

    def length(self, string):
        if string == "":
            return 0
        elif "," in string:
            return len(string.split(","))
        else:
            return 1


    def min(self, string):
        if string == "":
            return 0
        elif "," in string:
            return min(int(string[0]), int(string[2]))
        else:
            return int(string)