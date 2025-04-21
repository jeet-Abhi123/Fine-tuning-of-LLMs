# Hindi ASR using OpenAI Whisper

**Dataset** : SpringLab Hindi TTS : [Click Here](https://huggingface.co/datasets/SPRINGLab/IndicTTS-Hindi)

**Note** : I have used L4 GPU for training the model. These models require a lot of GPU memory. So you can use Google Colab or any other cloud service to train the model. I used Lightning AI cloud platform for training the model. Lightning AI provides some free credits to train on some good GPU's. [Lighting AI](https://lightning.ai/)

**Metric Used** : WER(Word Error Rate) <br>
- This Formula is derived from **Levenshtein distance**. <br>
- WER = (S + D + I) / N = (S + D + I) / (S + D + C) <br>

Here, S --> no. of Substitution,  D --> no. of Deletions, I --> no. of Insertions <br> 
C --> no. of correct words, N --> no. of words in the reference (N=S+D+C) <br>

The average number of errors per reference word is indicated by this value.  With a WER of 0 representing a perfect score, the lower the number, the better the ASR system performs.

### Results 💯🚀🎯

| Ground Truth  | Whisper Base  |
| ------------- | ------------- |
| क्योंकि उनका मन जो आप भी जानते हैं कि छोटे बच्चे रहते हैं चंचल बच्चे होते हैं  | चुकि उनका मन जो आप बी जानती है कि छूटे वच्चे रखते हैं, चन्जर वच्य होते.  |
