from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def get_models():

    return {
        "Logistic Regression": LogisticRegression(
            max_iter=1000
        ),

        "Random Forest": RandomForestClassifier(
            random_state=42
        )
    }