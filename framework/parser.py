class FeatureParser:

    def parse(self, path):
        steps = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Given "):
                    steps.append(("GIVEN", line[6:]))
                elif line.startswith("When "):
                    steps.append(("WHEN", line[5:]))
                elif line.startswith("Then "):
                    steps.append(("THEN", line[5:]))
        return steps
