def update(state, row, alpha=0.85):

    state.flow = alpha * state.flow + (1 - alpha) * row["flow"]
    state.speed = alpha * state.speed + (1 - alpha) * row["speed"]
    state.density = row["density"]

    return state