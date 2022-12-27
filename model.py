class Model:
    def __init__(self):
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif isinstance(caption, int):
            self.value += str(caption)

        elif caption == '=':
            value = self._evaluate()
            if '.0' in str(value):
                value = int(value)
            self.value = str(value)

        elif caption == '.':
            if caption not in self.value:
                self.value += caption

        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)
