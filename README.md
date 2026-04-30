# SEEM3650 Practical Exam - BabyGPT with nanoGPT

This repository is the GitHub-ready submission for the SEEM3650 Practical Exam.

## Student information

- Student ID: 1155213983
- Last three digits: 983
- XYZ mod 4: 3
- XYZ mod 2: 1

## Summary

This project uses [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) to train small character-level BabyGPT models.

- Step 2 trains the default Shakespeare character-level model with nanoGPT's literal default settings (`max_iters=5000`, `eval_interval=250`, `eval_iters=200`).
- Step 3 fixes `n_head = 4`, varies `n_layer` over `[2, 3, 5, 7]`, and plots loss at iteration 750. PDF Step 3.2 explicitly allows reducing the iteration target when training is too slow, kept consistent across all four runs.
- Step 4 builds a Python code corpus, creates `config/train_code_generation.py`, trains a code-generation BabyGPT model, and records generated code samples.

## Repository layout

```text
.
|-- README.md                                # this file
|-- NANOGPT_README.md                        # original nanoGPT README, kept for reference
|-- LICENSE                                  # nanoGPT MIT License
|-- .gitignore
|-- report.md                                # Step 2 / Step 3 / Step 4 results and discussion
|-- SEEM3650_Practical_Exam.ipynb            # end-to-end Kaggle notebook
|-- train.py                                 # nanoGPT core
|-- sample.py
|-- model.py
|-- configurator.py
|-- bench.py
|-- config/
|   |-- train_shakespeare_char.py            # nanoGPT default
|   |-- train_shakespeare_char_l2_h4.py      # Step 3 variant
|   |-- train_shakespeare_char_l3_h4.py      # Step 3 variant
|   |-- train_shakespeare_char_l5_h4.py      # Step 3 variant
|   |-- train_shakespeare_char_l7_h4.py      # Step 3 variant
|   `-- train_code_generation.py             # Step 4 config
|-- data/
|   |-- shakespeare_char/
|   |   |-- prepare.py
|   |   `-- input.txt
|   `-- code_generation/
|       |-- prepare.py
|       `-- input.txt                        # >= 100,000 character-level tokens
|-- figures/
|   |-- loss_vs_layers.png                   # Step 3 main plot
|   `-- val_loss_curves.png                   # bonus learning curves
`-- samples/
    |-- shakespeare_char_full.txt
    |-- shakespeare_char_first5.txt
    |-- code_generation_full.txt
    |-- code_generation_first20.txt
    `-- code_generation_favourite.txt
```

## Key results

- Best Step 3 setting: layers = 7, heads = 4, validation loss = 1.6265
- Code corpus size: 572,125 character-level tokens
- Code-generation final validation loss: 1.6525

## Reproduce on Kaggle

1. Upload and open `SEEM3650_Practical_Exam.ipynb` on Kaggle.
2. Enable Internet.
3. Select GPU T4 x1.
4. Run all cells.
5. Download `/kaggle/working/seem3650-practical-exam.zip`.

## Reproduce locally

```bash
pip install torch numpy transformers datasets tiktoken wandb tqdm

# Step 2: Shakespeare character-level model
python data/shakespeare_char/prepare.py
python train.py config/train_shakespeare_char.py --device=cuda --compile=False
python sample.py --out_dir=out-shakespeare-char --device=cuda --num_samples=2 --max_new_tokens=500

# Step 3: re-run any layer variant produced by the notebook
python train.py config/train_shakespeare_char_l5_h4.py --device=cuda --compile=False

# Step 4: code-generation BabyGPT
python data/code_generation/prepare.py
python train.py config/train_code_generation.py --device=cuda --compile=False
python sample.py --out_dir=out-code-generation --device=cuda --num_samples=3 --max_new_tokens=800 --start="def "
```

Replace `--device=cuda` with `--device=cpu` and add `--max_iters=2000 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --dropout=0.0` if you only have a CPU machine.

## Recommended GitHub metadata

Suggested About description:

```text
SEEM3650 Practical Exam: BabyGPT training with nanoGPT on Shakespeare and open-source Python code, including architecture exploration and code generation samples.
```

Suggested topics:

```text
nanogpt, gpt, babygpt, transformer, language-model, character-level, shakespeare, code-generation, pytorch, kaggle, seem3650, data-analytics
```
