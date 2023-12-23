NAME_OF_FILE_TO_GENERATE = "car_ped_parallelcomposition_policy.prism"  #Add prism to the end of this file

# For acceleration
P_ACC_STAY = 0.1
P_ACC_FORW = 0.9

# For braking
P_BRK_STAY = 0.8
P_BRK_FORW = 0.2

P_PED_STAY = 0.7
P_PED_FORW = 0.3

NUM_CAR_STATES = 5
NUM_PED_STATES = 5

with open(NAME_OF_FILE_TO_GENERATE, "w") as filename:
    filename.write("dtmc \n\n")
    filename.write(f"module car{NUM_CAR_STATES}_ped{NUM_PED_STATES}_parallelcomposition_policy \n\n")
    
    filename.write(f"\t c : [1..{NUM_CAR_STATES}] init 1; \n")
    filename.write(f"\t p : [1..{NUM_CAR_STATES}] init 1; \n")
    
    for car in range(1, NUM_CAR_STATES + 1):
        for ped in range(1, NUM_PED_STATES + 1):
            if(car == 1 and ped == 3):
                filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_BRK_FORW*P_PED_STAY, 2)}:(c'={car+1}) & (p'={ped}) + {round(P_BRK_STAY*P_PED_FORW, 2)}:(c'={car}) & (p'={ped+1}) + {round(P_BRK_FORW*P_PED_FORW, 2)}:(c'={car+1}) & (p'={ped+1}); \n")
    
            elif car == 2 and (ped == 2 or ped == 3 or ped == 4):
                filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_BRK_FORW*P_PED_STAY, 2)}:(c'={car+1}) & (p'={ped}) + {round(P_BRK_STAY*P_PED_FORW, 2)}:(c'={car}) & (p'={ped+1}) + {round(P_BRK_FORW*P_PED_FORW, 2)}:(c'={car+1}) & (p'={ped+1}); \n")
    
            elif car == 3 and ped == 3:
                filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_BRK_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_BRK_FORW*P_PED_STAY, 2)}:(c'={car+1}) & (p'={ped}) + {round(P_BRK_STAY*P_PED_FORW, 2)}:(c'={car}) & (p'={ped+1}) + {round(P_BRK_FORW*P_PED_FORW, 2)}:(c'={car+1}) & (p'={ped+1}); \n")
              
            elif car == 5 and ped == 5:
                filename.write(f"\t \t[] c={car} & p={ped} -> 1:(c'={car}) & (p'={ped}); \n")
    
            elif car == 5:
                filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_ACC_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_ACC_STAY*P_PED_FORW, 2)}: (c'={car}) & (p'={ped+1}); \n")
              
            elif ped == 5:
                filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_ACC_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_ACC_FORW*P_PED_STAY, 2)}: (c'={car+1}) & (p'={ped}); \n")
    
            else:
               filename.write(f"\t \t[] c={car} & p={ped} -> {round(P_ACC_STAY * P_PED_STAY, 2)}:(c'={car}) & (p'={ped}) + {round(P_ACC_FORW*P_PED_STAY, 2)}:(c'={car+1}) & (p'={ped}) + {round(P_ACC_STAY*P_PED_FORW, 2)}:(c'={car}) & (p'={ped+1}) + {round(P_ACC_FORW*P_PED_FORW, 2)}:(c'={car+1}) & (p'={ped+1}); \n")
        
                
                
    filename.write("\n endmodule")
    filename.close()

print(" = = = = = Done generating file = = = = =")
            
            

            