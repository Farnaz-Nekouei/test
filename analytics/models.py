from sklearn.linear_model import LinearRegression

def regression(df):

    X = df[["density", "speed"]]
    y = df["flow"]

    model = LinearRegression()
    model.fit(X, y)

    return model