import streamlit as st
from datetime import date

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AgriQueue",
    page_icon="🌾",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "registered" not in st.session_state:
    st.session_state.registered = False

if "farmer_name" not in st.session_state:
    st.session_state.farmer_name = ""

if "mobile" not in st.session_state:
    st.session_state.mobile = ""

if "farmer_id" not in st.session_state:
    st.session_state.farmer_id = ""

if "village" not in st.session_state:
    st.session_state.village = ""

if "district" not in st.session_state:
    st.session_state.district = ""

if "centre" not in st.session_state:
    st.session_state.centre = ""

if "slot_booked" not in st.session_state:
    st.session_state.slot_booked = False

if "crop" not in st.session_state:
    st.session_state.crop = "Wheat"

if "quantity" not in st.session_state:
    st.session_state.quantity = 25

if "booking_date" not in st.session_state:
    st.session_state.booking_date = date.today()

if "booking_time" not in st.session_state:
    st.session_state.booking_time = "11:30 AM"

if "token" not in st.session_state:
    st.session_state.token = "A102"


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🌾 AgriQueue")
    st.caption("Smart Procurement Queue Management")
    st.divider()

    if st.button("🏠 Home", use_container_width=True, key="sidebar_home"):
        st.session_state.page = "home"
        st.rerun()

    if st.session_state.registered:

        if st.button("👨‍🌾 Farmer Dashboard", use_container_width=True, key="sidebar_farmer_dashboard"):
            st.session_state.page = "farmer_dashboard"
            st.rerun()

        if st.button("📅 Book Slot", use_container_width=True, key="sidebar_book_slot"):
            st.session_state.page = "booking"
            st.rerun()

        if st.button("🎫 My Token", use_container_width=True, key="sidebar_my_token"):
            st.session_state.page = "token"
            st.rerun()

        if st.button("📦 Procurement Status", use_container_width=True, key="sidebar_procurement_status"):
            st.session_state.page = "procurement"
            st.rerun()

        if st.button("💰 Payment Status", use_container_width=True, key="sidebar_payment_status"):
            st.session_state.page = "payment"
            st.rerun()

        if st.button("🔔 Notifications", use_container_width=True, key="sidebar_notifications"):
            st.session_state.page = "notifications"
            st.rerun()

    st.divider()

    if st.button("⚙️ Admin Dashboard", use_container_width=True, key="sidebar_admin_dashboard"):
        st.session_state.page = "admin"
        st.rerun()


# ==================================================
# HOME PAGE
# ==================================================

if st.session_state.page == "home":

    st.title("🌾 AgriQueue")
    st.subheader("Smart Procurement Queue Management System")

    st.write(
        "Reduce waiting time, manage procurement slots, "
        "track queue position and monitor payments."
    )

    st.divider()

    col1, col2 = st.columns(2, gap="large")

    # ---------------- FARMER ----------------

    with col1:

        st.markdown(
            """<div style="
height: 145px;
padding: 20px;
border: 1px solid #dddddd;
border-radius: 12px;
margin-bottom: 10px;
">
<h3>👨‍🌾 Farmer</h3>
<p>
Register, book a procurement slot,
track your queue and receive updates.
</p>
</div>""",
            unsafe_allow_html=True
        )

        if st.button(
            "👨‍🌾 Continue as Farmer",
            key="farmer_home",
            use_container_width=True
        ):
            st.session_state.page = "registration"
            st.rerun()

    # ---------------- ADMIN ----------------

    with col2:

        st.markdown(
            """<div style="
height: 145px;
padding: 20px;
border: 1px solid #dddddd;
border-radius: 12px;
margin-bottom: 10px;
">
<h3>⚙️ Admin</h3>
<p>
Manage live queues, call farmers
and monitor procurement.
</p>
</div>""",
            unsafe_allow_html=True
        )

        if st.button(
            "⚙️ Continue as Admin",
            key="admin_home",
            use_container_width=True
        ):
            st.session_state.page = "admin"
            st.rerun()

    st.divider()

    st.info(
        "💡 AgriQueue changes the experience from "
        "'Waiting in Line' → 'Waiting Smart'."
    )


# ==================================================
# FARMER REGISTRATION
# ==================================================

elif st.session_state.page == "registration":

    st.title("👨‍🌾 Farmer Registration")
    st.write("Enter your details to continue.")

    farmer_name = st.text_input(
        "Farmer Name",
        value=st.session_state.farmer_name
    )

    mobile = st.text_input(
        "Mobile Number",
        value=st.session_state.mobile
    )

    farmer_id = st.text_input(
        "Farmer ID",
        value=st.session_state.farmer_id
    )

    village = st.text_input(
        "Village",
        value=st.session_state.village
    )

    district = st.text_input(
        "District",
        value=st.session_state.district
    )

    centre = st.selectbox(
        "Procurement Centre",
        [
            "Shirpur Procurement Centre",
            "Shahada Procurement Centre",
            "Nandurbar Procurement Centre"
        ]
    )

    st.divider()

    if st.button(
        "✅ Register Farmer",
        use_container_width=True
    ):

        if farmer_name and mobile and farmer_id and village and district:

            st.session_state.farmer_name = farmer_name
            st.session_state.mobile = mobile
            st.session_state.farmer_id = farmer_id
            st.session_state.village = village
            st.session_state.district = district
            st.session_state.centre = centre
            st.session_state.registered = True
            st.session_state.page = "farmer_dashboard"

            st.success("Registration successful!")
            st.rerun()

        else:
            st.error("Please fill in all the details.")


# ==================================================
# FARMER DASHBOARD
# ==================================================

elif st.session_state.page == "farmer_dashboard":

    st.title(
        f"👋 Welcome, {st.session_state.farmer_name}"
    )

    st.write("Here is your procurement overview.")

    st.divider()

    # STATUS CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🎫 Your Token",
            st.session_state.token
        )

    with col2:
        st.metric(
            "👥 Farmers Ahead",
            "3"
        )

    with col3:
        st.metric(
            "⏱️ Estimated Wait",
            "35 min"
        )

    with col4:
        st.metric(
            "📦 Procurement",
            "Pending"
        )

    st.divider()

    # TODAY'S PROCUREMENT

    st.subheader("📅 Today's Procurement")

    if st.session_state.slot_booked:

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write("**Centre**")
            st.write(st.session_state.centre)

        with col2:
            st.write("**Crop**")
            st.write(st.session_state.crop)

        with col3:
            st.write("**Quantity**")
            st.write(
                f"{st.session_state.quantity} Quintals"
            )

        with col4:
            st.write("**Time**")
            st.write(st.session_state.booking_time)

    else:

        st.warning(
            "You have not booked a procurement slot yet."
        )

        if st.button(
            "📅 Book Procurement Slot",
            use_container_width=True
        ):
            st.session_state.page = "booking"
            st.rerun()

    st.divider()

    # LIVE QUEUE

    st.subheader("🔴 Live Queue")

    queue_data = {
        "Token": [
            "A098",
            "A099",
            "A100",
            "A101",
            "A102"
        ],
        "Farmer": [
            "Suresh",
            "Mahesh",
            "Ramesh",
            "Ganesh",
            st.session_state.farmer_name
        ],
        "Status": [
            "Completed",
            "Serving",
            "Waiting",
            "Waiting",
            "Your Token"
        ]
    }

    st.dataframe(
        queue_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # QUICK ACTIONS

    st.subheader("⚡ Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "🎫 View Token",
            use_container_width=True
        ):
            st.session_state.page = "token"
            st.rerun()

    with col2:

        if st.button(
            "📦 Track Procurement",
            use_container_width=True
        ):
            st.session_state.page = "procurement"
            st.rerun()

    with col3:

        if st.button(
            "💰 Check Payment",
            use_container_width=True
        ):
            st.session_state.page = "payment"
            st.rerun()


# ==================================================
# SLOT BOOKING
# ==================================================

elif st.session_state.page == "booking":

    st.title("📅 Book Procurement Slot")

    st.write(
        "Select your crop, quantity and preferred procurement slot."
    )

    st.divider()

    crop = st.selectbox(
        "🌾 Select Crop",
        [
            "Wheat",
            "Rice",
            "Maize",
            "Bajra",
            "Soybean"
        ]
    )

    quantity = st.number_input(
        "⚖️ Quantity (in Quintals)",
        min_value=1,
        max_value=100,
        value=25
    )

    centre = st.selectbox(
        "🏢 Procurement Centre",
        [
            "Shirpur Procurement Centre",
            "Shahada Procurement Centre",
            "Nandurbar Procurement Centre"
        ]
    )

    booking_date = st.date_input(
        "📅 Select Date",
        value=date.today()
    )

    booking_time = st.selectbox(
        "⏰ Select Time Slot",
        [
            "09:00 AM",
            "09:30 AM",
            "10:00 AM",
            "10:30 AM",
            "11:00 AM",
            "11:30 AM",
            "12:00 PM",
            "12:30 PM"
        ]
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "✅ Confirm Slot",
            use_container_width=True
        ):

            st.session_state.slot_booked = True
            st.session_state.crop = crop
            st.session_state.quantity = quantity
            st.session_state.centre = centre
            st.session_state.booking_date = booking_date
            st.session_state.booking_time = booking_time
            st.session_state.token = "A102"
            st.session_state.page = "token"

            st.rerun()

    with col2:

        if st.button(
            "⬅️ Back",
            use_container_width=True
        ):

            st.session_state.page = "farmer_dashboard"
            st.rerun()


# ==================================================
# DIGITAL TOKEN / LIVE QUEUE
# ==================================================

elif st.session_state.page == "token":

    st.title("🎫 Digital Token")

    if not st.session_state.slot_booked:

        st.warning(
            "Please book a procurement slot first."
        )

        if st.button("📅 Book Slot", key="token_page_book_slot"):
            st.session_state.page = "booking"
            st.rerun()

    else:

        st.success(
            "Your procurement slot has been confirmed!"
        )

        st.divider()

        # TOKEN SUMMARY

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Your Token",
                st.session_state.token
            )

        with col2:
            st.metric(
                "Currently Serving",
                "A099"
            )

        with col3:
            st.metric(
                "Farmers Ahead",
                "3"
            )

        st.divider()

        # LARGE TOKEN CARD
        # IMPORTANT: HTML lines must NOT be indented, or Markdown
        # renders them as a literal code block instead of HTML.

        token = st.session_state.token

        st.markdown(
            f"""<div style="
background-color: #e8f5e9;
border: 2px solid #4caf50;
border-radius: 15px;
padding: 30px;
text-align: center;
margin: 20px 0;
">
<div style="
font-size: 20px;
font-weight: bold;
color: #1b5e20;
">
YOUR DIGITAL TOKEN
</div>
<div style="
font-size: 55px;
font-weight: bold;
color: #1b5e20;
margin: 10px;
">
{token}
</div>
<div style="
font-size: 18px;
color: #333333;
">
Estimated waiting time: 35 minutes
</div>
</div>""",
            unsafe_allow_html=True
        )

        # BOOKING INFORMATION

        st.subheader("📋 Booking Details")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write("**Crop**")
            st.write(st.session_state.crop)

        with col2:
            st.write("**Quantity**")
            st.write(
                f"{st.session_state.quantity} Quintals"
            )

        with col3:
            st.write("**Centre**")
            st.write(st.session_state.centre)

        with col4:
            st.write("**Time**")
            st.write(st.session_state.booking_time)

        st.divider()

        # LIVE QUEUE

        st.subheader("🔴 Live Queue")

        queue = {
            "Token": [
                "A098",
                "A099",
                "A100",
                "A101",
                "A102"
            ],
            "Status": [
                "✅ Completed",
                "🟢 Serving",
                "🟡 Waiting",
                "🟡 Waiting",
                "🔵 Your Token"
            ]
        }

        st.dataframe(
            queue,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            "🔔 You will receive a notification when "
            "your turn is approaching."
        )


# ==================================================
# PROCUREMENT STATUS
# ==================================================

elif st.session_state.page == "procurement":

    st.title("📦 Procurement Status")

    if not st.session_state.slot_booked:

        st.warning(
            "No procurement booking found."
        )

    else:

        st.write(
            f"Token: **{st.session_state.token}**"
        )

        st.write(
            f"Crop: **{st.session_state.crop}**"
        )

        st.write(
            f"Quantity: **{st.session_state.quantity} Quintals**"
        )

        st.divider()

        st.subheader("📍 Procurement Timeline")

        st.success("✅ Slot Booked")
        st.success("✅ Farmer Registered")
        st.info("🔵 Farmer Waiting")
        st.warning("🟡 Produce Verification – Pending")
        st.warning("🟡 Procurement – Pending")
        st.warning("🟡 Payment – Pending")


# ==================================================
# PAYMENT STATUS
# ==================================================

elif st.session_state.page == "payment":

    st.title("💰 Payment Status")

    if not st.session_state.slot_booked:

        st.warning(
            "No procurement transaction found."
        )

    else:

        st.subheader("Payment Details")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Procurement Amount",
                "₹52,500"
            )

        with col2:
            st.metric(
                "Payment Status",
                "Initiated"
            )

        st.divider()

        st.write(
            "**Farmer:**",
            st.session_state.farmer_name
        )

        st.write(
            "**Token:**",
            st.session_state.token
        )

        st.write(
            "**Crop:**",
            st.session_state.crop
        )

        st.write(
            "**Quantity:**",
            f"{st.session_state.quantity} Quintals"
        )

        st.write(
            "**Procurement Centre:**",
            st.session_state.centre
        )

        st.success(
            "💳 Payment has been initiated. "
            "The farmer will be notified once payment is completed."
        )


# ==================================================
# NOTIFICATIONS
# ==================================================

elif st.session_state.page == "notifications":

    st.title("🔔 Notifications")

    notifications = [
        (
            "📅 Slot Confirmed",
            "Your procurement slot has been successfully booked."
        ),
        (
            "🎫 Token Generated",
            f"Your digital token is {st.session_state.token}."
        ),
        (
            "⏳ Queue Update",
            "Your turn is approaching. Please be ready at the centre."
        ),
        (
            "📦 Procurement Update",
            "Your produce verification is pending."
        ),
        (
            "💰 Payment Update",
            "Payment will be initiated after procurement completion."
        )
    ]

    for title, message in notifications:

        with st.container(border=True):

            st.subheader(title)
            st.write(message)


# ==================================================
# ADMIN DASHBOARD
# ==================================================

elif st.session_state.page == "admin":

    st.title("⚙️ Admin Dashboard")

    st.write(
        "Monitor procurement centres and manage the live queue."
    )

    st.divider()

    # ADMIN METRICS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👨‍🌾 Farmers Registered",
            "124"
        )

    with col2:
        st.metric(
            "🎫 Tokens Issued",
            "124"
        )

    with col3:
        st.metric(
            "📦 Procured",
            "87"
        )

    with col4:
        st.metric(
            "⏳ Waiting",
            "37"
        )

    st.divider()

    # LIVE QUEUE

    st.subheader("🔴 Live Queue")

    admin_queue = {
        "Token": [
            "A098",
            "A099",
            "A100",
            "A101",
            "A102"
        ],

        "Farmer": [
            "Suresh Patil",
            "Mahesh Sharma",
            "Ramesh Kumar",
            "Ganesh Pawar",
            st.session_state.farmer_name
        ],

        "Crop": [
            "Wheat",
            "Rice",
            "Wheat",
            "Maize",
            st.session_state.crop
        ],

        "Quantity": [
            "20 Q",
            "30 Q",
            "25 Q",
            "15 Q",
            f"{st.session_state.quantity} Q"
        ],

        "Status": [
            "Completed",
            "Serving",
            "Waiting",
            "Waiting",
            "Waiting"
        ]
    }

    st.dataframe(
        admin_queue,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # QUEUE CONTROLS

    st.subheader("🎛️ Queue Controls")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "📢 Call Next Farmer",
            use_container_width=True
        ):

            st.success(
                "Token A100 has been called."
            )

    with col2:

        if st.button(
            "📦 Complete Procurement",
            use_container_width=True
        ):

            st.success(
                "Procurement for token A099 completed."
            )

    with col3:

        if st.button(
            "🔄 Refresh Queue",
            use_container_width=True
        ):

            st.rerun()

    st.divider()

    # CENTRE STATISTICS

    st.subheader("📊 Procurement Centre Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Waiting Time",
            "32 min"
        )

    with col2:
        st.metric(
            "Average Processing Time",
            "12 min"
        )

    with col3:
        st.metric(
            "Farmers Served Today",
            "87"
        )

    st.divider()

    # PROCUREMENT CENTRES

    st.subheader("🏢 Procurement Centres")

    centre_data = {
        "Centre": [
            "Shirpur",
            "Shahada",
            "Nandurbar"
        ],

        "Farmers Waiting": [
            14,
            11,
            12
        ],

        "Status": [
            "🟢 Active",
            "🟢 Active",
            "🟡 Moderate"
        ]
    }

    st.dataframe(
        centre_data,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "💡 Admin can monitor queues in real time "
        "and manage farmer flow to reduce congestion."
    )