"""Generates 60 annotated student wellness journal entries for sentiment analysis."""

import os
import csv
from datetime import date, timedelta

SAMPLE_ENTRIES = [
    ("Finished implementing the computer vision model today! Very happy with the results.", 5, "Positive", 0.85),
    ("Feeling overwhelmed by midterms preparation and two assignment deadlines tomorrow.", 2, "Negative", -0.62),
    ("Went for an evening walk at the riverfront. Feeling peaceful and relaxed.", 4, "Positive", 0.72),
    ("Attended morning database lectures. Standard concepts covered, nothing surprising.", 3, "Neutral", 0.05),
    ("Bug in the database query took four hours to track down. Frustrated but finally resolved.", 2, "Negative", -0.45),
    ("Great hackathon team sync tonight! We finalized our prototype architecture and roles.", 5, "Positive", 0.88),
    ("Woke up tired today. Need to catch up on sleep this weekend.", 2, "Negative", -0.35),
    ("Read two chapters on discrete mathematics. Practiced 10 problem sets.", 4, "Positive", 0.40),
    ("Anxious about upcoming project viva next Monday. Practicing talking points out loud.", 2, "Negative", -0.55),
    ("Cleaned up my GitHub repositories and wrote unit tests for the attendance system.", 5, "Positive", 0.82),
    ("Rainy day in Ahmedabad. Had hot tea and reviewed algorithm notes quietly.", 4, "Positive", 0.65),
    ("Group partner did not submit their frontend module on time. Annoying delay.", 2, "Negative", -0.58),
    ("Received full marks on the Python data structures practical lab!", 5, "Positive", 0.92),
    ("Regular college day. Worked on library study assignments for two hours.", 3, "Neutral", 0.10),
    ("Could not concentrate on coding today. Brain fog and low energy.", 1, "Negative", -0.70),
    ("Refactored code to eliminate technical debt. Much cleaner and modular now.", 4, "Positive", 0.60),
    ("Enjoyed a weekend break with family. Feeling recharged and ready for the week.", 5, "Positive", 0.86),
    ("Missed morning bus, arrived late to class. Started the day on the wrong foot.", 2, "Negative", -0.50),
    ("Trained a random forest model that achieved 91% accuracy on student test data.", 5, "Positive", 0.90),
    ("Ordinary study session. Solved 3 LeetCode problems on arrays and hashing.", 3, "Neutral", 0.20)
]

def generate_csv():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mood_journal_sample_data.csv")

    headers = ["entry_id", "date", "journal_text", "mood_rating", "sentiment_label", "compound_score"]
    rows = []

    start_date = date.today() - timedelta(days=60)
    for i in range(60):
        cur_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        template = SAMPLE_ENTRIES[i % len(SAMPLE_ENTRIES)]
        rows.append([
            f"ENT-{101 + i}",
            cur_date,
            template[0],
            template[1],
            template[2],
            template[3]
        ])

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Generated {len(rows)} journal records at {out_path}")

if __name__ == "__main__":
    generate_csv()
