# train a miniature character-level Python-code BabyGPT
# SEEM3650 Practical Exam, Step 4

out_dir = 'out-code-generation'
eval_interval = 500
eval_iters = 100
log_interval = 10

always_save_checkpoint = False

wandb_log = False
wandb_project = 'code-generation'
wandb_run_name = 'baby-code-gpt'

dataset = 'code_generation'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256

n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.1

learning_rate = 1e-3
max_iters = 2000
lr_decay_iters = 2000
min_lr = 1e-4
beta2 = 0.99

warmup_iters = 100
