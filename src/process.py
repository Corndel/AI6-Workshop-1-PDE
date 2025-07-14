import pandas as pd
import numpy as np
import argparse
import os
from sklearn.model_selection import train_test_split

input_data_path = "../data/cs-training.csv"
train_output_path = "../processing/train/"
validation_output_path = "../processing/validation/"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-test-split-ratio", type=float, default=0.2)
    args, _ = parser.parse_known_args()

    df = pd.read_csv(input_data_path)

    df = df.drop(columns=['Unnamed: 0'])
    df['MonthlyIncome'].fillna(df['MonthlyIncome'].median(), inplace=True)
    df['NumberOfDependents'].fillna(df['NumberOfDependents'].mode()[0], inplace=True)
    df.rename(columns={'SeriousDlqin2yrs': 'Target'}, inplace=True)
  
    X = df.drop('Target', axis=1)
    y = df['Target']
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=args.train_test_split_ratio, random_state=42, stratify=y)

    train_df = pd.concat([y_train, X_train], axis=1)
    validation_df = pd.concat([y_val, X_val], axis=1)

    train_df.to_csv(os.path.join(train_output_path, 'train.csv'), index=False, header=False)
    validation_df.to_csv(os.path.join(validation_output_path, 'validation.csv'), index=False, header=False)
