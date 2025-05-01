import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

# ===== 1. Load dan Preprocessing Dataset =====
df = pd.read_csv('data/telco_customer_churn_final.csv')

# Drop kolom yang menyebabkan data leakage
leakage_cols = ['Customerstatus', 'Churnscore', 'Cltv']
df = df.drop(columns=leakage_cols)

# Konversi target ke numerik
df['Churnlabel'] = df['Churnlabel'].map({'No': 0, 'Yes': 1})

# Pisahkan X dan y
X = df.drop(columns='Churnlabel')
y = df['Churnlabel']

# One-hot encoding fitur kategorikal
X = pd.get_dummies(X, drop_first=True)

# ===== 2. Train-Test Split =====
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===== 3. SMOTE Resampling pada Data Latih =====
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# ===== 4. Daftar Model =====
models = {
    'Random Forest': RandomForestClassifier(random_state=42),
    'KNN': KNeighborsClassifier(),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'SVM RBF': SVC(kernel='rbf', probability=True, random_state=42),
    'XGBoost': XGBClassifier(eval_metric='logloss', random_state=42)
}

# ===== 5. Evaluasi Model =====
results = {
    'Model': [],
    'Accuracy': [],
    'ROC-AUC': [],
    'Precision': [],
    'Recall': [],
    'F1-Score': []
}

for name, model in models.items():
    model.fit(X_train_res, y_train_res)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    report = classification_report(y_test, y_pred, output_dict=True)

    results['Model'].append(name)
    results['Accuracy'].append(accuracy_score(y_test, y_pred))
    results['ROC-AUC'].append(roc_auc_score(y_test, y_proba))
    results['Precision'].append(report['macro avg']['precision'])
    results['Recall'].append(report['macro avg']['recall'])
    results['F1-Score'].append(report['macro avg']['f1-score'])

# ===== 6. Tampilkan Hasil =====
results_df = pd.DataFrame(results)
print("=== Hasil Evaluasi Model ===")
print(results_df)
