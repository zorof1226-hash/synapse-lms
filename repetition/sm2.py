from datetime import date, timedelta
from typing import Tuple

class SM2Scheduler:
    """SuperMemo SM-2 Spaced Repetition Algorithm.
    Quality grades:
      5: Perfect response, complete recall
      4: Correct response with hesitation
      3: Correct response with serious difficulty
      2: Incorrect response, but seemed easy upon seeing answer
      1: Incorrect response, remembered wrong thing
      0: Complete blackout
    """

    @staticmethod
    def calculate_review(quality: int, repetition_count: int, interval_days: int, ease_factor: float) -> Tuple[int, int, float, str]:
        """Returns (new_repetition_count, new_interval_days, new_ease_factor, next_review_date)"""
        # Constrain quality between 0 and 5
        quality = max(0, min(5, quality))

        if quality >= 3:
            if repetition_count == 0:
                new_interval = 1
            elif repetition_count == 1:
                new_interval = 6
            else:
                new_interval = int(round(interval_days * ease_factor))
            new_repetitions = repetition_count + 1
        else:
            new_repetitions = 0
            new_interval = 1

        # Calculate new ease factor: EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
        new_ef = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        if new_ef < 1.3:
            new_ef = 1.3

        next_date = (date.today() + timedelta(days=new_interval)).isoformat()
        return new_repetitions, new_interval, round(new_ef, 2), next_date
