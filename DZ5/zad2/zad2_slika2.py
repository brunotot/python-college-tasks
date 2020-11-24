# Implementirajte konačne automate na slikama 1, 2 i 3.
# Znak ε označava prazan, odnosno prelaz za koji nije potreban ulazni simbol.
# Na primjer, na slici 3 kada se automat nalazi u stanju 2 možemo zbog praznog prelaza pretpostaviti da se
# istovremeno nalazi i u stanju 0. 
# To znači da za idući ulazni simbol automat može krenuti od stanja 2 ili od stanja 0.

from zad2.automaton import Automaton

if __name__ == "__main__":

    automaton = Automaton(
        available_inputs=['a', 'b'],
        available_states=[0, 1, 2, 3, 4],
        start_states=[0],
        end_states=[2, 4]
    )

    automaton.create_crossing(0, 1)
    automaton.create_crossing(0, 3)

    automaton.create_link(1, 'a', 2)
    automaton.create_link(3, 'b', 4)
    automaton.create_link(2, 'a', 2)
    automaton.create_link(4, 'b', 4)

    print(automaton.validate("bbbbbbbb"))
