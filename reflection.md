# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
[1.]the game doesn't restart if we click new game, the message remains static, even when the secret gets reset
[2.] If we choose easy on the side bar, the range says 1-20, allows 6 attempts. In the main page the range is 1-100 and the game is played for the same. 
[3]Similar glitch for Hard were the range is 1-50 ,but it varies from 1-100 in main page.The attempts are correct. But the secret, range are not correct
[4] The Hints are backwards

---

## 2. How did you use AI as a teammate?

- I used GitHub Copilot (via this coding assistant) to inspect code, suggest fixes, and generate tests.
- Correct AI suggestion: Copilot pointed out the secret type mismatch issue where `check_guess` sometimes compared int to string due to session-state value conversion. I verified this by reading `app.py` and `logic_utils.py`, patching `check_guess` to normalize values to int, and then running `pytest` to confirm guessed outcomes were correct and game hints behaved consistently.
- Incorrect/misleading AI suggestion: Initially, Copilot suggested converting secret to string in alternate attempts (from original app behavior), which was misleading because it caused type-comparison bugs. I verified it was wrong by running the game logic manually and seeing incorrect outcomes for numeric comparisons, then fixed it by always keeping numeric comparison and retesting with unit tests.

---

## 3. Debugging and testing your fixes

- I decided a bug was fixed when I could reproduce the broken behavior before the change, apply the code fix, and then run the same case successfully. For logic bugs, I also added unit tests that failed before the fix and then passed after the fix.
- I ran `pytest -q` after implementing the fixes. It showed `17 passed`, confirming all unit tests for `parse_guess`, `check_guess`, `update_score`, and range mapping now behave correctly. I also manually ran `streamlit run app.py` and verified that attempts, secret range, and win/lose behavior are stable and accurate.
- Yes, AI helped me design tests by suggesting specific edge case checks (empty guess, float input, string secret, and attempt-based scoring). I used those suggestions to add tests in `tests/test_game_logic.py` and confirm the behavior.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  The original app generated or reconstructed the secret value on every rerun (and sometimes as a string on alternating attempts), so the value was not stable across reruns and guess checks. That made the game inconsistent and caused wrong outcomes.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns the whole script whenever the user interacts with widgets (like buttons or text input). Session state is the way to remember values across reruns, so variables like secret number and attempts persist rather than resetting each time.
- What change did you make that finally gave the game a stable secret number?
  I initialized `st.session_state.secret` once and only reset it after pressing New Game. I also stopped converting secret to string based on attempt parity and always used integer comparisons.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
