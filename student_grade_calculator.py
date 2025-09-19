# student_grade_calculator.py

import streamlit as st

# --- Grade calculation logic ---
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# --- App layout ---
st.set_page_config(page_title="Student Grade Calculator", layout="centered")
st.title("📘 Student Grade Calculator")
st.info("Enter the number of students and their scores below, then click Submit to calculate grades.")

# --- Input section ---
st.subheader("Enter Student Details")
num_students = st.number_input("How many students?", min_value=1, max_value=50, step=1)

students = []

with st.form("grade_form"):
    for i in range(int(num_students)):
        st.markdown(f"**Student {i+1}**")
        name = st.text_input(f"Name {i+1}", key=f"name_{i}")
        score = st.number_input(f"Score {i+1}", min_value=0, max_value=100, key=f"score_{i}")
        if name:
            grade = calculate_grade(score)
            students.append({"Name": name, "Score": score, "Grade": grade})
    submitted = st.form_submit_button("Submit")

# --- Display results ---
if submitted and students:
    st.subheader("📋 Results")
    for student in students:
        st.write(f"**{student['Name']}** — Score: {student['Score']} → Grade: **{student['Grade']}**")

    # --- Grade summary ---
    st.subheader("📊 Grade Summary")
    grade_counts = {}
    for student in students:
        grade = student["Grade"]
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    for grade, count in sorted(grade_counts.items()):
        st.write(f"Grade {grade}: {count} student(s)")
