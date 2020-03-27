inputf = open("date.txt", "r")
nrOfStates = int(inputf.readline())
nrOfChars = int(inputf.readline())
chars = inputf.readline().split()
chars.append('$')
initialState = int(inputf.readline())
nrOfValidStates = int(inputf.readline())
validStates = [int(x) for x in inputf.readline().split()]
nrOfTransitions = int(inputf.readline())
transitions = [[{char: [] for char in chars}][0] for x in range(nrOfStates)]
for i in range(nrOfTransitions):
    transition = inputf.readline().split()
    transitions[int(transition[0])][transition[1]].append(int(transition[2]))
print("Word: ")
cuv = input()
states = []
valid = False
states.append((initialState, 0))
while states:
    currentState = states.pop()
    stateNr = currentState[0]
    position = currentState[1]
    for state in transitions[stateNr]['$']:
        states.append((state, position))
    if position == len(cuv):
        if stateNr in validStates:
            valid = True
            break
    else:
        character = cuv[position]
        for state in transitions[stateNr][character]:
            states.append((state, position + 1))
print(valid)
