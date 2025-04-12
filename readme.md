# Fine Tuning of Vision Language Models using PEFT 

Parameter Efficient Fine Tuning(PEFT) has the following techniques :- <br>
- **Prompt Tuning** : Prepends a trainable tensor to the model's input embeddings, creating a soft prompt.
- **Prefix Tuning** : Learn task-specific vectors (prefixes) that are inserted into the key and value projections of each transformer layer.
- **Adapters** : Introduce small bottleneck neural networks (adapter modules) into each transformer layer.
- **Low Rank Composition** : Decomposes weight updates into low-rank matrices. We try to find the *Intrinsic Dimension(ID)* where a model achieves within 90% of the full parameter model performance. <br> 1) LoRA  &  2) QLoRA are two popular techniques. 
