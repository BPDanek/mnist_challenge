{
  "_comment": "===== MODEL CONFIGURATION =====",
  "model_dir": "/Users/BenjaminDanek/PycharmProjects/DAAA-designinformatics/DAAA-designinformatics-master/model_dir",

  "_comment": "===== TRAINING CONFIGURATION =====",
  "random_seed": 4557077,
  "max_num_training_steps": 100000,
  "num_output_steps": 100,
  "num_summary_steps": 100,
  "num_checkpoint_steps": 300,
  "training_batch_size": 50,

  "_comment": "===== EVAL CONFIGURATION =====",
  "num_eval_examples": 10000,
  "eval_batch_size": 200,
  "eval_on_cpu": true,

  "_comment": "=====ADVERSARIAL EXAMPLES CONFIGURATION=====",
  "epsilon": 0.3,
  "k": 40,
  "a": 0.01,
  "random_start": true,
  "loss_func": "xent",
  "store_adv_path": "attack.npy"
}
