import streamlit as st
import helper
import pickle

# Load trained model
model = pickle.load(open('rf.pkl', 'rb'))

st.set_page_config(page_title="Duplicate Question Checker", page_icon="❓")
st.title("🔍 Duplicate Question Pairs Detection")

# User input
q1 = st.text_input('✏️ Enter Question 1')
q2 = st.text_input('✏️ Enter Question 2')

if st.button('Find'):
    if not q1 or not q2:
        st.warning("⚠️ Please enter **both questions** before submitting.")
    else:
        # Create query point
        query = helper.query_point_creator(q1, q2)
        
        # Prediction
        result = model.predict(query)[0]
        # probability of being duplicate
        proba = model.predict_proba(query)[0][1]  
        
        # Show results
        if result:
            st.success(f"✅ These questions are likely **Duplicate**")
        else:
            st.error(f"❌ These questions are **Not Duplicate**")
        
        st.write(f"**Confidence Score:** {proba:.2f}")
