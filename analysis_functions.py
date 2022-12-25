import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Metrics
def report(K_value, y_test, y_pred):  
    metrics = precision_recall_fscore_support(y_test, y_pred) 

    dict_to_frame = {}
    diagnosis = ['Benign', 'Malignant']
    for i in range (len(diagnosis)):
        dict_to_frame[diagnosis[i]] = {'Error':np.mean(y_pred != y_test), 'Accuracy':accuracy_score(y_test, y_pred),'Precision':metrics[0][i], \
            'Recall':metrics[1][i], 'F1-Score':metrics[2][i], 'Support':metrics[3][i]}

    report_df = pd.DataFrame(dict_to_frame).T
    report_df['K-Value'] = [K_value, K_value]
    return report_df

def generate_csv(all_exec_df, number_of_execution):
    output = pd.concat(all_exec_df).reset_index()
    output.rename(columns={'index':'diagnosis'}, inplace=True)
    output.to_csv(f'results_exec_{number_of_execution}.csv')
    print(f'Execution {number_of_execution} finished.\nResults were saved on results_exec_{number_of_execution}.csv')