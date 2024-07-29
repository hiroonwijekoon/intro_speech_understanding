import bs4, gtts

def extract_stories_from_NPR_text(text):
    stories = []
    for div_tag in text.find_all('div', 'story-text'):
        titletag = div_tag.find('h3', 'title')
        teasertag = div_tag.find('p', 'teaser')
        
        if teasertag != None:
            stories.append((titletag.text, teasertag.text))
        else:
            stories.append((titletag.text, ""))
    return stories
    
def read_nth_story(stories, n, filename):
    text = "Here is a list of today's top stories."
    for n, story in enumerate(stories):
        text += "Story Number %d: %s.\n"%(n, story[0])
    gtts.gTTS(text=text, lang="en").save(filename)
