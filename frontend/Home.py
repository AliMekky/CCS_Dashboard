import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="CCS Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: green; margin-top: 100px;'>CCS Dashboard</h1>", unsafe_allow_html=True)

def nav_page(page_name, timeout_secs=3):
    page_name_url = page_name.replace(' ', '_')
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elapsed = new Date() - start_time;
                if (elapsed < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name_url, timeout_secs)
    html(nav_script)

local_css("styles.css")

# First row with a single button in one column
col1 = st.columns(1)[0]  # Correctly access the first column

if col1.button("About CCS"):
    nav_page("About_CCS")
