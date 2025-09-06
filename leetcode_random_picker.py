#!/usr/bin/env python3
"""
LeetCode Random Question Picker

This script reads the LeetCode Top Interview 150 questions from README.md
and provides functionality to randomly select questions based on various filters.

Features:
- Random question selection
- Filter by difficulty (Easy, Medium, Hard)
- Filter by topic
- Filter by completion status (completed, not completed, all)
- Track and exclude recently solved questions
- Interactive CLI interface

Author: Generated for LeetCode practice
"""

import re
import random
import json
import os
from typing import List, Dict, Optional, Set
from dataclasses import dataclass
from datetime import datetime
import argparse


@dataclass
class Question:
    """Represents a LeetCode question with all its metadata."""
    id: int
    name: str
    difficulty: str
    topic: str
    status: str
    url: Optional[str] = None


class LeetCodeQuestionPicker:
    """Main class for parsing and selecting LeetCode questions."""
    
    def __init__(self, readme_path: str = "README.md", history_file: str = "question_history.json"):
        self.readme_path = readme_path
        self.history_file = history_file
        self.questions: List[Question] = []
        self.topics: Set[str] = set()
        self.difficulties = {"Easy", "Medium", "Hard"}
        self.history = self._load_history()
        
    def _load_history(self) -> Dict:
        """Load question selection history from JSON file."""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {"selected_questions": [], "last_updated": ""}
        return {"selected_questions": [], "last_updated": ""}
    
    def _save_history(self):
        """Save question selection history to JSON file."""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save history: {e}")
    
    def parse_readme(self):
        """Parse the README.md file to extract question information."""
        try:
            with open(self.readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"README.md not found at {self.readme_path}")
        except IOError as e:
            raise IOError(f"Error reading README.md: {e}")
        
        # Find the table section
        table_start = content.find('<tbody>')
        table_end = content.find('</tbody>')
        
        if table_start == -1 or table_end == -1:
            raise ValueError("Could not find question table in README.md")
        
        table_content = content[table_start:table_end]
        
        # Parse topics and questions
        current_topic = ""
        topic_pattern = r'<strong>(Topic-\d+:\s*[^<]+)</strong>'
        question_pattern = r'<tr>\s*<td>(\d+)</td>\s*<td>\s*(?:<a[^>]*>)?\s*([^<\n]+?)(?:</a>)?\s*</td>\s*<td>([^<]+)</td>\s*<td>[^<]*</td>\s*<td>([^<]*)</td>'
        
        lines = table_content.split('\n')
        
        for line in lines:
            # Check for topic headers
            topic_match = re.search(topic_pattern, line)
            if topic_match:
                current_topic = topic_match.group(1).strip()
                self.topics.add(current_topic)
                continue
            
            # Check for question rows
            question_match = re.search(question_pattern, line)
            if question_match and current_topic:
                try:
                    question_id = int(question_match.group(1))
                    name = question_match.group(2).strip()
                    difficulty = question_match.group(3).strip()
                    status = question_match.group(4).strip()
                    
                    # Clean up name (remove extra whitespace and newlines)
                    name = re.sub(r'\s+', ' ', name)
                    
                    # Map status symbols to readable text
                    if status == '✅':
                        status = 'completed'
                    elif status == '❌':
                        status = 'not_completed'
                    else:
                        status = 'unknown'
                    
                    # Extract URL if present
                    url_match = re.search(r'href=["\']([^"\']+)["\']', line)
                    url = url_match.group(1) if url_match else None
                    
                    question = Question(
                        id=question_id,
                        name=name,
                        difficulty=difficulty,
                        topic=current_topic,
                        status=status,
                        url=url
                    )
                    
                    self.questions.append(question)
                    
                except (ValueError, IndexError) as e:
                    # Skip malformed entries
                    continue
        
        print(f"✅ Parsed {len(self.questions)} questions from {len(self.topics)} topics")
    
    def get_questions(self, 
                     difficulty: Optional[str] = None,
                     topic: Optional[str] = None,
                     status: Optional[str] = None,
                     exclude_recent: bool = False,
                     recent_count: int = 10) -> List[Question]:
        """Filter questions based on criteria."""
        filtered_questions = self.questions.copy()
        
        if difficulty:
            filtered_questions = [q for q in filtered_questions if q.difficulty.lower() == difficulty.lower()]
        
        if topic:
            # Allow partial topic matching
            filtered_questions = [q for q in filtered_questions if topic.lower() in q.topic.lower()]
        
        if status:
            if status.lower() == 'completed':
                filtered_questions = [q for q in filtered_questions if q.status == 'completed']
            elif status.lower() == 'not_completed':
                filtered_questions = [q for q in filtered_questions if q.status == 'not_completed']
        
        if exclude_recent and self.history["selected_questions"]:
            recent_ids = set(self.history["selected_questions"][-recent_count:])
            filtered_questions = [q for q in filtered_questions if q.id not in recent_ids]
        
        return filtered_questions
    
    def select_random_question(self, **filters) -> Optional[Question]:
        """Select a random question based on filters."""
        available_questions = self.get_questions(**filters)
        
        if not available_questions:
            return None
        
        selected = random.choice(available_questions)
        
        # Update history
        self.history["selected_questions"].append(selected.id)
        self.history["last_updated"] = datetime.now().isoformat()
        
        # Keep only last 50 selections to prevent file from growing too large
        if len(self.history["selected_questions"]) > 50:
            self.history["selected_questions"] = self.history["selected_questions"][-50:]
        
        self._save_history()
        return selected
    
    def display_question(self, question: Question):
        """Display question information in a formatted way."""
        print("\n" + "="*60)
        print(f"🎯 RANDOM LEETCODE QUESTION")
        print("="*60)
        print(f"📝 Problem #{question.id}: {question.name}")
        print(f"📊 Difficulty: {self._get_difficulty_emoji(question.difficulty)} {question.difficulty}")
        print(f"📚 Topic: {question.topic}")
        print(f"✅ Status: {self._get_status_emoji(question.status)} {question.status.replace('_', ' ').title()}")
        
        if question.url:
            print(f"🔗 URL: {question.url}")
        
        print("="*60)
        print("💡 Good luck with your coding practice!")
        print("="*60 + "\n")
    
    def _get_difficulty_emoji(self, difficulty: str) -> str:
        """Get emoji for difficulty level."""
        emoji_map = {
            "Easy": "🟢",
            "Medium": "🟡", 
            "Hard": "🔴"
        }
        return emoji_map.get(difficulty, "⚪")
    
    def _get_status_emoji(self, status: str) -> str:
        """Get emoji for completion status."""
        emoji_map = {
            "completed": "✅",
            "not_completed": "❌",
            "unknown": "❓"
        }
        return emoji_map.get(status, "❓")
    
    def show_statistics(self):
        """Display statistics about the question collection."""
        if not self.questions:
            print("No questions loaded. Please run parse_readme() first.")
            return
        
        print("\n📊 LEETCODE QUESTIONS STATISTICS")
        print("="*50)
        
        # Overall stats
        total = len(self.questions)
        completed = len([q for q in self.questions if q.status == 'completed'])
        not_completed = len([q for q in self.questions if q.status == 'not_completed'])
        
        print(f"Total Questions: {total}")
        print(f"Completed: {completed} ({completed/total*100:.1f}%)")
        print(f"Not Completed: {not_completed} ({not_completed/total*100:.1f}%)")
        
        # Difficulty breakdown
        print("\nBy Difficulty:")
        for difficulty in self.difficulties:
            count = len([q for q in self.questions if q.difficulty == difficulty])
            print(f"  {self._get_difficulty_emoji(difficulty)} {difficulty}: {count}")
        
        # Topic breakdown
        print(f"\nTopics: {len(self.topics)}")
        for topic in sorted(self.topics):
            count = len([q for q in self.questions if q.topic == topic])
            print(f"  📚 {topic}: {count} questions")
        
        print("="*50 + "\n")
    
    def interactive_mode(self):
        """Run interactive mode for question selection."""
        print("🎯 Welcome to LeetCode Random Question Picker!")
        print("Type 'help' for available commands or 'quit' to exit.\n")
        
        while True:
            try:
                command = input("🔍 Enter command: ").strip().lower()
                
                if command == 'quit' or command == 'exit':
                    print("👋 Happy coding!")
                    break
                
                elif command == 'help':
                    self._show_help()
                
                elif command == 'stats':
                    self.show_statistics()
                
                elif command == 'random' or command == 'r':
                    question = self.select_random_question()
                    if question:
                        self.display_question(question)
                    else:
                        print("❌ No questions available with current filters.")
                
                elif command.startswith('difficulty ') or command.startswith('d '):
                    difficulty = command.split(' ', 1)[1].strip().title()
                    if difficulty in self.difficulties:
                        question = self.select_random_question(difficulty=difficulty)
                        if question:
                            self.display_question(question)
                        else:
                            print(f"❌ No {difficulty} questions available.")
                    else:
                        print(f"❌ Invalid difficulty. Choose from: {', '.join(self.difficulties)}")
                
                elif command.startswith('topic ') or command.startswith('t '):
                    topic = command.split(' ', 1)[1].strip()
                    question = self.select_random_question(topic=topic)
                    if question:
                        self.display_question(question)
                    else:
                        print(f"❌ No questions found for topic containing '{topic}'.")
                
                elif command == 'not completed' or command == 'nc':
                    question = self.select_random_question(status='not_completed')
                    if question:
                        self.display_question(question)
                    else:
                        print("❌ No uncompleted questions found.")
                
                elif command == 'completed' or command == 'c':
                    question = self.select_random_question(status='completed')
                    if question:
                        self.display_question(question)
                    else:
                        print("❌ No completed questions found.")
                
                elif command == 'topics':
                    print("\n📚 Available Topics:")
                    for i, topic in enumerate(sorted(self.topics), 1):
                        count = len([q for q in self.questions if q.topic == topic])
                        print(f"  {i:2d}. {topic} ({count} questions)")
                    print()
                
                else:
                    print("❌ Unknown command. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def _show_help(self):
        """Display help information."""
        help_text = """
🎯 Available Commands:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Basic Commands:
  random, r              - Get a random question
  stats                  - Show question statistics
  topics                 - List all available topics
  help                   - Show this help message
  quit, exit             - Exit the program

Filtering Commands:
  difficulty <level>     - Random question by difficulty (Easy/Medium/Hard)
  d <level>             - Short form of difficulty command
  topic <name>          - Random question from topic (partial matching)
  t <name>              - Short form of topic command
  not completed, nc     - Random uncompleted question
  completed, c          - Random completed question

Examples:
  difficulty Easy       - Get random Easy question
  d Medium             - Get random Medium question
  topic Array          - Get random question from Array topics
  t Binary Tree        - Get random Binary Tree question
  nc                   - Get random uncompleted question

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        print(help_text)


def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description="LeetCode Random Question Picker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python leetcode_random_picker.py                    # Interactive mode
  python leetcode_random_picker.py --random           # Get one random question
  python leetcode_random_picker.py --difficulty Easy  # Get random Easy question
  python leetcode_random_picker.py --topic "Array"    # Get random Array question
  python leetcode_random_picker.py --stats            # Show statistics
        """
    )
    
    parser.add_argument('--readme', default='README.md', 
                       help='Path to README.md file (default: README.md)')
    parser.add_argument('--random', action='store_true',
                       help='Get one random question and exit')
    parser.add_argument('--difficulty', choices=['Easy', 'Medium', 'Hard'],
                       help='Filter by difficulty level')
    parser.add_argument('--topic', help='Filter by topic (partial matching)')
    parser.add_argument('--status', choices=['completed', 'not_completed'],
                       help='Filter by completion status')
    parser.add_argument('--stats', action='store_true',
                       help='Show statistics and exit')
    parser.add_argument('--exclude-recent', action='store_true',
                       help='Exclude recently selected questions')
    
    args = parser.parse_args()
    
    # Initialize picker
    picker = LeetCodeQuestionPicker(readme_path=args.readme)
    
    try:
        # Parse questions from README
        picker.parse_readme()
        
        if args.stats:
            picker.show_statistics()
            return
        
        if args.random or args.difficulty or args.topic or args.status:
            # Command line mode
            question = picker.select_random_question(
                difficulty=args.difficulty,
                topic=args.topic,
                status=args.status,
                exclude_recent=args.exclude_recent
            )
            
            if question:
                picker.display_question(question)
            else:
                print("❌ No questions found matching the specified criteria.")
        else:
            # Interactive mode
            picker.interactive_mode()
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
