
import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Karishma Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #e50914;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.summary {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
}

.total {
    font-size: 28px;
    font-weight: bold;
    color: #e50914;
    text-align: right;
}

</style>
""", unsafe_allow_html=True)


# ---------------- MOVIE DATA ----------------
movies = {
    "Avengers: Endgame": 200,
    "Interstellar": 180,
    "Inception": 180,
    "Spider-Man": 220,
    "RRR": 150,
    "Pushpa 2": 180
}


# ---------------- TICKET TYPES ----------------
ticket_types = {
    "Regular": 1.0,
    "Premium": 1.25,
    "VIP": 1.50
}


# ---------------- HEADER ----------------
st.markdown(
    '<div class="title">🎬 Karishma Movie Ticket Booking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Book your movie tickets quickly and easily!'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- CUSTOMER DETAILS ----------------
st.subheader("👤 Customer Details")

customer_name = st.text_input(
    "Customer Name",
    placeholder="Enter your name",
    key="customer_name"
)


# ---------------- MOVIE SELECTION ----------------
st.subheader("🎥 Select Movie")

movie = st.selectbox(
    "Choose a movie",
    list(movies.keys()),
    key="movie_selection"
)

base_price = movies[movie]


# ---------------- TICKET CATEGORY ----------------
st.subheader("🎟️ Ticket Category")

ticket_type = st.radio(
    "Choose ticket type",
    list(ticket_types.keys()),
    horizontal=True,
    key="ticket_type"
)

multiplier = ticket_types[ticket_type]

ticket_price = base_price * multiplier


# ---------------- NUMBER OF TICKETS ----------------
st.subheader("🔢 Number of Tickets")

quantity = st.number_input(
    "Tickets",
    min_value=1,
    max_value=20,
    value=1,
    step=1,
    key="ticket_quantity"
)


# ---------------- SHOW INFORMATION ----------------
st.subheader("📅 Show Details")

col1, col2 = st.columns(2)

with col1:
    show_date = st.date_input(
        "Select Date",
        key="show_date"
    )

with col2:
    show_time = st.selectbox(
        "Select Show Time",
        [
            "10:00 AM",
            "1:00 PM",
            "4:00 PM",
            "7:00 PM",
            "10:00 PM"
        ],
        key="show_time"
    )


# ---------------- PRICE CALCULATION ----------------
total_price = ticket_price * quantity


# ---------------- PRICE PREVIEW ----------------
st.markdown("---")

st.subheader("💰 Price Details")

col1, col2 = st.columns(2)

with col1:
    st.write("Movie")
    st.write("Ticket Type")
    st.write("Price per Ticket")
    st.write("Number of Tickets")

with col2:
    st.write(f"**{movie}**")
    st.write(f"**{ticket_type}**")
    st.write(f"**₹{ticket_price:.2f}**")
    st.write(f"**{quantity}**")


st.markdown(
    f'<div class="total">Total: ₹{total_price:.2f}</div>',
    unsafe_allow_html=True
)


# ---------------- BOOK TICKET ----------------
if st.button(
    "🎟️ Confirm Booking",
    use_container_width=True,
    key="confirm_booking"
):

    if customer_name.strip() == "":
        st.warning("⚠️ Please enter your name.")

    else:

        st.success(
            "🎉 Booking Confirmed Successfully!"
        )

        st.markdown("---")

        # ---------------- BOOKING SUMMARY ----------------
        st.markdown(
            '<div class="summary">',
            unsafe_allow_html=True
        )

        st.markdown(
            "## 🎬 BOOKING SUMMARY"
        )

        st.write(
            f"**Customer Name:** {customer_name}"
        )

        st.write(
            f"**Movie:** {movie}"
        )

        st.write(
            f"**Ticket Type:** {ticket_type}"
        )

        st.write(
            f"**Number of Tickets:** {quantity}"
        )

        st.write(
            f"**Show Date:** {show_date}"
        )

        st.write(
            f"**Show Time:** {show_time}"
        )

        st.write(
            f"**Price per Ticket:** ₹{ticket_price:.2f}"
        )

        st.markdown("---")

        st.markdown(
            f'<div class="total">'
            f'Grand Total: ₹{total_price:.2f}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.write(
            f"🕐 Booking Time: "
            f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
        )

        st.markdown(
            '<p style="text-align:center;">'
            '🍿 Enjoy your movie! 🎉'
            '</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# ---------------- FOOTER ----------------
st.markdown("---")

st.caption(
    "🎬 Karishma Movie Ticket Booking "
    "| Built with Python + Streamlit"
)

