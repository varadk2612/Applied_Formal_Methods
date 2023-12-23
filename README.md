# Final Project

This Repository contains code to run Probabilistic Model Checking using the Prism Model Checker. It contains two traffic scenarios modeled as Markov Decision Processes (MDPs) along with some LTL specifications for overall system behavior.

Ways to run the code in this repo
1. Running code in VSCode
    - clone this repo
    - Open it in VSCode. VSCode will prompt you to open it as a devcontainer
    - Click "open in devcontainer" and you will have the environment setup
2. Through the terminal
    - clone this repo
    - Navigate to the top level of this directory and cd into `.devcontainer` and run `docker build .`
    - This will take a few minutes and create a docker image
    - To run this, use the command `docker exec -it -v <mount our repo> <image id>`
        - `image id` can be found using `docker image list` 
        - you will have to mount our repo into the devcontainer using `-v <path in container>:<path of dir to mount on host>`. Alternatively, you can run it without mounting our repo and you'll clone it inside the container. If you don't wish to persist changes you made, that is the way to do it. 

### Generating heatmaps
- These instructions apply to generate a heatmap for the car-pedestrian where we generated our own policy
1. Open the file `car_ped_analysis.py`
2. Update variable `prop to check` on line 7 with the proposition you wish to try
3. Ensure the line 38 `plt.savefig('car_ped_noColl_reach_heatmap.png')` is not commented. You can change the name of the file. 

### Generating a PRISM file using a python generator script
- This script is used to generate PRISM code that implements the policy break - c1p3, c2p2, c2p3, c2p4; acce;erate - otherwise; The constituent probabilities. We can run either of the below files 
- `python3 car_ped_parallelcomposition_generator.py` which generates `car_ped_parallelcomposition.prism`
- `python3 car_ped_parallelcomposition_policy_generator.py` which generates `car_ped_parallelcomposition_policy.prism`

### Running analysis on a given PRISM file
- `prism <PRISM FILE.prism> <SPECS_FILE.specs> -exportstrat stdout > turn_auto.out`
- `prism <PRISM FILE.prism> <PLAINTEXT SPEC> -exportstrat stdout > turn_auto.out` where `<PLAINTEXT SPEC>` can be `F (c=3 & p=3)` or something of that form

### # Applied_Formal_Methods
