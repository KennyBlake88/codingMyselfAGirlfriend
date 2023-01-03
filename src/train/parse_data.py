from convokit import Corpus, download, Conversation
movieCorpus = Corpus(download("movie-corpus"))
friendCorpus = Corpus(download("friends-corpus"))



for uttId in movieCorpus.get_utterance_ids():
    currUtt = movieCorpus.get_utterance(uttId)
    currGen = currUtt.speaker.meta.get("gender") 
    if (currGen == "m" or currGen == "?"):

    else:
        currConv: Conversation = currUtt.get_conversation()
        currGenres: list = currConv.meta.get("genre")
        if "romance" in currGenres:
            print(currUtt.text)