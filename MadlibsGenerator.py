# def madlibs_generator():
#     print("Welcome to Madlibs Generator!")
#     print("Please provide the following words to complete the story:")
    
#     adjective = input("Enter an adjective: ")
#     noun = input("Enter a noun: ")
#     place = input("Enter a place: ")
#     verb1 = input("Enter a verb: ")
#     noun_plural = input("Enter a plural noun: ")
#     verb2 = input("Enter another verb: ")
#     adverb = input("Enter an adverb: ")
#     preposition = input("Enter a preposition: ")
#     object = input("Enter an object: ")
#     something_amazing = input("Enter something amazing: ")
    
#     story = f"""
#     Once upon a time, there was a {adjective} {noun} who lived in a {place}.
#     Every day, they would {verb1} with their {noun_plural} and {verb2} {adverb}.
#     One day, they found a {adjective} {noun} hiding {preposition} a {object}.
#     They decided to {verb1} it and were surprised to find {something_amazing}.
#     From that day on, they became known as the {adjective} {noun_plural} of {place}
#     and lived {adverb} ever after.
#     """
    
#     print("\nHere's your Madlibs story:\n")
#     print(story)

# madlibs_generator()

with open('story.txt', 'r') as f:
    story = f.read()
    
words = set()
start_of_word = -1

start = '<'
end = '>'
    
for i, char in enumerate(story):
    if char == start:
        start_of_word = i
    
    if char == end and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1
        
answers = {}

for word in words:
    answer = input("Enter a word for "+ word +": ")
    answers[word] = answer
    
for word in words:
    
    story = story.replace(word, answers[word])

print(story)