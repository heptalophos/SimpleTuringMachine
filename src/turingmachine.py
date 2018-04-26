# -*- coding: utf-8 -*-

"""
    A simple Turing Machine

"""

class SimpleTuringMachine:
    
    tape = []
    state_table = {}
    
    def __init__(self):
        self.tape = ["B", "B", "B", "B"]
        self.state_table = {
            ("B", "s1"): ("X", "R", "s2"),
            ("B", "s2"): ("B", "L", "s3"),
            ("X", "s3"): ("B", "R", "s4"),
            ("B", "s4"): ("B", "L", "s1"),
        }   

    def print_state(self, state, tape, head):
        return state.rjust(4) + ": " + "".join(tape) + "\n" + "      " + " " * head + "^"

    def simulate(self, instructions, steps):
        tape = self.tape
        head = 0
        state = "s1"
        output = []
        output.append(self.print_state(state, tape, head))
        for _ in range(steps):
            key = (tape[head], state)
            tape_symbol, head_direction, new_state = instructions[key]
            tape[head] = tape_symbol
            head += 1 if head_direction == "R" else -1
            state = new_state
            output.append(self.print_state(state, tape, head))
        # print(output)
        last_state = state + ": " + "".join(tape) + "\n" + "    " + " " * head + "^"
        return output            
