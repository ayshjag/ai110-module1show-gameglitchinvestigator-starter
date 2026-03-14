def get_range_for_difficulty(difficulty: str):
    # FIX: Refactored and verified ranges with Copilot Agent mode.
    # FIX ME: Difficulty mapping must match values used by the game.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    # FIX: Added validation in collaboration with Copilot Agent mode.
    # FIX ME: Must reject blank input and non-number input.
    if raw is None or str(raw).strip() == "":
        return False, None, "Enter a guess."

    raw = str(raw).strip()
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    # FIX: Co-developed type normalization with Copilot Agent mode.
    # FIX ME: Normalize input types before comparing.
    try:
        guess_int = int(guess)
    except (ValueError, TypeError):
        return "Invalid", "That guess is invalid."

    try:
        secret_int = int(secret)
    except (ValueError, TypeError):
        return "Invalid", "Game is in an invalid state."

    if guess_int == secret_int:
        return "Win", "🎉 Correct!"
    if guess_int > secret_int:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    # FIX ME: Ensure scoring is consistent and floor at minimum points for a win.
    if outcome == "Win":
        # FIX: Added safe win scoring minimum with guidance from Copilot Agent mode.
        # FIX ME: Ensure scoring is consistent and floor at minimum points for a win.
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
