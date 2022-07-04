import pandas as pd
import sagemaker

def automl():
  
  df = pd.read_csv('./data/diamonds.csv')
  session = sagemaker.Session()
  
  prefix = 'sagemaker/autopilot/input'
  
  uri = session.upload_data(path = './data/diamonds.csv', key_prefix = prefix)

  #print(uri): "s3://sagemaker-us-east-1-082380823452/sagemaker/autopilot/input/./data/diamonds.csv"
  output = 's3://sagemaker-us-east-1-082380823452/sagemaker/autopilot/output'
  
  #OutcomeL: Automl predictions

  
if __name__ == "__main__":
    automl()
