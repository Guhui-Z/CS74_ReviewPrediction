from final_iteration_model import FinalIterationModel

# driver code to produce predictions CSV file
tr = '/Users/zhangguhui/OneDrive - Dartmouth College/CS 74/datasets/Train.csv'
te = '/Users/zhangguhui/OneDrive - Dartmouth College/CS 74/datasets/Test.csv'
m = FinalIterationModel(tr, te, 'predict')
