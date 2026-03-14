def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guess range for a difficulty label.

    Args:
        difficulty: Difficulty string ("Easy", "Normal", "Hard").

    Returns:
        A tuple of (low, high) for the guess range.
    """
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
    """Parse raw user input into an integer guess.

    Args:
        raw: Raw user string input.

    Returns:
        A tuple (ok, value, error_message).
        - ok: True if parse succeeded.
        - value: The parsed integer guess or None.
        - error_message: Reason for parse failure, if any.
    """
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
    """Compare a guess against the secret and return outcome and hint.

    Args:
        guess: The user's guess value (int or string convertible to int).
        secret: The secret number value (int or string convertible to int).

    Returns:
        A tuple (outcome, message).
        - outcome: "Win", "Too High", "Too Low", or "Invalid".
        - message: Hint string for the player.
    """
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
    """Compute the updated score based on outcome and attempt count.

    Args:
        current_score: Current player score.
        outcome: Result from check_guess ("Win", "Too High", "Too Low", "Invalid").
        attempt_number: Number of attempts taken so far.

    Returns:
        Updated score integer.
    """
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
