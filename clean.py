import pandas as pd

def clean(input1, input2, output):
    # read file
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)

    # merge data
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    # delete id column
    merged_df = merged_df.drop(columns=['id'])

    # delete na rows
    merged_df = merged_df.dropna()

    # delete rows with 'insurance' or 'Insurance'
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    return merged_df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='1st data file (CSV)')
    parser.add_argument('input2', help='2nd data file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2, args.output)
    cleaned.to_csv(args.output, index=False)


