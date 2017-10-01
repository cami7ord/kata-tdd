class StringProcessor:

    def length(self, string):
        if string == "":
            return 0
        elif "," in string:
            return len(string.split(","))
        else:
            return 1
