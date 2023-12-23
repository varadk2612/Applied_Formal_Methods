import stormpy

prism_prog = stormpy.parse_prism_program("car_ped.prism")
prop_to_check = stormpy.parse_properties('Pmax=? [F c=3 & p=3]', prism_prog)
model = stormpy.build_sparse_model(prism_prog, prop_to_check)

# print(model.nr_states)
print(model)
print(stormpy.check_model_sparse(model, prop_to_check[0]).get_values())

# print(model.markovian_states)

if __name__ == '__main__': pass



# This is chances of collision ([F (c = 3 & p = 3)])
# [0.1168561287106359, 
#  0.02039858396415135, 0.3125381618665129, 
#  0.3201812849906691, 0.0010405827263267429, 
#  0.03225806451612903, 0.10123966942148756, 
#  0.3181818181818181, 1.0, 
#  0.0, 0.0, 
#  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]