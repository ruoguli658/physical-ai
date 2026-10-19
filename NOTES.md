# Setup notes

Facts and fixes needed again. When you solve a problem, write the fix here.

## PACE (Phoenix)
- Login: `ssh rli658@login-phoenix.pace.gatech.edu` (GT VPN needed off campus)
- Charge account: `gts-aalexeev3-afrench` (check with `pace-quota`)
- Queue (QOS): `embers` = free, can be preempted; `inferno` = charges the account, not preempted
- GPU partitions seen: `gpu-h200` (H200, 141 GB)
- Choose GPU type at submit time: `sbatch --gres=gpu:h100:1 gpu_test.sbatch`
- **Avoid V100**: the pai env's PyTorch is built for CUDA 13, which dropped Volta support

## Conda env
- Name: `pai`, Python 3.10
- Location: `/storage/home/hcoda1/3/rli658/.conda/envs/pai`
- Installed: torch 2.14.1+cu130
- To do: `pip install numpy`, `pip install wandb`

## Job commands
- Submit: `sbatch gpu_test.sbatch`
- Check queue: `squeue -u $USER` (PD = pending, R = running)
- Estimated start time: `squeue -u $USER --start`
- Read log: `cat gpu_test-<jobid>.out`

## Fixes that worked
- `conda activate` inside a job script: add `eval "$(conda shell.bash hook)"` before it
- Log warning "No module named 'numpy'": harmless for the test, but install numpy in pai

## Queue wait times (embers)
| GPU | Submitted | Started | Wait |
|---|---|---|---|
| H200 | 2026-10-17 | 2026-10-17 18:10 | |
| A100 | 2026-10-17 | pending | |
| H100 | 2026-10-17 | pending | |
| L40S | 2026-10-17 | pending | |
