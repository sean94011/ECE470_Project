# ECE470_Project

## Installation & Setup
```sh
git clone https://github.com/sean94011/ECE470_Project.git

cd catkin_final_project/src

catkin_init_workspace

cd..

catkin_make
```

## Run the Project
```sh
cd catkin_final_project

source devel/setup.bash

catkin_make

roslaunch ur3_driver ur3_gazebo.launch
```
* Now open another new command prompt with "crtl+shift+N"
```sh
cd catkin_final_project/src/projectandDriver/project_py/scripts/

chmod +x project_exec.py

rosrun lab2pkg_py project_exec.py --simulator True
```

## Run Chemprop
* Go to Chemprop and activate the environment
```sh
cd <path/to/chemprop>

source/conda activate chemprop
```
* Directly Train with Class Balancing
```sh
python train.py --data_path </path/to/Moleculenet/data/ecoli.csv> --dataset_type classification --save_dir ecoli_checkpoints --class_balance
```
* Hyperparameter Optimization First and then Train
```sh
python hyperparameter_optimization.py --data_path </path/to/Moleculenet/data/ecoli.csv> --dataset_type classification --num_iters 100 --config_save_path config_ecoli

python train.py --data_path </path/to/Moleculenet/data/ecoli.csv> --dataset_type classification --config_path config_ecoli
```
* Prediction on Library with Trained Model
```sh
python predict.py --test_path <path/to/library> --checkpoint_dir ecoli_checkpoints --preds_path ecoli_preds.csv
```
