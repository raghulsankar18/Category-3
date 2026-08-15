# Local Beam Search

def f(x):
    return -(x - 5) ** 2 + 25


def local_beam_search(k):s
    states = [0, 2, 7]

    for _ in range(20):

        all_candidates = []
        for state in states:

            neighbors = [state - 1, state + 1]

            for neighbor in neighbors:
                if 0 <= neighbor <= 10:
                    all_candidates.append(neighbor)


        all_candidates.extend(states)

        all_candidates = list(set(all_candidates))

        states = sorted(
            all_candidates,
            key=f,
            reverse=True
        )[:k]

        if f(states[0]) == 25:
            break

    best_state = max(states, key=f)

    return best_state, f(best_state)


k = int(input("Enter number of beams (K): "))

state, value = local_beam_search(k)

print("\nLocal Beam Search Result")
print("Best State:", state)
print("Maximum Value:", value)
