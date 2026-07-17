import json
from bs4 import BeautifulSoup

def extract_quiz_data(html_file_path, output_json_path):
    try:
        # Load the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        quiz_list = []

        # Find all question containers
        # Moodle quizzes usually wrap each question in a div with class 'que'
        questions = soup.find_all('div', class_='que')
        print(f"Found {len(questions)} questions in the HTML file.")
        
        for q in questions:
            # Extract question text
            qtext_div = q.find('div', class_='qtext')
            
            # Extract the correct answer text
            # We strip "The correct answer is: " from the start if it exists
            right_answer_div = q.find('div', class_='rightanswer')

            if qtext_div and right_answer_div:
                question_text = qtext_div.get_text(separator=" ", strip=True)
                answer_text = right_answer_div.get_text(strip=True)
                
                # Clean up the answer prefix
                if ":" in answer_text:
                    answer_text = answer_text.split(":", 1)[1].strip()

                quiz_list.append({
                    "query": question_text,
                    "response": answer_text
                })

        # Write to JSON file
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(quiz_list, json_file, indent=2)

        print(f"Successfully extracted {len(quiz_list)} items to {output_json_path}")

    except FileNotFoundError:
        print("Error: The HTML file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure your html file is named correctly or update this path
    extract_quiz_data('c:\\temp\\quiz.html', 'c:\\temp\\quiz_results.json')
