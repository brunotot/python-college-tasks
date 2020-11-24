class Automaton:
    def __init__(self, available_inputs, available_states, start_states, end_states):
        self.available_inputs = set(available_inputs)
        self.available_states = set(available_states)
        self.start_states = set(start_states)
        self.end_states = set(end_states)
        self.links = {}
        self.crossings = {}
        for state in available_states:
            self.links[state] = []
            self.crossings[state] = [state]

    def create_link(self, start_state, input_value, end_state):
        if input_value in self.available_inputs and (input_value, end_state) not in self.links[start_state]:
            self.links[start_state].append((input_value, end_state))

    def create_crossing(self, start_state, end_state):
        if start_state in self.crossings and end_state not in self.crossings[start_state]:
            self.crossings[start_state].append(end_state)

    def validate(self, n):
        if set(n).issubset(self.available_inputs):
            for start_state in self.start_states:
                if self.__recursive_validation(n, start_state):
                    return True
        return False

    def __recursive_validation(self, n, current_state):
        if len(n) == 0:
            return current_state in self.end_states
        for state in self.crossings[current_state]:
            for link in self.links[state]:
                if n[0] == link[0] and self.__recursive_validation(n[1:], link[1]):
                    return True
        return False
