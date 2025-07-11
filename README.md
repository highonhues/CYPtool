## CYPTOOL

A Streamlit web-app that predicts a patient’s **CYP2C19 metabolizer status** (Ultra, Rapid, Normal, Intermediate, or Poor Metabolizer) using allele data and clinical risk factors.

### Live Demo

**[Click here](http://ec2-54-151-0-232.us-west-1.compute.amazonaws.com:8501/)** to launch the hosted app in your browser.

### Quickstart with Docker

```bash
git clone https://github.com/highonhues/CYPtool.git
cd CYPtool
docker build -t cyp2c19-app .
docker run -p 8501:8501 cyp2c19-app
```

### Quickstart with Python

```python
git clone https://github.com/highonhues/CYPtool.git
cd CYPtool
python -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt
streamlit run app.py
```
