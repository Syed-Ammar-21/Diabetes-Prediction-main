import base64
import os
import io
import pandas as pd
import joblib
from PIL import Image
from data.config import thresholds



from sklearn.metrics import (accuracy_score,
                             precision_score,
                             recall_score,
                             f1_score,
                             roc_auc_score)

base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, 'datasets', 'diabetes.csv')
data = pd.read_csv(csv_path)
X = data[['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'Age']]
y = data['Outcome']

# Load and process page icon to remove white background
page_icon_raw = Image.open("image/page_icon.jpeg")
# Convert to RGBA if not already
if page_icon_raw.mode != 'RGBA':
    page_icon_raw = page_icon_raw.convert('RGBA')

# Remove white/light background (make it transparent)
data = page_icon_raw.getdata()
new_data = []
for item in data:
    # If pixel is white or very light (threshold for white removal)
    if item[0] > 240 and item[1] > 240 and item[2] > 240:  # White/light pixels
        new_data.append((255, 255, 255, 0))  # Make transparent
    else:
        new_data.append(item)  # Keep original pixel

page_icon_raw.putdata(new_data)
page_icon = page_icon_raw

# Base64 logo for footer (same image as page_icon)
_buffer = io.BytesIO()
page_icon.save(_buffer, format='PNG')
logo_base64 = base64.b64encode(_buffer.getvalue()).decode()

model = joblib.load('model.pkl')



y_score = model.predict_proba(X)[:, 1]
y_pred = (y_score >= thresholds).astype(int)

# Accuracy Score
accuracy_result = round(accuracy_score(y, y_pred) * 100, 2)
# F1 Score
f1_result = round(f1_score(y, y_pred) * 100, 2)
# Recall Score
recall_result = round(recall_score(y, y_pred) * 100, 2)
# Precision Score
precision_result = round(precision_score(y, y_pred) * 100, 2)
# ROC AUC Score
roc_auc = round(roc_auc_score(y, y_score) * 100, 2)