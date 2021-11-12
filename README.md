# QAA: Query and Attention Augmentatio for Knowledge-Based Explainable Reasoning

https://anonymous.4open.science/r/QAA-32B8/

https://rb.gy/2bkxpy

### Scene Graph Generation Part
1. Download and unpack Visual Genome images as well as the annotations, class info and image meta-data
2. Get initial scene graph with [VCT](https://github.com/KaihuaTang/VCTree-Scene-Graph-Generation)
3. Next, run train_graph.py to train the scene graph generation
```
python train_graph.py --input_scene_dir <path/to/input/scene/dir> --output_scene_dir <path/to/output/scene/dir> 
```

### Query Augmentation and Training
1. Download Glove pretrained word vectors
2. Preprocess OK-VQA questions to obtain train_questions.pt and vocab.json
```
python preprocess_questions.py --glove_pt </path/to/generated/glove/pickle/file> --input_questions_json </your/path/to/v2_OpenEnded_mscoco_train2014_questions.json> --input_annotations_json </your/path/to/v2_mscoco_train2014_annotations.json> --output_pt </your/output/path/train_questions.pt> --vocab_json </your/output/path/vocab.json> --mode train
``` 
3. Download grounded features from paper Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering [repo](https://github.com/peteanderson80/bottom-up-attention)
4. Preprocess featurs
```
python preprocess_features.py --input_tsv_folder /your/path/to/trainval_36/ --output_h5 /your/output/path/trainval_feature.h5
```
5. Train the pretrained model
```
python train.py --input_dir <path/to/preprocessed/files> --save_dir </path/for/checkpoint> --val
```
6. Query Augmentation
```
python train.py --input_dir <path/to/preprocessed/files> --save_dir </path/for/checkpoint> --mode aug
```
7. Test
```
python train.py --input_dir <path/to/preprocessed/files> --save_dir </path/for/checkpoint> --mode test
```
