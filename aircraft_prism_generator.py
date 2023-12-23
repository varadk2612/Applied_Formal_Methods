NAME_OF_FILE_TO_GENERATE = "aircraft_MDP_generator.prism"  #Add prism to the end of this file

# For acceleration

# action_nextstate_nextspeed
P_ACC_STAY_FAST = 0.2
P_ACC_FORW_FAST = 0.7
P_ACC_FORW_SLOW = 0.02
P_ACC_STAY_SLOW = 0.08

# For braking
P_BRK_STAY_FAST = 0.01
P_BRK_STAY_SLOW = 0.2
P_BRK_FORW_FAST = 0.09
P_BRK_FORW_SLOW = 0.7

P_GO_SLOW_STAY_FAST = 0.1
P_GO_NEXT_FAST = 0.8
P_GO_STAY_SLOW = 0.4

# For turning
P_TURN_SUCCESS = 0.9
P_TURN_FAIL = 0.1

# # 
# P_PED_STAY = 0.7
# P_PED_FORW = 0.3

NUM_PLANE_STATES = 12
# NUM_PED_STATES = 5

with open(NAME_OF_FILE_TO_GENERATE, "w") as filename:
    filename.write("dtmc \n\n")
    filename.write(f"module plane{NUM_PLANE_STATES} \n\n")
    
    filename.write(f"\t c : [1..{NUM_PLANE_STATES}] init 1; \n")
    
    #Going from 1 to 12. We label odd states as Fast, even states as Slow.
    # When Slow, we can accelerate, go.
    # When Fast, we can brake, go.
    for plane in range(1, NUM_PLANE_STATES + 1):
        # if(car == 1 and ped == 3):
        #     filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY), 2}:(c'={car}) & (p'={ped}) + {round(P_BRK_FORW*P_PED_STAY)}:(c'={car+1}) & (p'={ped}) + {round(P_BRK_STAY*P_PED_FORW)}:(c'={car}) & (p'={ped+1}) + {round(P_BRK_FORW*P_PED_FORW)}:(c'={car+1}) & (p'={ped+1}); \n")

        # elif car == 2 and (ped == 2 or ped == 3 or ped == 4):
        #     filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY), 2}:(c'={car}) & (p'={ped}) + {round(P_BRK_FORW*P_PED_STAY)}:(c'={car+1}) & (p'={ped}) + {round(P_BRK_STAY*P_PED_FORW)}:(c'={car}) & (p'={ped+1}) + {round(P_BRK_FORW*P_PED_FORW)}:(c'={car+1}) & (p'={ped+1}); \n")

        # elif car == 3 and ped == 3:
        #     filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY), 2}:(c'={car}) & (p'={ped}) + {round(P_BRK_FORW*P_PED_STAY)}:(c'={car+1}) & (p'={ped}) + {round(P_BRK_STAY*P_PED_FORW)}:(c'={car}) & (p'={ped+1}) + {round(P_BRK_FORW*P_PED_FORW)}:(c'={car+1}) & (p'={ped+1}); \n")
        if(plane%2 ==1):#Fast
            filename.write(f"\t \t[go] p={plane} -> 0.1:(p'={plane}) + 0.8:(p'={plane+2}) +  \n")
            filename.write(f"\t \t[go]")
            
        if car == 5 and ped == 5:
            filename.write(f"\t \t[] c={car} & p={ped} -> 1:(c'={car}) & (p'={ped}); \n")

        elif car == 5:
            filename.write(f"\t \t[accelerate] c={car} & p={ped} -> {round(P_ACC_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_ACC_STAY*P_PED_FORW, 2)}: (c'={car}) & (p'={ped+1}); \n")
            filename.write(f"\t \t[brake] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_BRK_STAY*P_PED_FORW, 2)}: (c'={car}) & (p'={ped+1}); \n")

        elif ped == 5:
            filename.write(f"\t \t[accelerate] c={car} & p={ped} -> {round(P_ACC_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_ACC_FORW*P_PED_STAY, 2)}: (c'={car+1}) & (p'={ped}); \n")
            filename.write(f"\t \t[brake] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_BRK_FORW*P_PED_STAY, 2)}: (c'={car+1}) & (p'={ped}); \n")

        else:
            filename.write(f"\t \t[accelerate] c={car} & p={ped} -> {round(P_ACC_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_ACC_FORW*P_PED_STAY, 2)}:(c'={car+1}) & (p'={ped}) + {round(P_ACC_STAY*P_PED_FORW, 2)}:(c'={car}) & (p'={ped+1}) + {round(P_ACC_FORW*P_PED_FORW, 2)}:(c'={car+1}) & (p'={ped+1}); \n")
            filename.write(f"\t \t[brake] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_BRK_FORW*P_PED_STAY, 2)}:(c'={car+1}) & (p'={ped}) + {round(P_BRK_STAY*P_PED_FORW, 2)}:(c'={car}) & (p'={ped+1}) + {round(P_BRK_FORW*P_PED_FORW, 2)}:(c'={car+1}) & (p'={ped+1}); \n")
        