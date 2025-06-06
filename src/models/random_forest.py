from sklearn.ensemble import RandomForestClassifier

def get_random_forest(n_estimators=100, random_state=42):
    return RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)