import numpy as np

def introduce_missingness(X, missing_rate, random_state=None):

    # 1. Make a copy
    X_missing = X.copy()

    # 2. Calculate number of cells
    no_cells = X.shape[0] * X.shape[1]

    # 3. Calculate number of missing values
    no_missing = int(no_cells * missing_rate)

    # 4. Create random number generator
    rng = np.random.default_rng(random_state)

    # 5. Randomly select unique cells
    indices = rng.choice(no_cells, size=no_missing, replace=False)

    # 6. Convert selected positions to row/column indices
    rows, columns = np.unravel_index(indices, X.shape)

    # 7. Replace those cells with NaN
    X_missing.values[rows, columns] = np.nan


    # 8. Return modified copy
    return X_missing