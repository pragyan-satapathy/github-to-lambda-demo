import pandas as pd

print('outside function')


def lambda_handler(event, context):
    import a
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done!!!!!!!!!!!!!!!!!')
