# merges the predictions and ID prop from Relaxation



pred = open("Predictions.csv", mode ='r')
truth = open("./data/Relaxation/id_prop.csv", mode='r')
output = open("CGCNN Pred vs Truth.csv", mode = 'w')
pred_dict = dict()
truth_dict = dict()

for line in pred:
    parts = line.split(": ")
    pred_dict[parts[0]] = float(parts[1])

for line in truth:
    parts = line.split(",")
    truth_dict[parts[0]] = float(parts[1])


for key in pred_dict.keys():
    output.write("{},{},{}\n".format(key, pred_dict[key], truth_dict[key]))



