import streamlit as st
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import numpy as np

FILE = "expenses.csv"

# Load data
def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

# Save data
def save_data(df):
    df.to_csv(FILE, index=False)
    


st.markdown("<h1 style='text-align:center;'>💸 Smart Expense Tracker</h1>", unsafe_allow_html=True)
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #dcdcdc;  /* light grey */
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📊 Menu")
st.caption("Track your daily expenses and manage your budget efficiently")
st.sidebar.markdown("Manage your daily expenses easily")

menu = st.sidebar.selectbox("Menu", ["Add Expense", "View Expenses", "Summary","Chatbot"])


df = load_data()

# 👇 YAHAN ADD KARO
if df.empty:
    sample_data = pd.DataFrame([
        ["2026-03-20", "Food", 120, "Lunch"],
        ["2026-03-21", "Travel", 50, "Bus fare"],
        ["2026-03-22", "Study", 300, "Books"],
        ["2026-03-23", "Other", 200, "Stationery"]
    ], columns=df.columns)
    
    df = sample_data
    
    save_data(df)

# ---------------- ADD EXPENSE ----------------
if menu == "Add Expense":
    st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f", use_column_width=True)
    
    st.subheader("Add New Expense")

    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Travel", "Study", "Other"])
    amount = st.number_input("Amount", min_value=0.0)
    description = st.text_input("Description")

    if st.button("Add"):
        new_data = pd.DataFrame([[date, category, amount, description]],
                                columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        save_data(df)
        st.success("Expense Added Successfully!")

# ---------------- VIEW EXPENSE ----------------
elif menu == "View Expenses":
    st.image("https://images.unsplash.com/photo-1556745757-8d76bdb6984b", use_column_width=True)
    if st.button("Clear All Data"):
        df = df.iloc[0:0]
        save_data(df)
        st.warning("All data cleared!")
    st.subheader("All Expenses")

    if not df.empty:
        search = st.selectbox("Filter by Category", ["All"] + list(df["Category"].unique()))

        if search != "All":
            filtered_df = df[df["Category"] == search]
        else:
            filtered_df = df

        st.dataframe(filtered_df)
        st.dataframe(df)

        if st.button("Delete Last Entry"):
            df = df.iloc[:-1]
            save_data(df)
            st.warning("Last entry deleted")
    else:
        st.info("No data available")

# ---------------- SUMMARY ----------------
elif menu == "Summary":

    st.image("https://images.unsplash.com/photo-1543286386-713bdd548da4", use_column_width=True)
    st.subheader("Expense Summary")

    if not df.empty:
        total = df["Amount"].sum()
        st.write(f"### Total Spending: ₹{total}")

        category_summary = df.groupby("Category")["Amount"].sum()
        st.bar_chart(category_summary)
        max_exp = df.loc[df["Amount"].idxmax()]

        st.warning(f"💸 Highest Expense: ₹{max_exp['Amount']} ({max_exp['Category']})")
        df["Date"] = pd.to_datetime(df["Date"])

        monthly = df.groupby(df["Date"].dt.month)["Amount"].sum()

        st.write("### Monthly Spending")
        st.bar_chart(monthly)
        csv = df.to_csv(index=False)
        st.download_button("Download Report", csv, "expenses.csv", "text/csv")
        # 🤖 Expense Prediction
    if len(df) > 2:
        st.write("### 🤖 Expense Prediction")

        df["Date"] = pd.to_datetime(df["Date"])
        df["Days"] = (df["Date"] - df["Date"].min()).dt.days

        X = df[["Days"]]
        y = df["Amount"]

        model = LinearRegression()
        model.fit(X, y)

        next_day = np.array([[df["Days"].max() + 1]])
        prediction = model.predict(next_day)

        st.success(f"Predicted Next Expense: ₹{prediction[0]:.2f}")
    else:
        st.info("No data to summarize")
        # ----------------- WHAT-IF SCENARIO -----------------
st.write("### 🔮 What-If Savings Calculator")

# User inputs hypothetical daily/weekly saving
whatif_amount = st.number_input("Enter amount you want to save daily (₹)", min_value=0.0)
period = st.selectbox("Select period", ["Week", "Month", "Year"])

if st.button("Calculate Savings"):
    if period == "Week":
        savings = whatif_amount * 7
    elif period == "Month":
        savings = whatif_amount * 30
    elif period == "Year":
        savings = whatif_amount * 365

    st.success(f"💰 You can save approximately ₹{savings:.2f} in a {period.lower()}.")
# #-------------------CHATBOT-------------------------------------   
     
# elif menu == "Chatbot":
#     st.subheader("💬 Financial Assistant Bot")
#     st.info("Try: 'saving tips', 'food expense', 'budget planning'") 

#     user_input = st.text_input("Ask something...")

#     if user_input:
#         user_input = user_input.lower()

#         # 👋 Greetings
#         if any(word in user_input for word in ["hi", "hello", "hey"]):
#             st.success("👋 Hello! I'm your finance assistant. How can I help you today?")

#         elif "how are you" in user_input:
#             st.success("😊 I'm doing great! Ready to help you manage your expenses.")

#         elif "your name" in user_input:
#             st.success("🤖 I'm your Smart Expense Assistant!")

        
        

#         if "save" in user_input:
#             st.success("💡 Tip: Try saving at least 20% of your income.")

#         elif "food" in user_input:
#             st.success("🍔 Tip: Reduce eating out to save money.")

#         elif "travel" in user_input:
#             st.success("🚌 Tip: Use public transport to cut costs.")

#         elif "budget" in user_input:
#             st.success("📊 Tip: Set a monthly budget and track daily expenses.")

#         else:
#             st.info("🤖 I'm still learning! Try asking about saving, food, travel, or budget.")        

