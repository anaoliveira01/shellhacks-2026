import streamlit as st
from datetime import date, time
import time as time_module

import requests
import folium
from streamlit_folium import st_folium


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Wayfind",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       GLOBAL
    -------------------------------------------------------- */

    .stApp {
        background-color: #F7F9FC;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* --------------------------------------------------------
       HEADER
    -------------------------------------------------------- */

    .brand {
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -1px;
        color: #172033;
    }

    .brand-icon {
        font-size: 1.8rem;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.05;
        letter-spacing: -2px;
        color: #172033;
        margin-top: 2rem;
        margin-bottom: 0.75rem;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: #667085;
        max-width: 700px;
        line-height: 1.6;
        margin-bottom: 2rem;
    }

    /* --------------------------------------------------------
       SECTION HEADERS
    -------------------------------------------------------- */

    .section-title {
        font-size: 1.5rem;
        font-weight: 750;
        color: #172033;
        margin-top: 2rem;
        margin-bottom: 0.25rem;
    }

    .section-subtitle {
        color: #667085;
        margin-bottom: 1.25rem;
    }

    /* --------------------------------------------------------
       CARDS
    -------------------------------------------------------- */

    .card {
        background: white;
        border: 1px solid #E4E7EC;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 16px;
        box-shadow: 0 4px 15px rgba(16, 24, 40, 0.04);
    }

    .recommended-card {
        background: white;
        border: 2px solid #4F7CFF;
        border-radius: 20px;
        padding: 26px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(79, 124, 255, 0.10);
    }

    .route-card {
        background: white;
        border: 1px solid #E4E7EC;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 14px;
    }

    /* --------------------------------------------------------
       RECOMMENDED BADGE
    -------------------------------------------------------- */

    .recommended-badge {
        display: inline-block;
        background-color: #EEF4FF;
        color: #3157C7;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 6px 10px;
        border-radius: 999px;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* --------------------------------------------------------
       ROUTE INFORMATION
    -------------------------------------------------------- */

    .route-mode {
        font-size: 1.3rem;
        font-weight: 750;
        color: #172033;
    }

    .route-arrival {
        font-size: 2.3rem;
        font-weight: 800;
        color: #172033;
    }

    .route-label {
        color: #667085;
        font-size: 0.85rem;
    }

    .score {
        font-size: 2rem;
        font-weight: 800;
        color: #3157C7;
    }

    .score-label {
        color: #667085;
        font-size: 0.8rem;
    }

    /* --------------------------------------------------------
       AI EXPLANATION
    -------------------------------------------------------- */

    .ai-card {
        background: #F0F5FF;
        border: 1px solid #D7E2FF;
        border-radius: 18px;
        padding: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .ai-title {
        color: #3157C7;
        font-weight: 750;
        font-size: 1.1rem;
        margin-bottom: 10px;
    }

    /* --------------------------------------------------------
       TRADEOFF
    -------------------------------------------------------- */

    .tradeoff {
        background: #FFF8E7;
        border: 1px solid #F5DF9B;
        border-radius: 12px;
        padding: 14px 16px;
        margin-top: 12px;
        color: #765B00;
    }

    /* --------------------------------------------------------
       MAP PLACEHOLDER
    -------------------------------------------------------- */

    .map-placeholder {
        height: 460px;
        border-radius: 20px;
        border: 1px solid #D9DEE8;
        background:
            linear-gradient(
                135deg,
                #EEF2F7 25%,
                #F8FAFC 25%,
                #F8FAFC 50%,
                #EEF2F7 50%,
                #EEF2F7 75%,
                #F8FAFC 75%
            );
        background-size: 70px 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #667085;
        text-align: center;
        margin-bottom: 20px;
    }

    .map-content {
        background: white;
        border-radius: 16px;
        padding: 20px 28px;
        box-shadow: 0 8px 30px rgba(16, 24, 40, 0.08);
    }

    /* --------------------------------------------------------
       FOOTER
    -------------------------------------------------------- */

    .footer {
        text-align: center;
        color: #98A2B3;
        font-size: 0.85rem;
        padding-top: 3rem;
        padding-bottom: 1rem;
    }

    /* --------------------------------------------------------
       BUTTONS
    -------------------------------------------------------- */

    div.stButton > button {
        border-radius: 12px;
        font-weight: 700;
        min-height: 46px;
    }

    /* --------------------------------------------------------
       DIVIDER
    -------------------------------------------------------- */

    .soft-divider {
        height: 1px;
        background-color: #EAECF0;
        margin: 2rem 0;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DEMO BACKEND
#
# IMPORTANT:
# This is temporary.
#
# Later, your teammates' real backend functions will replace
# this section.
# ============================================================


def get_demo_routes():
    """
    Temporary route data.

    Later this will be replaced by your real routing backend.

    Example future flow:

        get_routes(
            origin,
            destination,
            arrival_time,
            preferences
        )
    """

    return [
        {
            "id": "route_1",
            "mode": "🚗 Drive + Walk",
            "arrival": "9:22 AM",
            "duration": 31,
            "walking": 5,
            "traffic": "Moderate",
            "cost": "$8–12",
            "score": 89,
            "description": "Fast drive followed by a short walk.",
        },
        {
            "id": "route_2",
            "mode": "🚇 Transit + Walk",
            "arrival": "9:26 AM",
            "duration": 38,
            "walking": 9,
            "traffic": "Low",
            "cost": "$2.25",
            "score": 81,
            "description": "Lower traffic exposure with additional walking.",
        },
        {
            "id": "route_3",
            "mode": "🚗 Drive",
            "arrival": "9:18 AM",
            "duration": 27,
            "walking": 2,
            "traffic": "High",
            "cost": "$10–15",
            "score": 76,
            "description": "Fastest option but more traffic exposure.",
        },
    ]


def get_demo_ai_explanation():
    """
    Temporary AI explanation.

    Later Gemini will generate this based on:

    - User preferences
    - Actual routes
    - Route scores
    """

    return {
        "summary": (
            "This route best matches your current priorities because "
            "it keeps walking to a minimum while getting you to your "
            "destination before your target arrival time."
        ),
        "benefits": [
            "Arrives before your target time",
            "Only requires about 5 minutes of walking",
            "Balances travel time and traffic",
        ],
        "tradeoff": (
            "The main tradeoff is moderate traffic compared with "
            "the transit option."
        ),
    }




# ============================================================
# MAP SERVICES: NOMINATIM + OSRM
# ============================================================

@st.cache_data(ttl=86400, show_spinner=False)
def get_coordinates(address):
    """Convert an address into coordinates using Nominatim."""
    response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": address, "format": "jsonv2", "limit": 1},
        headers={"User-Agent": "Wayfind-ShellHacks2026/1.0"},
        timeout=15,
    )
    response.raise_for_status()
    results = response.json()

    if not results:
        return None

    return {
        "latitude": float(results[0]["lat"]),
        "longitude": float(results[0]["lon"]),
        "display_name": results[0].get("display_name", address),
    }


def get_driving_routes(start, end):
    """Retrieve driving routes from OSRM for two coordinate dictionaries."""
    coordinates = (
        f"{start['longitude']},{start['latitude']};"
        f"{end['longitude']},{end['latitude']}"
    )
    response = requests.get(
        f"https://router.project-osrm.org/route/v1/driving/{coordinates}",
        params={
            "overview": "full",
            "geometries": "geojson",
            "alternatives": "true",
        },
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()

    if data.get("code") != "Ok":
        return []

    return data.get("routes", [])


def build_route_map(start, end, routes):
    """Build a Folium map with start/end markers and OSRM route lines."""
    center = [
        (start["latitude"] + end["latitude"]) / 2,
        (start["longitude"] + end["longitude"]) / 2,
    ]
    route_map = folium.Map(location=center, zoom_start=12)

    folium.Marker(
        [start["latitude"], start["longitude"]],
        tooltip="Starting location",
        popup=start["display_name"],
        icon=folium.Icon(color="green", icon="play"),
    ).add_to(route_map)

    folium.Marker(
        [end["latitude"], end["longitude"]],
        tooltip="Destination",
        popup=end["display_name"],
        icon=folium.Icon(color="red", icon="flag"),
    ).add_to(route_map)

    for index, route in enumerate(routes):
        # GeoJSON coordinates are [longitude, latitude]; Folium expects
        # [latitude, longitude].
        points = [
            [latitude, longitude]
            for longitude, latitude in route["geometry"]["coordinates"]
        ]
        folium.PolyLine(
            points,
            color="#3157C7" if index == 0 else "#98A2B3",
            weight=6 if index == 0 else 4,
            opacity=0.9,
            tooltip=f"Driving route {index + 1}",
        ).add_to(route_map)

    route_map.fit_bounds([
        [start["latitude"], start["longitude"]],
        [end["latitude"], end["longitude"]],
    ])
    return route_map


# ============================================================
# SESSION STATE
# ============================================================

if "show_results" not in st.session_state:
    st.session_state.show_results = False

if "selected_route" not in st.session_state:
    st.session_state.selected_route = 0


# ============================================================
# HEADER
# ============================================================

header_col1, header_col2 = st.columns([5, 1])

with header_col1:
    st.markdown(
        '<div class="brand">🧭 Wayfind</div>',
        unsafe_allow_html=True,
    )

with header_col2:
    st.button("How it works", use_container_width=True)


# ============================================================
# HERO
# ============================================================

st.markdown(
    '<div class="hero-title">'
    'Your commute.<br>Your priorities.'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero-subtitle">'
    'Compare transportation options and find the route '
    'that fits your schedule, preferences, and priorities.'
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# COMMUTE PLANNER
# ============================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Plan your commute</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">'
    'Tell us where you are going and what matters most.'
    '</div>',
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Origin / Destination
# ------------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    origin = st.text_input(
        "📍 From",
        placeholder="Starting location",
    )

with col2:

    destination = st.text_input(
        "📍 To",
        placeholder="Destination",
    )


# ------------------------------------------------------------
# Date / Time
# ------------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    arrival_date = st.date_input(
        "📅 Arrival date",
        value=date.today(),
    )

with col2:

    arrival_time = st.time_input(
        "🕘 Arrive by",
        value=time(9, 30),
    )
# ============================================================
# PRIORITY RANKING
# ============================================================

st.markdown(
    '<div class="section-title">Rank your priorities</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">'
    'Rank what matters most for this trip. '
    '1 is your highest priority and 7 is your lowest.'
    '</div>',
    unsafe_allow_html=True,
)

priority_options = [
    "⚡ Fastest",
    "🚶 Low walking",
    "🔄 Fewer transfers",
    "💰 Cheapest",
    "🚦 Avoid accidents & traffic jams",
    "🛡️ Avoid unsafe zones",
    "🅿️ Easy parking",
]

rank_options = [1, 2, 3, 4, 5, 6, 7]

priority_rankings = {}

for index, priority in enumerate(priority_options):

    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(f"**{priority}**")

    with col2:
        priority_rankings[priority] = st.selectbox(
            f"Rank {priority}",
            rank_options,
            index=index,
            key=f"priority_{index}",
            label_visibility="collapsed",
        )

# ============================================================
# FIND ROUTES BUTTON
# ============================================================

st.markdown("")

find_routes = st.button(
    "✦ Find My Best Routes",
    type="primary",
    use_container_width=True,
)


if find_routes:

    # --------------------------------------------------------
    # Basic validation
    # --------------------------------------------------------

    if not origin or not destination:

        st.warning(
            "Please enter both a starting location and destination."
        )

    else:

        # ----------------------------------------------------
        # Loading state
        # ----------------------------------------------------

        with st.spinner(
            "Finding the best transportation options..."
        ):

            # ------------------------------------------------
            # ADDRESS LOOKUP + REAL DRIVING ROUTE FOR THE MAP
            # ------------------------------------------------

            try:
                start_location = get_coordinates(origin.strip())

                # Respect the public Nominatim service's one-request-
                # per-second usage limit when both addresses are uncached.
                time_module.sleep(1)
                end_location = get_coordinates(destination.strip())

                if not start_location or not end_location:
                    st.session_state.show_results = False
                    st.error(
                        "We couldn't find one of those addresses. "
                        "Try adding a city or state."
                    )
                else:
                    driving_routes = get_driving_routes(
                        start_location, end_location
                    )

                    if not driving_routes:
                        st.session_state.show_results = False
                        st.error(
                            "No driving route was found between those "
                            "locations. Please try different addresses."
                        )
                    else:
                        st.session_state.map_start = start_location
                        st.session_state.map_end = end_location
                        st.session_state.map_routes = driving_routes

                        # These cards and the AI explanation are still
                        # demonstration data; only the map route is live.
                        st.session_state.routes = get_demo_routes()
                        st.session_state.ai_explanation = (
                            get_demo_ai_explanation()
                        )
                        st.session_state.show_results = True

            except requests.RequestException as error:
                st.session_state.show_results = False
                st.error(
                    "A mapping service couldn't be reached. "
                    "Please check your connection and try again."
                )


st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# RESULTS
# ============================================================

if st.session_state.show_results:

    routes = st.session_state.routes
    ai_explanation = st.session_state.ai_explanation

    st.markdown(
        '<div class="soft-divider"></div>',
        unsafe_allow_html=True,
    )

    # ========================================================
    # RESULTS HEADER
    # ========================================================

    st.markdown(
        '<div class="section-title">Your best options</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="section-subtitle">'
        f'Routes for arriving by '
        f'<strong>{arrival_time.strftime("%I:%M %p")}</strong>'
        f'</div>',
        unsafe_allow_html=True,
    )


    # ========================================================
    # RECOMMENDED ROUTE
    # ========================================================

    recommended = routes[0]

    st.markdown(
        '<div class="recommended-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="recommended-badge">'
        '✦ Best match for you'
        '</div>',
        unsafe_allow_html=True,
    )

    top_col1, top_col2 = st.columns([4, 1])

    with top_col1:

        st.markdown(
            f'<div class="route-mode">'
            f'{recommended["mode"]}'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="route-arrival">'
            f'{recommended["arrival"]}'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="route-label">'
            'Estimated arrival'
            '</div>',
            unsafe_allow_html=True,
        )

    with top_col2:

        st.markdown(
            f'<div class="score">'
            f'{recommended["score"]}'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="score-label">'
            'Preference match'
            '</div>',
            unsafe_allow_html=True,
        )


    st.markdown("")

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.metric(
            "Travel time",
            f'{recommended["duration"]} min',
        )

    with metric2:
        st.metric(
            "Walking",
            f'{recommended["walking"]} min',
        )

    with metric3:
        st.metric(
            "Traffic",
            recommended["traffic"],
        )

    with metric4:
        st.metric(
            "Estimated cost",
            recommended["cost"],
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


    # ========================================================
    # MAP + AI EXPLANATION
    # ========================================================

    map_col, explanation_col = st.columns([1.5, 1])

    # --------------------------------------------------------
    # MAP
    # --------------------------------------------------------

    with map_col:

        st.markdown(
            '<div class="section-title">Your route</div>',
            unsafe_allow_html=True,
        )

        if (
            "map_start" in st.session_state
            and "map_end" in st.session_state
            and "map_routes" in st.session_state
        ):
            route_map = build_route_map(
                st.session_state.map_start,
                st.session_state.map_end,
                st.session_state.map_routes,
            )
            st_folium(
                route_map,
                width=None,
                height=460,
                key="wayfind_route_map",
            )

            selected_map_route = st.session_state.map_routes[0]
            st.caption(
                "Map route calculated by OSRM. "
                "The route comparison cards below are currently demo data."
            )
            st.metric(
                "Driving distance",
                f"{selected_map_route['distance'] / 1000:.2f} km",
            )
            st.metric(
                "Estimated driving time",
                f"{selected_map_route['duration'] / 60:.0f} min",
            )
            st.caption("Map data © OpenStreetMap contributors.")
        else:
            st.info("Enter two addresses and select Find My Best Routes.")


    # --------------------------------------------------------
    # AI EXPLANATION
    # --------------------------------------------------------

    with explanation_col:

        st.markdown(
            '<div class="ai-card">',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="ai-title">'
            '✦ Why this route?'
            '</div>',
            unsafe_allow_html=True,
        )

        st.write(
            ai_explanation["summary"]
        )

        st.markdown("#### Why it fits")

        for benefit in ai_explanation["benefits"]:

            st.markdown(
                f"✓ {benefit}"
            )

        st.markdown(
            f'<div class="tradeoff">'
            f'<strong>Tradeoff</strong><br>'
            f'{ai_explanation["tradeoff"]}'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )


    # ========================================================
    # OTHER ROUTES
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        'Compare other routes'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        'See how the alternatives compare.'
        '</div>',
        unsafe_allow_html=True,
    )


    for index, route in enumerate(routes):

        if index == 0:
            continue

        with st.container():

            route_col1, route_col2, route_col3 = st.columns(
                [3, 2, 1]
            )

            with route_col1:

                st.markdown(
                    f'<div class="route-mode">'
                    f'{route["mode"]}'
                    f'</div>',
                    unsafe_allow_html=True,
                )

                st.caption(
                    route["description"]
                )

            with route_col2:

                st.write(
                    f'**{route["arrival"]}** arrival'
                )

                st.caption(
                    f'{route["duration"]} min · '
                    f'{route["walking"]} min walking · '
                    f'{route["traffic"]} traffic'
                )

            with route_col3:

                st.markdown(
                    f'<div class="score">'
                    f'{route["score"]}'
                    f'</div>',
                    unsafe_allow_html=True,
                )

                st.caption("Match")


        st.divider()


    # ========================================================
    # DETAILED COMPARISON
    # ========================================================

    with st.expander("See detailed route comparison"):

        comparison_data = []

        for route in routes:

            comparison_data.append(
                {
                    "Route": route["mode"],
                    "Arrival": route["arrival"],
                    "Travel time": f'{route["duration"]} min',
                    "Walking": f'{route["walking"]} min',
                    "Traffic": route["traffic"],
                    "Cost": route["cost"],
                    "Match": f'{route["score"]}/100',
                }
            )

        st.dataframe(
            comparison_data,
            use_container_width=True,
            hide_index=True,
        )


    # ========================================================
    # RESET
    # ========================================================

    st.markdown("")

    if st.button(
        "↻ Plan another commute",
        use_container_width=True,
    ):

        st.session_state.show_results = False

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">'
    'Wayfind · Smarter choices for getting there.'
    '</div>',
    unsafe_allow_html=True,
)
