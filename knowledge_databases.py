from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(art_title, wiki_link, rating):
	new_article = Knowledge(
		art_title = art_title,
		wiki_link = wiki_link,
		rating = rating)
	session.add(new_article)
	session.commit()
add_article(art_title = "Quantum Mechanincs", wiki_link = "https://en.wikipedia.org/wiki/Quantum_mechanics", rating=10)

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

#print(query_all_articles())
	

def query_article_by_topic():
	article = session.query(Knowledge).filter_by(art_title="Quantum Mechanincs").first()
	return article
#print(query_article_by_topic())
	

def delete_article_by_topic():
    session.query(Knowledge).filter_by(art_title="Quantum Mechanincs").delete()
    session.commit()
delete_article_by_topic()
print(query_all_articles())
def delete_all_articles():
	pass

def edit_article_rating():
	pass