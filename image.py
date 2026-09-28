import streamlit as st
import google.generativeai as genai
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Receipt/Invoice Analyzer",
    page_icon="🧾",
    layout="wide"
)

st.title("🧾 Receipt/Invoice Analyzer")
st.write("Upload a image and get insights using Gemini 3.8 Flash.")

# -----------------------------
# Gemini API Configuration
# -----------------------------
GOOGLE_API_KEY = "AQ.Ab8RN6K1doV0nUz0QJcHhTmgCFHd6SmmM9Y54OTsGiEVwzh2FQ"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-3.8-flash")

# -----------------------------
# Image Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Analyze Button
# -----------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with col2:

        if st.button("Analyze Image"):

            with st.spinner("Analyzing image..."):

                prompt = """
                You are an AI document-analysis assistant specializing in receipts and invoices.

                Analyze the uploaded receipt or invoice and extract only information that is clearly visible.

                Extract:

                1. Business/store name
                2. Business address, if visible
                3. Date
                4. Time, if visible
                5. Invoice/receipt number
                6. Customer information, if visible
                7. Individual purchased items
                8. Quantity of each item
                9. Unit price
               10. Item total
               11. Subtotal
               12. Tax
               13. Discount
               14. Other charges
               15. Final amount
               16. Payment method, if visible

               Create a structured table for line items.

               Then check whether the visible arithmetic appears internally consistent.

               If any value is unclear:
               - Write "Not readable"
               - Do not guess.

               OUTPUT FORMAT:

               ## 🧾 Receipt/Invoice Summary

               | Field | Value |
               |---|---|
               | Business | |
               | Date | |
               | Receipt/Invoice Number | |
               | Customer | |
               | Payment Method | |

               ## 🛒 Purchased Items

               | Item | Quantity | Unit Price | Total |
               |---|---:|---:|---:|
               | | | | |

               ## 💰 Financial Summary

               | Description | Amount |
               |---|---:|
               | Subtotal | |
               | Discount | |
               | Tax | |
               | Other Charges | |
               | Final Amount | |

               ## 🔎 Verification
               ...

               IMPORTANT:
               Extract only visible information.
               Never invent missing values.
               Do not expose or infer sensitive information that is not clearly visible.
                """

                response = model.generate_content(
                    [prompt, image]
                )

                st.subheader("Analysis Result")
                st.write(response.text)
