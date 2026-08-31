from sklearn.impute import (
    SimpleImputer,
    KNNImputer
)


def get_imputers():

    return {
        "Mean": SimpleImputer(
            strategy="mean"
        ),

        "Median": SimpleImputer(
            strategy="median"
        ),

        "KNN": KNNImputer(
            n_neighbors=5
        )
    }