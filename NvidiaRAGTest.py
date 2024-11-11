python3 -m virtualenv genai
source genai/bin/activate

pip install -r community/5_mins_rag_no_gpu/requirements.txt

export NVIDIA_API_KEY="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"

import streamlit as st
st.title("Progress")

