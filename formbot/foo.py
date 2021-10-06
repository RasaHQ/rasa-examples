import numpy as np
from hulearn.classification import FunctionClassifier


def fare_based(dataf, threshold=10):
    """
    The assumption is that folks who paid more are wealthier and are more
    likely to have recieved access to lifeboats.
    """
    return np.array(dataf["fare"] > threshold).astype(int)


# The function is now turned into a scikit-learn compatible classifier.
mod = FunctionClassifier(fare_based)

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import *

# The GridSearch object can now "grid-search" over this model.
grid = GridSearchCV(
    mod,
    cv=2,
    param_grid={"threshold": np.linspace(0, 100, 30)},
    scoring={
        "accuracy": make_scorer(accuracy_score),
        "precision": make_scorer(precision_score),
        "recall": make_scorer(recall_score),
    },
    refit="accuracy",
)
grid.fit(X, y)


from hulearn.experimental.interactive import InteractiveCharts

df = load_penguins()
clf = InteractiveCharts(df, labels="species")

# It's best to run this in a single cell.
clf.add_chart(x="bill_length_mm", y="bill_depth_mm")

from hulearn.classification import InteractiveClassifier

# This classifier uses a point-in-poly method to convert the drawn
# data from `clf` into a scikit-learn classifier.
model = InteractiveClassifier(json_desc=clf.data())
