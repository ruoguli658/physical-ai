"""Phase 0 test job: proves the GPU works end to end (submit -> log -> retrieve output)."""
import json
import os
import socket
import time

import torch

info = {
    "host": socket.gethostname(),
    "torch_version": torch.__version__,
    "cuda_available": torch.cuda.is_available(),
}

if torch.cuda.is_available():
    dev = torch.device("cuda")
    info["gpu_name"] = torch.cuda.get_device_name(0)
    info["gpu_count"] = torch.cuda.device_count()

    # Time a large matrix multiply so you see the GPU doing real work
    a = torch.randn(8192, 8192, device=dev)
    b = torch.randn(8192, 8192, device=dev)
    torch.cuda.synchronize()
    t0 = time.time()
    for _ in range(10):
        c = a @ b
    torch.cuda.synchronize()
    dt = time.time() - t0
    tflops = 10 * 2 * 8192**3 / dt / 1e12
    info["matmul_tflops_fp32"] = round(tflops, 2)

print(json.dumps(info, indent=2))

# Write a result file so you also practise retrieving output
with open(f'gpu_test_result_{os.environ.get("SLURM_JOB_ID", "local")}.json', 'w') as f:
    json.dump(info, f, indent=2)
