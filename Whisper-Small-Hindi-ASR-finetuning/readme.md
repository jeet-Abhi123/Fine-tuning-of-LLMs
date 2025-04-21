# Hindi ASR using OpenAI Whisper

**Dataset** : SpringLab Hindi TTS : [Click Here](https://huggingface.co/datasets/SPRINGLab/IndicTTS-Hindi)

**Metric Used** : WER(Word Error Rate) <br>
- This Formula is derived from **Levenshtein distance**. <br>
- WER = (S + D + I) / N = (S + D + I) / (S + D + C) <br>

Here, S --> no. of Substitution,  D --> no. of Deletions, I --> no. of Insertions <br> 
C --> no. of correct words, N --> no. of words in the reference (N=S+D+C) <br>

The average number of errors per reference word is indicated by this value.  With a WER of 0 representing a perfect score, the lower the number, the better the ASR system performs.
