# Video Action Recognition

## Dataset: EPIC-KICHENS-100
[Official site](https://epic-kitchens.github.io/2022)

[Annotations](https://github.com/epic-kitchens/epic-kitchens-100-annotations#epic_100_validationcsv)

[Dataset download](https://github.com/epic-kitchens/epic-kitchens-download-scripts)

<br />

## EPIC-KITCHENS Action Recognition Baselines:
1. [Results Evaluation](https://github.com/epic-kitchens/C1-Action-Recognition)
2. [Pretrained state-of-the-art](https://github.com/epic-kitchens/C1-Action-Recognition-TSN-TRN-TSM) (Data prepation, training, testing, etc. )

<br />

## Instruction and Tips
1. Download: Use arguments like `--rgb-frames` to specify modality, split, and challenge.
2. Extraction: Use script provided in `scripts/extract_frames.py` to generate organized folders and extract compressed files into it.
3. Data gulping: Use scripts provided by official repo.
4. Training: Follow [instruction](https://github.com/epic-kitchens/C1-Action-Recognition-TSN-TRN-TSM#training), make modifications to `../config/*.yaml` file and the correspoding bash command argument when needed.
5. Testing: Follow [instruction](https://github.com/epic-kitchens/C1-Action-Recognition-TSN-TRN-TSM#testing), make modifications the correspoding bash command argument when needed. **Note: Use `scripts/test.py`, in which a bug is fixed and will not produce corrupted results file.**
6.  Evaluation: Follow [instruction](https://github.com/epic-kitchens/C1-Action-Recognition), it is done on the validation set.
7. Put `scripts/launch.json` in `.vscode` file under the project root directory, for remote debugging. A [documentation](https://code.visualstudio.com/docs/python/debugging) is provided.
8. Put `scripts/settings.json` in `.vscode` file under the project root directory, if facing any issue regarding python package import.

## Some Commands
### Training:  
>
>`(epic-models) ~/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM$`  
>
>`nohup python3 -u src/train.py --config-name tsm_rgb data._root_gulp_dir=/home/students/s121md105_01/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM data.worker_count=$(nproc) learning.batch_size=64 trainer.gpus=4 hydra.run.dir=models/train_from_raw/experiment-1 > training_experiment_1.log 2>&1 &`  

<br>

### Gulp:  
>
>`(base) ~/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM$`  
>
>`nohup python3 -u src/gulp_data.py /home/students/s121md105_01/EPIC-KITCHENS-Data rgb_val /home/students/s121md105_01/EPIC-KITCHENS/epic-kitchens-100-annotations/EPIC_100_validation.pkl rgb > gulp_val.log 2>&1 &`  

<br>

### Test for pre-trained models:  
>
>`(epic-models) ~/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM$`  
>
>`python3 src/test.py /home/students/s121md105_01/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM/models/pretrained/tsm_rgb.ckpt /home/students/s121md105_01/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM/models/results/tsm_rgb_val_results_version.pt --split val`  

<br>

### Test for pre-trained models:  
>
>`(epic-models) ~/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM$`  
>
>`python3 src/test.py /home/students/s121md105_01/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM/models/pretrained/tsm_rgb.ckpt /home/students/s121md105_01/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM/models/results/tsm_rgb_val_results_version.pt --split val`

<br>

### Test for train-from-scatch models:  
>
>`(epic-models) ~/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM$`  
>
>`python3 src/test.py /home/students/s121md105_01/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM/models/train_from_raw/experiment-1/lightning_logs/version_6/checkpoints/epoch\=79-step\=168079.ckpt /home/students/s121md105_01/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM/models/train_from_raw/experiment-1/tsm_rgb_val_results.pt --split val`

<br>

### Evaluation:  
>
>`(epic-models) ~/EPIC-KITCHENS/C1-Action-Recognition$`  
>
>`python3 evaluate.py /home/students/s121md105_01/EPIC-KITCHENS/C1-Action-Recognition-TSN-TRN-TSM/models/train_from_raw/experiment-1/tsm_rgb_val_results.pt /home/students/s121md105_01/EPIC-KITCHENS/epic-kitchens-100-annotations/EPIC_100_validation.pkl --tail-verb-classes-csv /home/students/s121md105_01/EPIC-KITCHENS/epic-kitchens-100-annotations/EPIC_100_tail_verbs.csv --tail-noun-classes-csv /home/students/s121md105_01/EPIC-KITCHENS/epic-kitchens-100-annotations/EPIC_100_tail_nouns.csv --unseen-participant-ids /home/students/s121md105_01/EPIC-KITCHENS/epic-kitchens-100-annotations/EPIC_100_unseen_participant_ids_validation.csv >evaluation_result.log`

<br>
