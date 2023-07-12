import pandas as pd
import sys
import joblib
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import sklearn

print("***** Loading model...")
print("***** Python version:", sys.version)
print("***** joblib version:", joblib.__version__)
print("***** scikit version:", sklearn.__version__)
# load model
model = joblib.load('house_price_model.pkl', 'r')
print("***** model loaded")


def get_price(parameter_array):
    """
    Gets the price of a house given the parameters
    """
    print('> model prediction params', parameter_array)

    # Create a 'DataFrame' with column headers matching the variables the model wants
    my_df = pd.DataFrame(columns=[
        'LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd'])

    # Input your test values into the dataframe
    my_df.loc[0] = parameter_array

    # use the model on the dataframe to calculate the house price for each row
    test_prediction = model.predict(my_df)

    print('> prediction result', test_prediction)
    return int(test_prediction[0])
