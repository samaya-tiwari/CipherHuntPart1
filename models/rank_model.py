class RankModel:
    @staticmethod
    def calculate_rank(points: int) -> str:
        if points >= 700:
            return "Oracle"
        elif points >= 500:
            return "Cipher-Smith"
        elif points >= 300:
            return "Cryptic"
        elif points >= 100:
            return "Inquisitor"
        else:
            return "Bystander"


if __name__ == "__main__":
    test_points = [45, 120, 350, 520, 750]
    for p in test_points:
        print(f"Points: {p} -> Rank: {RankModel.calculate_rank(p)}")