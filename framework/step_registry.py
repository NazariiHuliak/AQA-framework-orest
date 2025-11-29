import re

class StepRegistry:
    def __init__(self):
        self.steps = []

    def register(self, stype, pattern, func):
        self.steps.append((stype, re.compile(pattern), func))

    def match(self, stype, text):
        for t, regex, func in self.steps:
            if t == stype:
                match = regex.fullmatch(text)
                if match:
                    return func, match.groups()
        raise Exception(f"No step found for: {stype} {text}")
