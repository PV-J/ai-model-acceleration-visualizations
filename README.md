AI Model Acceleration Visualization & Minimalist Pipeline
This repository hosts Python code snippets demonstrating performance visualizations and a minimalist AI pipeline integrating image processing with large language models (LLMs). These complement the blog post "Accelerate AI Model Speed; Python Minimalist!".

Overview
Visualization scripts: Generate charts showing inference latency, throughput improvements, and memory usage comparing FP32 vs FP16.

Minimal AI pipeline: A modular, clean Python prototype showing how to chain image loading, preprocessing, feature extraction, and language model querying — all designed for clarity and compact one-liners.

Contents

File                          |  Description                                              
------------------------------+-----------------------------------------------------------
inference_latency_cpu_gpu.py  |  Bar chart comparing CPU vs GPU inference latency         
throughput_vs_batch_size.py   |  Line plot showing throughput scalability with batch sizes
memory_usage_fp32_fp16.py     |  Bar chart comparing FP32 and FP16 memory usage           
minimal_ai_pipeline.py        |  Minimalist prototype pipeline for image + LLM processing 

Usage Instructions
Clone the repository:

bash
git clone https://github.com/PV-J/ai-model-acceleration-visualizations.git
cd ai-model-acceleration-visualizations

Install dependencies:

bash
pip install matplotlib seaborn pandas pillow torch transformers

Run any visualization script to generate PNG charts locally:

bash
python inference_latency_cpu_gpu.py
python throughput_vs_batch_size.py
python memory_usage_fp32_fp16.py

Experiment with the minimalist pipeline:

bash
python minimal_ai_pipeline.py
This runs a sample image through loading, preprocessing, feature extraction, and LLM caption generation in a concise chained manner.

Contributing
Contributions, bug fixes, and suggestions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.


