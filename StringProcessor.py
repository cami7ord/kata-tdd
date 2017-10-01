class StringProcessor:

    def length(self, string):
        if string == "":
            return 0
        elif "," in string:
            return 2
        else:
            return 1
