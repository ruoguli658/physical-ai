# Results log

One entry per experiment, written the same day. The "Learned" line is the one that becomes CV numbers and interview stories.

Template:
## YYYY-MM-DD — short title (Phase N)
- Ran:
- Result:
- Learned:
- Next:

---

## 2026-10-17 — GPU test jobs (Phase 0)
- Ran: gpu_test.py on 4 GPU types (A100, H100, H200, L40S), embers queue. H200 finished (job 14142142); A100, H100, L40S still pending.
- Result: H200 works end to end. CUDA available, PyTorch 2.14.1+cu130, 23.6 TFLOPS FP32 (under-measured: no warm-up, plain FP32). Run time 8 s, ~1 GB RAM used of 16 GB requested.
- Learned: 
- Next: add warm-up + BF16 measurement to gpu_test.py; compare all 4 GPU types once the pending jobs finish; pip install numpy in pai env.
