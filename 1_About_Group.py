import streamlit as st

st.title("About the Group")
st.write("This page provides information about the group members.")

group_members = [
    {"Name": "Alice", "Role": "Leader", "Email": "alice@example.com"},
    {"Name": "Bob", "Role": "Developer", "Email": "bob@example.com"},
    {"Name": "Charlie", "Role": "Tester", "Email": "charlie@example.com"},
]

for member in group_members:
    st.subheader(member["Name"])
    st.write(f"**Role:** {member['Role']}")
    st.write(f"**Email:** {member['Email']}")
    st.write("---")