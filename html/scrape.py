import urllib.request, re

# Fetches the raw HTML content served by a specified URL
def getPageContent(url):
    connection = urllib.request.urlopen(url)
    rawContent = connection.read().decode("utf-8")
    connection.close()
    return rawContent

# Filters out HTML tags
def cleanHTML(rawContent):
    regEx = re.compile('<.*?>')
    cleanedContent = re.sub(regEx, '', rawContent)
    return cleanedContent

# Split content into a list of words and remove stopwords
def wordList(cleanedContent):
    cleanedContent = cleanedContent.lower()
    stopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    rawList = cleanedContent.split()
    cleanList = []
    for word in rawList:
        if word not in stopWords:
            cleanList.append(word)
    return cleanList
    
# Return a count of how many instances a word appears in a given word list
def getCount(word, cleanList):
    return cleanList.count(word)

# Return a sorted dictionary of all words and the number of times they appear
def getCountDict(cleanList):
    wordDict = {word:cleanList.count(word) for word in cleanList}
    sortedDict = {k: v for k, v in sorted(wordDict.items(), key=lambda item: item[1])}
    return sortedDict

# Working Example
#rawContent = getPageContent('https://en.wikipedia.org/wiki/Python_(programming_language)')
#cleanedContent = cleanHTML(rawContent)
#cleanList = wordList(cleanedContent)
#print(getCount('mutable', cleanList))
#print(str(getCountDict(cleanList)))