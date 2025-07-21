# Welcome and Initial Prompts
WELCOME_PROMPT = """🌟 Welcome to CareerMap AI! 🌟

I'm here to help you discover career paths that align with your interests, skills, and aspirations. 

Together, we'll:
1. Explore your professional interests
2. Identify your current skills
3. Match you with suitable careers
4. Create a personalized learning plan

Let's begin! What are you passionate about or interested in pursuing? (e.g., technology, healthcare, design)"""

INTERESTS_PROMPT = "Great! Could you tell me more about your specific interests within {interests}? What aspects particularly excite you?"

SKILLS_PROMPT = """Thanks for sharing your interests! 

Now, please list any skills you currently have (separated by commas). These can be:
- Technical skills (programming, design tools)
- Soft skills (communication, leadership)
- Domain knowledge (finance, biology)
  
Example: Python, public speaking, financial analysis"""

EDUCATION_PROMPT = """Almost done with the initial assessment!

What's your current education level? 
(e.g., High school, Bachelor's in Computer Science, Master's in Business, PhD candidate)"""

# Career Matching
NO_MATCHES_PROMPT = """Hmm, I'm having trouble finding perfect matches based on your current profile. 

This could mean:
1. Your interests/skills are very unique (which is great!)
2. We need to explore broader options

Would you like to:
- [Broaden] Expand the search criteria
- [Refine] Re-enter your skills/interests
- [Explore] See emerging fields in your interest area"""

CAREER_SUGGESTION_TEMPLATE = """🚀 Career Suggestion: {title}

📌 Overview: {description}

🔧 Key Skills Needed: {skills}

🌍 Global Demand: {demand}

✅ Your Alignment: {alignment} (based on your current profile)

📈 Future Outlook: {outlook}

Does this career path interest you? (Yes/No)"""

# Learning Path
LEARNING_ROADMAP_TEMPLATE = """📚 Learning Roadmap for {title}

⏳ Estimated Duration: {duration}

🔗 Recommended Resources:
{resources}

🗺️ Step-by-Step Path:
{steps}

💡 Motivational Tip: {tips}

Would you like me to save this plan or modify any aspects?"""

MOTIVATIONAL_TIPS = [
    "Remember: Every expert was once a beginner. Consistency beats intensity in the long run.",
    "Progress isn't linear. Celebrate small wins along your journey!",
    "The best time to start was yesterday. The next best time is now!",
    "Skill acquisition is like compound interest - small daily improvements lead to massive results over time."
]

# Follow-up
FOLLOW_UP_PROMPT = """What would you like to do next?
1. Get more details about this career
2. See alternative career options
3. Adjust my profile information
4. Save this plan and exit"""
