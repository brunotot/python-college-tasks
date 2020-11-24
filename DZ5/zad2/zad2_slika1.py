# Implementirajte konačne automate na slikama 1, 2 i 3.
# Znak ε označava prazan, odnosno prelaz za koji nije potreban ulazni simbol.
# Na primjer, na slici 3 kada se automat nalazi u stanju 2 možemo zbog praznog prelaza pretpostaviti da se
# istovremeno nalazi i u stanju 0. 
# To znači da za idući ulazni simbol automat može krenuti od stanja 2 ili od stanja 0.

from zad2.automaton import Automaton

if __name__ == "__main__":

    automaton = Automaton(
        available_inputs=['a', 'b'],
        available_states=[0, 1, 2, 3],
        start_states=[0],
        end_states=[3]
    )

    automaton.create_link(0, 'b', 0)
    automaton.create_link(0, 'a', 1)
    automaton.create_link(1, 'b', 2)
    automaton.create_link(1, 'a', 1)
    automaton.create_link(2, 'b', 3)
    automaton.create_link(2, 'a', 1)
    automaton.create_link(3, 'b', 0)
    automaton.create_link(3, 'a', 1)

    print(automaton.validate("abbc"))
