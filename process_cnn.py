# https://machinelearningmastery.com/prepare-news-articles-text-summarization/

from io import open	
from os import listdir
 
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, encoding='utf-8')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# split a document into news story and highlights
def split_story(doc):
	# find first highlight
	index = doc.find('@highlight')
	# split into story and highlights
	story, highlights = doc[:index], doc[index:].split('@highlight')
	# strip extra white space around each highlight
	highlights = [h.strip() for h in highlights if len(h) > 0]
	return story, highlights
 
subsample = False
# load all stories in a directory
def load_stories(directory):
	stories = list()
	if subsample:
		dirr = listdir(directory)[0:10]
	else:
		dirr = listdir(directory)
	for i, name in enumerate(dirr):
		filename = directory + '/' + name
		# load document
		doc = load_doc(filename)
		# split into story and highlights
		story, highlights = split_story(doc)
		# store
		stories.append({'story':story, 'highlights':highlights})
		if i %1000 == 0:
			print('Processed story {}'.format(i))
	return stories
 
# load stories
directory = 'data/cnn/stories/'
stories = load_stories(directory)
print('Loaded Stories %d' % len(stories))
print(stories[0])

import json
with open('data/data.json', 'wb') as outfile:
    json.dump(stories, outfile)
