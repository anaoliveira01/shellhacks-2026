# shellhacks-2026
WayFind
-WayFind will find a way!-


Wayfind is an AI-powered pathfinding tool that helps users find a transportation option that best fits their schedule and priorities.


It uses route information and input provided by the user such as the user's current location, destination, arrival time, and transportation preferences. WayFind compares available route options, evaluates them according to the user's preferences, and presents the tradeoffs in an easy-to-understand interface, allowing users to compare and evaluate transportation options before making a decision.


# Problem
Modern transportation tools always find the quickest route, but never accounts for which route is best based on the user's preferences such as they want minimal walking or don't mind a longer travel time.


# Solution
WayFind combines real-world transportation data, deterministic route scoring, and AI-powered preference interpretation into one system.


WayFind takes user input such as their destination, arrival time, their preferences (travel time, walking distance, cost, etc.), then processes and interprets the user's priorities to provide and score routes based on those priorities, allowing the user to compare all available routes before making a decision.


# Core Experience
1. Users enter their location, destination, arrival date and time.
2. Then the users adjust their transportation preferences such as travel time, walking distance, avoid traffic, cost, and number of transfers.
3. WayFind presents the user multiple routes along with a score of how well it matches their preferences and an explanation for its reasoning.
4. The routes are displayed on a map for the user to see them visually


# Tech Stack
Python, Streamlit, Google Gemini API, GitHub, Overleaf extension, Google Gemini API, OSRM HTTP server, Geocoding, Git, and powershell

