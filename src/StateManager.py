# Initialize the state variable
state = "initial"
# Define possible states
possible_states = ["initial", "gameover", "victory", "loss", "menu", "settings"]
def setState(newState):
    global state
    if newState in possible_states:
        state = newState
    else:
        raise ValueError(f"{newState} is not a valid state.")
def getState():
    return state

