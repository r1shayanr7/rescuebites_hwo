import json

# 1. Load your notebook
with open('reinforcementandpredictiveanalysismodel.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# 2. Fix the widgets metadata while preserving everything else
if 'metadata' in notebook and 'widgets' in notebook['metadata']:
    # Either remove widgets completely:
    del notebook['metadata']['widgets']
    
    # OR fix each widget by adding state (uncomment below):
    # for widget in notebook['metadata']['widgets']:
    #     if 'state' not in widget:
    #         widget['state'] = {}

# 3. Save the fixed notebook
with open('rmodel.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2)