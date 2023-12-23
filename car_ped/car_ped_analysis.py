import stormpy
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

prism_prog = stormpy.parse_prism_program("car_ped/car_ped_parallelcomposition_policy.prism")
prop_to_check = stormpy.parse_properties('Pmax =? [ (G !(c = 3 & p = 3)) & (F (c=5 & p = 5))]', prism_prog)
model = stormpy.build_sparse_model(prism_prog, prop_to_check)

print(model)

for state in model.states:
    if state.id in model.initial_states:
        print(state)
    for action in state.actions:
        for transition in action.transitions:
            print("From state {}, with probability {}, go to state {}".format(state, transition.value(),transition.column))




print(stormpy.check_model_sparse(model, prop_to_check[0]))
probabilities = stormpy.check_model_sparse(model, prop_to_check[0]).get_values()
print(probabilities)

# umm??
probs_2 = []
weird_order = [0,1,4,9,15,2,3,5,10,16,6,7,8,11,17,12,13,14,18,19,20,21,22,23,24]
for i in weird_order:
    probs_2.append(probabilities[i])

probs_2 = numpy.reshape(probs_2, (5, 5))

plt.cla()
plt.clf()
heatmap = sns.heatmap(probs_2, annot=True, cmap='Blues', xticklabels=["c1", "c2", "c3", "c4", "c5"], yticklabels=["p1", "p2", "p3", "p4", "p5"])
heatmap.set(xlabel='Car States', ylabel='Pedestrian States')
plt.savefig('car_ped_auto_heatmap.png')



if __name__ == '__main__': pass