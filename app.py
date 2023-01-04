from flask import Flask, Response, render_template
import pdfkit
import pandas as pd


app = Flask(__name__)
stories_list = pd.read_csv("db_books.csv")
all_stories = pd.read_csv("stories.csv")
non_english_rows = stories_list.loc[stories_list['Language'] != "English"]
stories_list.drop(non_english_rows.index, inplace=True)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('story.html')

@app.route('/generate-story', methods=['GET'])
def generate_story():
    print("Finding a random story")
    random_story_id = stories_list.sample().iloc[0, 0]
    story = all_stories.loc[all_stories['bookno'] == random_story_id].iloc[0,1]
    return story


@app.route('/download-pdf', methods=['GET'])
def download_pdf():
    # Generate a PDF of the story
    pdf = pdfkit.from_string('Story', 'story.pdf')
    return Response(pdf, mimetype='application/pdf')


if __name__ == '__main__':
    app.run()
