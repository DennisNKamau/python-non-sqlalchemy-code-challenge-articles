#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create instances for testing
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine1 = Magazine("Tech Weekly", "Technology")
    magazine2 = Magazine("Health Monthly", "Health")

    # Add articles
    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author1.add_article(magazine2, "Healthy Living Tips")
    article3 = author2.add_article(magazine1, "Advances in Robotics")
    article4 = author1.add_article(magazine1, "AI in Healthcare")

    # Test properties and methods
    print(author1.name)  # John Doe
    print(magazine1.name)  # Tech Weekly
    print(article1.title)  # The Future of AI

    print(author1.articles())  # [article1, article2, article4]
    print(author1.magazines())  # [magazine1, magazine2]
    print(magazine1.articles())  # [article1, article3, article4]
    print(magazine1.contributors())  # [author1, author2]

    print(magazine1.article_titles())  # ["The Future of AI", "Advances in Robotics", "AI in Healthcare"]
    print(magazine1.contributing_authors())  # None (no authors with more than 2 articles for this magazine)

    print(Magazine.top_publisher())  # magazine1 (most articles)

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
