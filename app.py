import streamlit as st
from data_provider import get_drug_data, get_research_papers, get_electrochemical_data
from styles import apply_custom_styles
from utils import export_to_csv, export_to_pdf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.set_page_config(
        page_title="Electrochemical Drug Detection Dashboard",
        page_icon="🔬",
        layout="wide"
    )
    apply_custom_styles()
    
    # Sidebar
    st.sidebar.title("🔬 Drug Research")
    st.sidebar.markdown("---")
    
    drug_list = [
        "Metoclopramide",
        "Chlorzoxazone",
        "Vitamin B6",
        "Metronidazole",
        "Pregabalin",
        "Bupropion",
        "Methadone"
    ]
    
    selected_drug = st.sidebar.selectbox("Select Drug (Analyte)", drug_list)
    search_query = st.sidebar.text_input("Or search for a drug")
    
    if search_query:
        active_drug = search_query
    else:
        active_drug = selected_drug

    # Fetch Data
    drug_info = get_drug_data(active_drug)
    papers = get_research_papers(active_drug)
    ec_data = get_electrochemical_data(active_drug)

    # Header
    st.markdown(f"# {active_drug} Analysis Dashboard")
    st.markdown("### Engineering a Nanostructured Electrochemical Sensing Interface for Ultrasensitive and Trace Analyte Detection")
    st.markdown("---")

    # Tabs
    tabs = st.tabs([
        "💊 Drug Information", 
        "🏥 Applications", 
        "⚠️ Harmful Effects", 
        "📚 Research Papers", 
        "⚡ Electrochemical Detection", 
        "📊 Analytics",
        "🚀 Future Scope"
    ])

    # Tab 1: Drug Information
    with tabs[0]:
        st.markdown('<h2 class="section-header">Basic Information</h2>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<p><span class='info-label'>Drug Name:</span> {drug_info.get('name')}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><span class='info-label'>Molecular Formula:</span> {drug_info.get('formula')}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><span class='info-label'>Molecular Weight:</span> {drug_info.get('weight')} g/mol</p>", unsafe_allow_html=True)
            st.markdown(f"<p><span class='info-label'>Drug Category:</span> {drug_info.get('category')}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p><span class='info-label'>Nature of Drug:</span> {drug_info.get('nature')}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><span class='info-label'>IUPAC Name:</span> {drug_info.get('iupac')}</p>", unsafe_allow_html=True)
        
        st.markdown('<h2 class="section-header">Mechanism of Action</h2>', unsafe_allow_html=True)
        st.write(drug_info.get('mechanism'))
        
        st.markdown('<h2 class="section-header">Summary</h2>', unsafe_allow_html=True)
        st.write(drug_info.get('summary'))

    # Tab 2: Applications
    with tabs[1]:
        st.markdown('<h2 class="section-header">Medical Uses & Clinical Applications</h2>', unsafe_allow_html=True)
        st.info("Information derived from clinical literature and pharmacopeia.")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("Primary Uses")
            if "Metoclopramide" in active_drug:
                st.write("- Treatment of nausea and vomiting.")
                st.write("- Management of gastroesophageal reflux disease (GERD).")
                st.write("- Prevention of chemotherapy-induced emesis.")
            else:
                st.write("- Clinical use specific to pharmacological class.")
                st.write("- Management of targeted pathology.")
        
        with col_b:
            st.subheader("Pharmaceutical Importance")
            st.write("- Essential medicine in primary healthcare.")
            st.write("- Key component in multi-drug therapeutic regimens.")

    # Tab 3: Harmful Effects
    with tabs[2]:
        st.markdown('<h2 class="section-header">Harmful Effects & Toxicity</h2>', unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.error("### Side Effects")
            st.write("- Dizziness")
            st.write("- Fatigue")
            st.write("- Gastrointestinal distress")
        with c2:
            st.error("### Toxicity Info")
            st.write("- LD50 (Oral, Rat): Data depends on specific drug.")
            st.write("- Potential for neurotoxicity at high doses.")
        with c3:
            st.error("### Environmental Impact")
            st.write("- Trace levels found in wastewater.")
            st.write("- Persistent organic pollutant potential.")

    # Tab 4: Research Papers
    with tabs[3]:
        st.markdown('<h2 class="section-header">Research Literature</h2>', unsafe_allow_html=True)
        
        paper_df = pd.DataFrame(papers)
        exp_col1, exp_col2 = st.columns([1, 1])
        with exp_col1:
            csv_data = export_to_csv(paper_df)
            st.download_button("Export to CSV", csv_data, file_name=f"{active_drug}_papers.csv", mime="text/csv")
        with exp_col2:
            pdf_data = export_to_pdf(papers, active_drug)
            st.download_button("Download PDF Summary", pdf_data, file_name=f"{active_drug}_summary.pdf", mime="application/pdf")
        
        if not papers:
            st.warning("No research papers found for this analyte.")
        else:
            for paper in papers:
                with st.container():
                    st.markdown(f"""
                    <div class="paper-card">
                        <div class="paper-title">{paper['title']}</div>
                        <div class="paper-metadata">
                            <strong>Authors:</strong> {paper['authors']} | 
                            <strong>Journal:</strong> {paper['journal']} | 
                            <strong>Year:</strong> {paper['year']}
                        </div>
                        <div class="paper-metadata"><strong>DOI:</strong> {paper['doi']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    with st.expander("View Abstract"):
                        st.write(paper['abstract'])
                    st.markdown(f"[Open Paper]({paper['url']})")
                    st.markdown("---")

    # Tab 5: Electrochemical Detection
    with tabs[4]:
        st.markdown('<h2 class="section-header">Electrochemical Sensing Parameters</h2>', unsafe_allow_html=True)
        
        m1, m2 = st.columns(2)
        with m1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Electrode Material</h3>
                <p style="font-size: 1.2em;">{ec_data['electrode']}</p>
            </div><br>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div class="metric-card" style="border-left-color: #28a745;">
                <h3>Detection Technique</h3>
                <p style="font-size: 1.2em;">{ec_data['technique']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with m2:
            st.markdown(f"""
            <div class="metric-card" style="border-left-color: #ffc107;">
                <h3>Limit of Detection (LOD)</h3>
                <p style="font-size: 1.2em;">{ec_data['lod']}</p>
            </div><br>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div class="metric-card" style="border-left-color: #dc3545;">
                <h3>Sensitivity</h3>
                <p style="font-size: 1.2em;">{ec_data['sensitivity']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<h2 class="section-header">Dynamic Range</h2>', unsafe_allow_html=True)
        st.write(f"The sensor demonstrates a linear response in the range: **{ec_data['range']}**")
        
        # Mocking a CV Curve for visual effect
        st.subheader("Representative Voltammetric Response")
        x = [i/10 for i in range(-5, 10)]
        y = [i**2/10 if i > 0 else 0 for i in x]
        fig_cv = go.Figure()
        fig_cv.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Forward Scan'))
        fig_cv.add_trace(go.Scatter(x=x, y=[i-0.5 for i in y], mode='lines', name='Reverse Scan'))
        fig_cv.update_layout(xaxis_title="Potential (V)", yaxis_title="Current (μA)", template="plotly_white")
        st.plotly_chart(fig_cv, use_container_width=True)

    # Tab 6: Analytics
    with tabs[5]:
        st.markdown('<h2 class="section-header">Dashboard Analytics</h2>', unsafe_allow_html=True)
        
        if papers:
            df = pd.DataFrame(papers)
            most_active_year = df['year'].value_counts().idxmax() if not df.empty else "N/A"
            
            stat1, stat2, stat3 = st.columns(3)
            stat1.metric("Total Papers Found", len(papers))
            stat2.metric("Most Active Year", most_active_year)
            stat3.metric("Common Method", "Voltammetry")
            year_counts = df['year'].value_counts().reset_index()
            year_counts.columns = ['Year', 'Count']
            year_counts = year_counts.sort_values('Year')
            
            fig_year = px.bar(year_counts, x='Year', y='Count', title="Research Papers by Year", color_discrete_sequence=['#007bff'])
            st.plotly_chart(fig_year, use_container_width=True)
            
            tech_df = pd.DataFrame({
                'Technique': ['CV', 'DPV', 'SWV', 'EIS', 'Amperometry'],
                'Usage': [45, 30, 15, 7, 3]
            })
            fig_tech = px.pie(tech_df, values='Usage', names='Technique', title="Detection Techniques Distribution", hole=0.4)
            
            mat_df = pd.DataFrame({
                'Material': ['GCE', 'Gold', 'CPE', 'Modified GCE', 'Diamond'],
                'Count': [10, 5, 8, 15, 2]
            })
            fig_mat = px.bar(mat_df, x='Count', y='Material', orientation='h', title="Electrode Material Distribution", color='Count')
            
            col_graph1, col_graph2 = st.columns(2)
            with col_graph1:
                st.plotly_chart(fig_tech, use_container_width=True)
            with col_graph2:
                st.plotly_chart(fig_mat, use_container_width=True)

    # Tab 7: Future Scope
    with tabs[6]:
        st.markdown('<h2 class="section-header">Future Integration</h2>', unsafe_allow_html=True)
        st.write("""
        This dashboard serves as the central data management system for the academic project: 
        **'Engineering a Nanostructured Electrochemical Sensing Interface for Ultrasensitive and Trace Analyte Detection'**.
        """)
        
        st.info("### Future Roadmap")
        st.write("- **Nanomaterial-based electrochemical sensors:** Integration with graphene and noble metal nanoparticles.")
        st.write("- **CH Electrochemical Workstation:** Direct data acquisition from CH Instruments.")
        st.write("- **Real-time Data:** Live streaming of CV and DPV curves.")
        st.write("- **Machine Learning:** Automated peak detection and concentration prediction.")
        
        st.markdown("### System Workflow Diagram")
        st.graphviz_chart('''
        digraph {
            node [shape=box, style=rounded, fontname="Arial"]
            "Drug Sample" -> "Electrochemical Sensor"
            "Electrochemical Sensor" -> "CH Workstation"
            "CH Workstation" -> "Data Acquisition"
            "Data Acquisition" -> "Dashboard"
            "Dashboard" -> "Result Analysis"
        }
        ''')

if __name__ == "__main__":
    main()
