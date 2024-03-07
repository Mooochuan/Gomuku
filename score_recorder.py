class ScoreRecorder:
    def __init__(self):
        self.scores = self.load_scores_from_file()

    def load_scores_from_file(self):
        scores = {}
        try:
            with open("scores.txt", 'r') as file:
                for line in file:
                    name, score = line.strip().split(': ')
                    scores[name] = int(score)
        except FileNotFoundError:
            pass
        return scores

    def record(self, name, result):
        if result == "win":
            if name in self.scores:
                self.scores[name] += 1
            else:
                self.scores[name] = 1
        else:
            if name in self.scores:
                self.scores[name] += 0
            else:
                self.scores[name] = 0

    def write_sorted_scores_to_file(self):
        sorted_scores = sorted(self.scores.items(),
                               key=lambda x: x[1],
                               reverse=True)
        with open("scores.txt", 'w') as file:
            for name, score in sorted_scores:
                file.write(name + ": " + str(score) + "\n")
