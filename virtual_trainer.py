import cv2
import mediapipe as mp
import random
import matplotlib.pyplot as plt
from transformers import pipeline
import threading

# Setup: Posture Detection
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# Setup: NLP Assistant
chatbot = pipeline("text-generation", model="gpt2")

# Simulated wearable API
def get_user_metrics():
    return {
        "heart_rate": random.randint(70, 130),
        "calories_burned": random.randint(200, 600),
        "steps": random.randint(3000, 10000)
    }

# Generate Adaptive Workout Plan
def generate_plan(goal, heart_rate, level):
    workouts = {
        "weight_loss": ["Jump rope", "Burpees", "Mountain climbers"],
        "muscle_gain": ["Push-ups", "Deadlifts", "Squats"],
        "endurance": ["Running", "Cycling", "Swimming"]
    }
    plan = random.sample(workouts[goal], k=2)
    intensity = "high" if heart_rate < 90 else "moderate" if heart_rate < 120 else "low"
    return {
        "plan": plan,
        "intensity": intensity,
        "level": level
    }

# NLP Coaching Response
def get_coaching_response(user_query):
    response = chatbot(user_query, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

# Gamification Badges
def get_badge(progress):
    if progress >= 100:
        return "🏅 Gold Badge"
    elif progress >= 50:
        return "🥈 Silver Badge"
    else:
        return "🥉 Bronze Badge"

# Progress Chart
def plot_progress(days, calories):
    plt.plot(days, calories, marker='o')
    plt.title("Calories Burned Over Time")
    plt.xlabel("Day")
    plt.ylabel("Calories Burned")
    plt.grid(True)
    plt.show()

# Live Posture Detection in Thread
def run_posture_detection():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if not success:
            break

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(img_rgb)

        if results.pose_landmarks:
            mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            if abs(left_shoulder.y - left_hip.y) < 0.2:
                posture = "Good Posture"
            else:
                posture = "Bad Posture"
            cv2.putText(img, posture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Posture Detection", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Main Trainer Logic
def virtual_trainer():
    print("\n🏋️‍♂️ Welcome to your AI Virtual Personal Trainer!")
    print("Choose your goal:\n1. Weight Loss\n2. Muscle Gain\n3. Endurance")
    choice = input("Enter (1/2/3): ")
    goals = {"1": "weight_loss", "2": "muscle_gain", "3": "endurance"}
    goal = goals.get(choice, "weight_loss")

    level = input("Enter fitness level (beginner/intermediate/advanced): ")
    metrics = get_user_metrics()
    plan = generate_plan(goal, metrics["heart_rate"], level)

    print("\n🧠 AI-Generated Workout Plan:")
    for ex in plan['plan']:
        print(f"- {ex} - Intensity: {plan['intensity']}")

    print(f"\n📈 Your Current Metrics: HR: {metrics['heart_rate']} bpm | Calories: {metrics['calories_burned']} | Steps: {metrics['steps']}")
    print(f"🏅 Your Badge: {get_badge(metrics['calories_burned'])}")

    ask = input("\nDo you want coaching advice? (yes/no): ")
    if ask.lower().startswith("y"):
        query = input("Ask your trainer: ")
        print("\n🤖 Coach says:")
        print(get_coaching_response(query))

    show_plot = input("\nSee progress chart? (yes/no): ")
    if show_plot.lower().startswith("y"):
        days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        calories = [random.randint(200, 600) for _ in days]
        plot_progress(days, calories)

    print("\n✅ Done. Start posture detection in a new window. Press 'q' to exit it.")

# Run trainer + posture in thread
if __name__ == "__main__":
    posture_thread = threading.Thread(target=run_posture_detection)
    posture_thread.start()
    virtual_trainer()
