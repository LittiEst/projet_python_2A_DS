import spacy # utile pour le traitement de language naturel (NLP)
import wikipedia # utile pour le scraping "simple" de Wikipédia

# chargement de la version anglaise web de SpaCy
nlp = spacy.load('en_core_web_sm')

def subject(question):
	"""subject(question): trouve le groupe nomimal sujet de la question"""
	doc = nlp(question)

	span = doc[doc[4].left_edge.i:doc[4].right_edge.i+1]
	span.merge()

	subj = [token.text for token in doc if token.dep_ in ["nsubj", "nsubjpass"]]

	return ' '.join(word for word in subj)

def keywords(question):
	"""keywords(question): retourne les mots importants de la question"""
	doc = nlp(question)

	kw = [token.text for token in doc if token.pos_ in ["ADJ","ADP","ADV","NOUN","NUM","PROPN","VERB","X"]]

	return kw

def get_wiki_page(subj):
	"""get_wiki_page(subj): retourne la page traitant du sujet de la question"""
	page_name = wikipedia.search(subj)[0]
	
	page = wikipedia.page(page_name)

	return page.content

# exemple : on rentre une question, on identifie le sujet et les mots importants, puis on écrit la page dans un fichier
question = "Where did the World Cup take place in 1930 ?"
subj = subject(question)
kw = keywords(question)

page = get_wiki_page(subj)

f = open('page.txt','w')
f.write(str(page.encode('utf-8')))
f.close()




class ask:
	def __init__(self, question):
		self.question = question
		self.subject = subject(question)
		self.keywords = keywords(question)

	def wikipedia_page(self):
		page_name = wikipedia.search(self.subject)[0]
		page = wikipedia.page(page_name)

		print(page.url)

question_1 = ask("When is John F. Kennedy born ?")

question_1.wikipedia_page()













