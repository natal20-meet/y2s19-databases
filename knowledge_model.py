from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "Topics to learn about"
	topic_id= Column(Integer, primary_key = True )
	art_title = Column(String)
	wiki_link = Column(String)
	rating = Column(Integer)
	def __repr__(self):
		return ("if you want to learn about {}\n, "

				"you should check this link on wikipedia {}\n, "
				"we gave it a rating of {}").format(
					self.art_title,
					self.wiki_link,
					self.rating)

#article_1 = Knowledge(art_title = "Quantum Physics", wiki_link = 'https://en.wikipedia.org/wiki/Quantum_mechanics', rating = 7)
#print(article_1)

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

