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
            numbers = map(int, string.split(","))
            return min(numbers)
        else:
            return int(string)


    def max(self, string):
        if string == "":
            return 0
        elif "," in string:
            numbers = map(int, string.split(","))
            return max(numbers)
        else:
            return int(string)


    def avg(self, string):
        if string == "":
            return 0
        elif "," in string:
            numbers = map(int, string.split(","))
            return sum(numbers) / float(len(numbers))
        else:
            return int(string)


    def process(self, string):
            return [self.length(string),
                    self.min(string),
                    self.max(string),
                    self.avg(string)]