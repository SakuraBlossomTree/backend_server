from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request
import praw
# import random

app = Flask(__name__,template_folder='template')
CORS(app)

def fetch_images():

    reddit = praw.Reddit(

           client_id="jbfroiFBDlM7jtEn9DVEVg",
           client_secret="wZZ4xdF8tuxY2Eopb5VOdnaashmZdw",
           user_agent="/r/Animewallpaper image grabber v1.0"
           
           )

    subreddit = reddit.subreddit("Animewallpaper")

    #search = ['Genshin Impact']

    search = request.args.get("keyword")

    already_done = []

    results = [] 

    if search is None or len(search) == 0:
        return results
    

    for submission in subreddit.search(search):

        result = submission.url

        print(result)

        print(submission.link_flair_text)

        if ".jpg" in result:

            if submission.link_flair_text == "Mobile":

                if submission.id not in already_done:

                    already_done.append(result)

                    results.append(submission.url)

                    print(results)

                    if len(results) == 10:  # limit to 10 results
                        break

    return results


@app.route("/wallpaper")
def get_images():

    images = fetch_images()
    print(images)

    response = {"images": images}

    return jsonify(response)

if __name__ in '__main__':

    app.run(host='0.0.0.0', port=5000)
