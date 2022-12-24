import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

def format_column_name(columns:list):
    new_names = {column:' '.join(column.split('_')[::-1]).title() for column in columns}
    new_names['id'] = 'id'
    return new_names



def lower_triangular_matrix(df:pd.DataFrame):
    '''
    This function replaces the values above main diagonal
    to NaN, discarding duplicated correlations
    '''
    mask = np.zeros_like(df, dtype = bool)
    mask[np.triu_indices_from(mask)] = True
    correlations = df.mask(mask)
    return correlations


# Generating confusion matrix
def confusion_matrix_generator(y_test, y_pred):
    matrix = confusion_matrix(y_test, y_pred)
    dict_matrix = {'Positive':{'Positive':matrix[0][0], 'Negative':matrix[0][1]},\
        'Negative':{'Positive': matrix[1][0], 'Negative':matrix[1][1]}}

    df_matrix = pd.DataFrame(dict_matrix)
    return df_matrix

