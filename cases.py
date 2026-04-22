from models import Suspect, Clue, Case

def load_cases():

    case1 = Case(
        "The Locked Room at Blackwood Manor",
        """A violent storm isolates Blackwood Manor.
Alistair Blackwood is found dead in his locked study.
A single glass of wine sits beside him.

No signs of forced entry.
The door was locked from inside.
Something does not add up.""",

        suspects=[
            Suspect("Emily", {
                "Where were you?": "In my room the entire night.",
                "Motive?": "I needed money, but I wouldn't kill him.",
                "Did you enter the study?": "No, I stayed upstairs."
            }),

            Suspect("James", {
                "Where were you?": "Serving dinner and then in quarters.",
                "Did you enter the study?": "No, I locked it and left.",
                "Who handled the wine?": "I poured it myself."
            }),

            Suspect("Dr. Reed", {
                "Argument?": "Yes, about his health.",
                "Medicine?": "I prescribed mild sedatives.",
                "Did you visit the study?": "No."
            }),

            Suspect("Clara", {
                "What did you see?": "The window was slightly open.",
                "Anything unusual?": "The hallway was empty.",
                "Did you enter the study?": "No."
            })
        ],

        clues=[
            Clue("-> Wine glass contains poison"),
            Clue("-> Wine bottle is clean"),
            Clue("-> Window too small to escape"),
            Clue("-> Butler has duplicate keys"),
            Clue("-> Poison matches doctor's medicine")
        ],

        contradictions=[
            "James claimed he never re-entered, yet he had duplicate keys.",
            "Poison is only in glass, meaning it was added after pouring."
        ],

        solution="James"
    )

    # ========================= CASE 2 =========================

    case2 = Case(
        "The Midnight Train Murder",
        """A luxury train cuts through the darkness at midnight.
Businessman Rajiv Mehta is found dead in his private compartment.

The door was locked from inside.
No blood outside the room.
The train never stopped.

The killer must still be on board.""",

        suspects=[
            Suspect("Priya", {
                "Where were you?": "I was asleep in my cabin.",
                "Motive?": "We argued, but I loved him.",
                "Did you see anything?": "No, nothing unusual."
            }),

            Suspect("Rohan", {
                "Where were you?": "Working late on business reports.",
                "Motive?": "He trusted me completely.",
                "Why change clothes?": "I spilled something earlier."
            }),

            Suspect("Stranger", {
                "Where were you?": "Walking through compartments.",
                "Ticket?": "I lost it.",
                "Did you know victim?": "No."
            }),

            Suspect("Collector", {
                "Where were you?": "Checking tickets all night.",
                "Did you enter his cabin?": "No.",
                "Anything unusual?": "Lights flickered once."
            })
        ],

        clues=[
            Clue("-> No blood outside compartment"),
            Clue("-> Knife belongs to train kitchen"),
            Clue("-> Assistant changed clothes"),
            Clue("-> Compartment locked from inside"),
            Clue("-> Wife has no blood stains")
        ],

        contradictions=[
            "Rohan claimed innocence, but changed clothes suspiciously.",
            "No blood outside suggests killer stayed inside after attack."
        ],

        solution="Rohan"
    )

    # ========================= CASE 3 =========================

    case3 = Case(
        "The Abandoned Hospital Case",
        """An abandoned hospital stands silent for years.
A YouTuber exploring it is found dead.

Camera footage is corrupted.
No sign of forced entry.
Strange noises echo through empty halls.

Someone else was there that night.""",

        suspects=[
            Suspect("Vik", {
                "Where were you?": "Filming with him.",
                "Argument?": "Just a small one.",
                "What happened?": "I blacked out."
            }),

            Suspect("Guard", {
                "Where were you?": "At the gate.",
                "Power outage?": "Yes, lights went out.",
                "Did anyone enter?": "No."
            }),

            Suspect("Rival", {
                "Where were you?": "At home.",
                "Jealous?": "He stole my ideas.",
                "Did you visit hospital?": "No."
            }),

            Suspect("Caretaker", {
                "Where were you?": "Maintaining outer area.",
                "Know building?": "Yes, very well.",
                "Anything strange?": "Voices sometimes."
            })
        ],

        clues=[
            Clue("-> Footprints show only 2 people"),
            Clue("-> Camera footage partially deleted"),
            Clue("-> Guard lied about power outage"),
            Clue("-> Weapon: metal rod from inside"),
            Clue("-> No third-party entry")
        ],

        contradictions=[
            "Guard lied about power outage.",
            "Only two people inside means killer is one of them."
        ],

        solution="Vik"
    )

    # ========================= CASE 4 =========================

    case4 = Case(
        "The Poisoned Dinner Party",
        """A lavish dinner party ends in tragedy.
Host Mrs. Kapoor collapses after drinking wine.

Everyone had access.
No one saw anything.
Yet only one glass was poisoned.

Someone planned this carefully.""",

        suspects=[
            Suspect("Chef", {
                "Where were you?": "In the kitchen.",
                "Did you serve drinks?": "No.",
                "Any issues?": "Everything was normal."
            }),

            Suspect("Friend", {
                "Where were you?": "Dining table.",
                "Motive?": "We were close.",
                "Did you notice anything?": "She looked nervous."
            }),

            Suspect("Husband", {
                "Where were you?": "With guests.",
                "Relationship?": "Complicated.",
                "Seat change?": "Just casual."
            }),

            Suspect("Waiter", {
                "Where were you?": "Serving drinks.",
                "New here?": "Yes.",
                "Did you notice anything?": "No."
            })
        ],

        clues=[
            Clue("-> Only victim's glass poisoned"),
            Clue("-> Chef never handled drinks"),
            Clue("-> Waiter served drinks"),
            Clue("-> Husband switched seats"),
            Clue("-> Cyanide detected")
        ],

        contradictions=[
            "Husband switched seats unexpectedly.",
            "Poison targeted a specific glass, not random."
        ],

        solution="Husband"
    )

    # ========================= CASE 5 =========================

    case5 = Case(
        "The College Hostel Nightmare",
        """A quiet hostel night turns deadly.
Student Arjun is found strangled in his room.

No forced entry.
Door was unlocked.
Only familiar faces around.

The killer was someone he trusted.""",

        suspects=[
            Suspect("Roommate", {
                "Where were you?": "In the room.",
                "Argument?": "Just normal fight.",
                "Last call?": "Yes, we talked."
            }),

            Suspect("Girlfriend", {
                "Where were you?": "Near hostel gate.",
                "Breakup?": "Yes, recently.",
                "Did you meet him?": "No."
            }),

            Suspect("Senior", {
                "Where were you?": "On same floor.",
                "Ragging?": "Just fun.",
                "Any conflict?": "No."
            }),

            Suspect("Watchman", {
                "Where were you?": "At entrance.",
                "Saw anything?": "Someone in hoodie.",
                "Time?": "Late night."
            })
        ],

        clues=[
            Clue("-> No forced entry"),
            Clue("-> Last call to roommate"),
            Clue("-> Hoodie found in room"),
            Clue("-> Watchman saw figure"),
            Clue("-> Signs of struggle inside")
        ],

        contradictions=[
            "Roommate claims calm, but evidence shows struggle.",
            "Hoodie found in room contradicts unknown intruder theory."
        ],

        solution="Roommate"
    )

    return [case1, case2, case3, case4, case5]

    return [case1]