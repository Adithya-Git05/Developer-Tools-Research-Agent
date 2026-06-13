import streamlit as st
from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()
workflow = Workflow()

st.title("Developer Tools Research Agent")

query = st.text_input("Developer Tools Query", "")

if st.button("Run Research") and query:
    with st.spinner("Running research..."):
        result = workflow.run(query)

    st.subheader(f"Results for: {query}")

    for i, company in enumerate(result.companies, 1):
        st.markdown(f"### {i}. {company.name}")

        st.write(f"Website: {company.website}")
        st.write(f"Pricing Model: {company.pricing_model}")
        st.write(f"Open Source: {company.is_open_source}")

        if company.tech_stack:
            st.write(f"Tech Stack: {', '.join(company.tech_stack[:5])}")

        if company.language_support:
            st.write(
                f"Language Support: {', '.join(company.language_support[:5])}"
            )

        if company.api_available is not None:
            api_status = "Available" if company.api_available else "Not Available"
            st.write(f"API: {api_status}")

        if company.integration_capabilities:
            st.write(
                f"Integrations: {', '.join(company.integration_capabilities[:4])}"
            )

        if company.description and company.description != "Analysis failed":
            st.write(f"Description: {company.description}")

        st.divider()

    if result.analysis:
        st.subheader("Recommendations")
        st.write(result.analysis)
