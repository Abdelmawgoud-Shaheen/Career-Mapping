import json
import random
from typing import Dict, List, Optional
import time

# Import prompts (we'll create this next)
from prompts import *

class CareerMapAI:
    def __init__(self):
        self.user_data = {}
        self.load_career_data()
        self.current_stage = "welcome"
        self.current_suggestions = []
        
    def load_career_data(self):
        """Load career database from JSON file"""
        with open('careers.json', 'r') as f:
            self.career_db = json.load(f)
    
    def greet_user(self):
        """Initial welcome message"""
        return WELCOME_PROMPT
    
    def process_response(self, user_input: str) -> str:
        """Main state machine handling conversation flow"""
        user_input = user_input.lower().strip()
        
        if self.current_stage == "welcome":
            self.current_stage = "collect_interests"
            return INTERESTS_PROMPT
            
        elif self.current_stage == "collect_interests":
            self.user_data['interests'] = user_input
            self.current_stage = "collect_skills"
            return SKILLS_PROMPT
            
        elif self.current_stage == "collect_skills":
            self.user_data['skills'] = user_input.split(',')
            self.current_stage = "collect_education"
            return EDUCATION_PROMPT
            
        elif self.current_stage == "collect_education":
            self.user_data['education'] = user_input
            self.current_stage = "suggest_careers"
            return self.generate_career_suggestions()
            
        elif self.current_stage == "suggest_careers":
            if "yes" in user_input:
                selected_career = self.current_suggestions[0]  # For simplicity, take first suggestion
                self.current_stage = "generate_roadmap"
                return self.generate_learning_roadmap(selected_career)
            else:
                self.current_suggestions.pop(0)  # Remove this suggestion
                if self.current_suggestions:
                    return self.format_career_suggestion(self.current_suggestions[0])
                else:
                    self.current_stage = "no_matches"
                    return NO_MATCHES_PROMPT
                    
        elif self.current_stage == "generate_roadmap":
            self.current_stage = "follow_up"
            return FOLLOW_UP_PROMPT
            
        return "I'm not sure how to respond to that. Could you rephrase?"
    
    def generate_career_suggestions(self) -> str:
        """Match user profile with career database"""
        # Simple matching algorithm - can be enhanced with ML later
        matched_careers = []
        
        for career in self.career_db:
            match_score = 0
            
            # Basic keyword matching
            for interest in self.user_data['interests'].split():
                if interest in career['keywords']:
                    match_score += 1
            
            for skill in self.user_data['skills']:
                if skill in career['required_skills']:
                    match_score += 2
            
            if match_score > 0:
                matched_careers.append((career, match_score))
        
        if not matched_careers:
            self.current_stage = "no_matches"
            return NO_MATCHES_PROMPT
        
        # Sort by match score
        matched_careers.sort(key=lambda x: x[1], reverse=True)
        self.current_suggestions = [career for career, score in matched_careers[:3]]
        
        return self.format_career_suggestion(self.current_suggestions[0])
    
    def format_career_suggestion(self, career: Dict) -> str:
        """Format career details for user presentation"""
        alignment = self.calculate_alignment(career)
        
        return CAREER_SUGGESTION_TEMPLATE.format(
            title=career['title'],
            description=career['description'],
            skills=", ".join(career['required_skills']),
            demand=career['demand'],
            alignment=alignment,
            outlook=career['outlook']
        )
    
    def calculate_alignment(self, career: Dict) -> str:
        """Calculate how well user matches career requirements"""
        matched_skills = sum(1 for skill in self.user_data['skills'] 
                          if skill in career['required_skills'])
        total_skills = len(career['required_skills'])
        
        ratio = matched_skills / max(total_skills, 1)
        
        if ratio > 0.75:
            return "Excellent match"
        elif ratio > 0.5:
            return "Good match"
        elif ratio > 0.25:
            return "Partial match"
        return "Basic match"
    
    def generate_learning_roadmap(self, career: Dict) -> str:
        """Create personalized learning plan"""
        level = self.user_data['education']
        duration = self.estimate_learning_duration(level, career)
        
        return LEARNING_ROADMAP_TEMPLATE.format(
            title=career['title'],
            duration=duration,
            resources="\n".join([f"- {res}" for res in career['learning_resources']]),
            steps="\n".join([f"{i+1}. {step}" for i, step in enumerate(career['learning_path'])]),
            tips=random.choice(MOTIVATIONAL_TIPS)
        )
    
    def estimate_learning_duration(self, education_level: str, career: Dict) -> str:
        """Estimate time needed to acquire required skills"""
        if "phd" in education_level.lower():
            return "3-6 months of focused learning"
        elif "master" in education_level.lower():
            return "6-12 months"
        elif "bachelor" in education_level.lower():
            return "1-2 years"
        return "2+ years (consider foundational education first)"

# Main chat loop
def run_chatbot():
    bot = CareerMapAI()
    print(bot.greet_user())
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("CareerMap AI: Thank you for using CareerMap AI! Wishing you success in your career journey!")
            break
            
        response = bot.process_response(user_input)
        print("\nCareerMap AI: " + response + "\n")

if __name__ == "__main__":
    run_chatbot()
