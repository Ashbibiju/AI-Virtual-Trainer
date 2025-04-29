# 🏋️‍♂️ AI Virtual Personal Trainer

An intelligent personal fitness trainer built using **Python**, **OpenCV**, **MediaPipe**, and **Hugging Face Transformers**. This project provides real-time posture detection, adaptive workout recommendations, progress visualization, and interactive AI-based coaching—all in one virtual assistant.

---

## 🚀 Features

- 🎯 **Adaptive Workout Plan**  
  Personalized exercise routines based on fitness goals (weight loss, muscle gain, endurance), user heart rate, and fitness level.

- 🧍‍♂️ **Posture Detection**  
  Live webcam-based posture feedback using MediaPipe’s pose estimation model.

- 💬 **NLP-Based Coaching**  
  Uses Hugging Face’s GPT-2 model to answer user queries and simulate AI coaching conversations.

- 🏅 **Gamification with Badges**  
  Assigns bronze, silver, or gold badges based on calories burned to keep users motivated.

- 📊 **Progress Visualization**  
  Displays a calorie burn chart across workout days using `matplotlib`.

---

## 🛠️ Technologies Used

| Tool / Library       | Purpose                              |
|----------------------|--------------------------------------|
| Python               | Core programming language            |
| OpenCV (`cv2`)       | Webcam feed and image processing     |
| MediaPipe Pose       | Real-time human posture estimation   |
| Hugging Face (`transformers`) | NLP-based coaching with GPT-2 |
| Matplotlib           | Graph plotting and progress tracking |
| Threading            | Simultaneous video processing + UI   |

---

## 🏃‍♀️ How It Works

1. **User selects a fitness goal** (weight loss, muscle gain, or endurance).
2. **Workout plan is generated** based on goal, heart rate, and level.
3. **User can ask questions**, and AI provides fitness coaching advice.
4. **Posture detection** starts via webcam in a separate window.
5. **Calories burned are visualized**, and performance badges are awarded.

---

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ashbibiju/ai-virtual-trainer.git
   cd ai-virtual-trainer
   
