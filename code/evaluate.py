from sklearn.metrics import precision_recall_curve
import sys
import sklearn.metrics as metrics

try: import cPickle as pickle   # python2
except: import pickle           # python3

if len(sys.argv) != 4:
    sys.stderr.write('Arguments error. Usage:\n')
    sys.stderr.write('\tpython metrics.py MODEL_FILE TEST_MATRIX METRICS_FILE\n')
    sys.exit(1)

model_file = sys.argv[1]
test_matrix_file = sys.argv[2]
metrics_file = sys.argv[3]

with open(model_file, 'rb') as fd:
    model = pickle.load(fd)

with open(test_matrix_file, 'rb') as fd:
    matrix = pickle.load(fd)

labels = matrix[:, 1].toarray()
x = matrix[:, 2:]

predictions_by_class = model.predict_proba(x)
predictions = predictions_by_class[:,1]

precision, recall, thresholds = precision_recall_curve(labels, predictions)

auc = metrics.auc(recall, precision)
#print('AUC={}'.format(metrics.auc(recall, precision)))
with open(metrics_file, 'w') as fd:
    fd.write('AUC: {:4f}\n'.format(auc))

