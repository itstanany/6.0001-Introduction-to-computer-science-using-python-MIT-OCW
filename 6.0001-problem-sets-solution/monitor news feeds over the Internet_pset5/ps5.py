# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Ahmed Ali Mohamed
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = str(guid)
        self.title = str(title)
        self.description = str(description)
        self.link = str(link)
        self.pubdate = pubdate
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        print("inside eval of trigger class")
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = str(phrase).lower()
    #text checking function
    def is_phrase_in(self, text):
        '''
        THIS FUNCTION FAILED BEAUASE IT RETURNS STRING OF ONE WORD
        WHEN IT'S SUPPLIED BY A STRING OF MORE THAN ONE WORD SEPARATED BY SYMBOLS AND PUNCTUAION
                # make a function to manipulate any text to be formed only from words in lower case
        #        def pure_words(row_string):
        #            #initialize new empty string to hold manipulated string
        #            new_wordy_string = ""
        #            #loop through evey chachter in the string,
        #            row_string = row_string.strip(' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        #            for c in row_string:   
        #                #if the charchter is in puctuatuin, ignore it, else, add it ti the new string
        #                if c in string.punctuation:
        #                    pass
        #                else:
        #                    new_wordy_string += c
        #            #return the new manipulated string
        #            return new_wordy_string
                #apply the above function to both phrase and text
                #those are strings of only words separated by whitespace
        '''
        wordy_phrase = re.findall(r'\w+', self.phrase.lower())
        words_text = re.findall(r'\w+', text.lower())
        
#        print("wordy phrase", wordy_phrase)
#        print("words text-title in is_phrase_in func", words_text)
#        latest_index = words_text.index
        present = True
        for w in wordy_phrase:
#            print("Enter loop for presence checking")
            if w in words_text:
                pass
            else:
                present = False
                break
        if not present:
            return False
        #test of being consecutive
        in_text_indices = []
        for p in wordy_phrase:
#            print("enter loop for appending indices")
#            print("words_text", words_text)
#            print("words_text.index[p]", words_text.index(p))
            in_text_indices.append(words_text.index(p))
        for i in range(len(in_text_indices)-1):
#            print("Enter loop for consecutive checking")
            if (in_text_indices[i+1] - in_text_indices[i]) != 1:
#                print("return False")
                return False
        #test whether phrase in text or not
#        print("REturn True")
        return True
        #return the result of the test
    
#ahmed = PhraseTrigger("AhmeD!")
#print(ahmed.is_phrase_in("Ali Mo aHmEd"))

# Problem 3
# TODO: TitleTrigger
#initialize the class
class TitleTrigger(PhraseTrigger):  
    # implement init funct to take a phrase
    def __init__(self, phrase):
        '''
        this function inherits attributes
        self.phrase
        '''
        PhraseTrigger.__init__(self, phrase)
        #implement evaluate function
        '''
        def evaluate(self, story):
        return self.is_phrase_in(story.get_title()) 
        '''
    def evaluate(self, story):
#        title = story.get_title()
#        is_in = self.is_phrase_in(story.get_title())
#        print("title", title)
#        print("is_in in evaluate", is_in )
        return self.is_phrase_in(story.get_title())
        #make it return the value of is_phrase_in taking 
#ahmed = TitleTrigger("AhmeD!")
#print(ahmed.evaluate("Ali Mo aHmEd"))
# Problem 4
class DescriptionTrigger(PhraseTrigger):  
    #It is the same as titletrigger class, except in evaluate function use method 
    #get description to test presence of the phrase upon it
    # implement init funct to take a phrase
    def __init__(self, phrase):
        '''
        this function inherits attributes
        self.phrase
        '''
        PhraseTrigger.__init__(self, phrase)
        #implement evaluate function
        '''
        def evaluate(self, story):
        return self.is_phrase_in(story.get_title()) 
        '''
    def evaluate(self, story):
#        title = story.get_description()
#        is_in = self.is_phrase_in(story.get_description())
#        print("get_description", get_description)
#        print("is_in in evaluate", is_in )
        return self.is_phrase_in(story.get_description())
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, trig_date):
        #converting string input to datetime object
        date_object = datetime.strptime(trig_date, "%d %b %Y %H:%M:%S")
        #assigning datetime object to instance attribute
        self.trigger_date = date_object

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger)        :
    def __init__(self, publicdate):
        TimeTrigger.__init__(self, publicdate)
    def evaluate(self, story):
        #solve the problem of time zone conflicts
        pub_date = story.get_pubdate().replace(tzinfo=None)
        if self.trigger_date > pub_date:
            return True
        else:
            return False


class AfterTrigger(TimeTrigger)        :
    def __init__(self, publicdate_after):
        TimeTrigger.__init__(self, publicdate_after)
    def evaluate(self, story):
        #solve the problem of time zone conflicts
        pub_date = story.get_pubdate().replace(tzinfo=None)
        if self.trigger_date < pub_date:
            return True
        else:
            return False


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, in_trig):
        self.trigr = in_trig
    def evaluate(self, story):
        return not self.trigr.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trig_1, trig_2):
        self.trig_one = trig_1
        self.trig_two = trig_2
    def evaluate(self, story):
        return (self.trig_one.evaluate(story) and self.trig_two.evaluate(story))
        
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trig_1, trig_2):
        self.trig_one = trig_1
        self.trig_two = trig_2
    def evaluate(self, story):
        return (self.trig_one.evaluate(story) or self.trig_two.evaluate(story))

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    trig_stories = []
    for story in stories:
        for trig in triggerlist:
            if trig.evaluate(story):
                trig_stories.append(story)
                break
            
    return trig_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trig_dict = {}
    trig_list = []
    for i in range(len(lines)):
        trig = lines[i].split(',')
        if trig[1] == 'TITLE':
            trig_dict[trig[0]] = TitleTrigger(trig[2])
        elif trig[1] == 'DESCRIPTION':
            trig_dict[trig[0]] = DescriptionTrigger(trig[2])
        elif trig[1] == 'AFTER':
            trig_dict[trig[0]] = AfterTrigger(trig[2])
        elif trig[1] == 'BEFORE':
            trig_dict[trig[0]] = BeforeTrigger(trig[2])
        elif trig[1] == 'NOT':
            trig_dict[trig[0]] = NotTrigger(trig[2])
        elif trig[1] == 'AND':
            trig_dict[trig[0]] = AndTrigger(trig_dict[trig[2]], trig_dict[trig[3]])
        elif trig[0] == 'ADD':
            for x in range(1, len(trig)):
                trig_list.append(trig_dict[trig[x]])
    return trig_list



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Minneapolis")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("black")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

