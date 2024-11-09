Functionality of development with neo4j is still under develeopmennt. Rest all virtues have been touched and the model is giving good responses.

One-Day Tour Planning Assistant

Description

This project implements a One-Day Tour Planning Assistant designed to help users create a personalized and optimized itinerary for a city visit based on their preferences. The system facilitates dynamic and flexible planning, adjusting in real-time as users provide new inputs, preferences, or constraints during the conversation.

The application interacts with the user via a chat interface where they specify details such as the city, available timings, budget, and interests (e.g., culture, adventure, food, shopping). It remembers user preferences across interactions and uses LLM agents to generate and optimize itineraries, considering factors such as available time, budget, and location preferences.

Problem Statement

The goal is to create an intuitive and dynamic one-day tour planning application that can:
	•	Collect user preferences, including city, available timings, budget, and interests.
	•	Recommend popular attractions based on the user’s preferences or suggest new options if the user is unsure.
	•	Optimize the itinerary based on the user’s budget, interests, and time constraints.
	•	Dynamically adjust the itinerary as the user adds or modifies parameters (e.g., lunch preferences, weather considerations).
	•	Provide a visual map (optional) and detailed itinerary, including transportation methods, attraction status, and weather information.

Features

	•	User Preferences: Collect user details such as the city, interests (e.g., culture, food), budget, and start/end times for the trip.
	•	Dynamic Itinerary Generation: Generate an initial itinerary with optimized travel paths and visit sequence.
	•	Personalization: The system remembers user preferences across sessions, adapting to different personas.
	•	Memory: Personalized memory of the user’s preferences, stored in a graph database (Neo4j).
	•	Weather Integration: Provides weather recommendations based on the selected day.
	•	Optimized Path: Adjusts travel based on budget constraints (e.g., using taxis or public transport).
	•	Interactive Chat Interface: Allows users to interact with the assistant, update their preferences, and make changes to the plan.

Tools and Technologies

	•	Transformers / Ollama / vLLM: For language model-based responses.
	•	Neo4j: For storing and managing user preferences using a graph database.
	•	Streamlit: For creating a user-friendly chat interface and displaying the itinerary.
	•	FastAPI: For handling microservices and agent interactions.
	•	Weather API: For fetching weather information to adjust the itinerary accordingly.

Agents Used

	•	User Interaction Agent: Gathers and processes user preferences.
	•	Itinerary Generation Agent: Creates the initial itinerary based on user preferences.
	•	Optimization Agent: Adjusts the itinerary to optimize travel paths based on budget and time.
	•	Weather Agent: Fetches weather conditions for the selected date.
	•	News Agent: Fetches any updates about the attractions or area.
	•	Memory Agent: Remembers user preferences for a personalized experience.


Project Structure

.
├── app.py               # Main Streamlit app to run the interface
├── utils.py             # Helper functions for itinerary generation and LLM calls
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation

Installation

To set up this project locally, follow these steps:
	1.	Clone the repository:

git clone https://github.com/Saransh0903/attention-ai.git
cd tour-planner


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Run the application:

streamlit run assistant.py
