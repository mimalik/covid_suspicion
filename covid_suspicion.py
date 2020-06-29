# By Mihir Malik
# This is a program to calculate coronavirus
# suspicion levels of a patient's statement
############################################
import nltk
import sys

# A list of useless words in English
stopwords = nltk.corpus.stopwords.words('english')

# return null if the word is a useless word
def normalize(token):
    if token in stopwords:
        token = None
    return token

# convert a statement into a list devoid of useless filler (stopwords) words
def process_statement(statement):
    cleanList = []
    dirtyList = nltk.word_tokenize(statement)
    if dirtyList != None:
        for word in dirtyList:
            word = word.lower()
            if (normalize(word) != None):
                cleanList.append(normalize(word))
        cleanList.sort()
    return cleanList

# perimeter class data type for each symptom for the virus
class branch:
    root = ""
    leaves = []
    def __init__(self, core, symptom):
        self.leaves = []
        symptom = process_statement(symptom)
        self.root = core.lower()
        for word in symptom:
            self.leaves.append(word)

# primary class containing a suspicion calculation diagnosis
class tree_of_symptoms:
    trunk = []
    branches = []
    # Function to add a symptom to the tree
    def add_branch(self, core, symptom):
        newBranch = branch(core, symptom)
        self.branches.append(newBranch)
    # Function to check if the word is a suspicious word in the tree
    def parse(self, word):

        if word in self.trunk:
            return 100

        else:
            for branch in self.branches:
                if word == branch.root:
                    return 5
            for branch in self.branches:
                for leaf in branch.leaves:
                    if word == leaf:
                        return 1
        return 0

    def __init__(self):
        # if these words are in the statement then we definitely suspect this
        # to be a coronavirus case
        self.trunk = ["corona", "coronavirus", "covid", "covid-19"]
        # For now I have manually added each symptom stated by the cdc
        self.add_branch("virus", "I think I might infected by the viral flu")
        self.add_branch("lungs", "lungs hurt and feel like they burn are burning" +
                                " or hurting and pain in the chest")
        self.add_branch("difficult", "difficulty breathing exhausted cannot hold breath")
        self.add_branch("breathe", "hard to breathe or hold breath shortness")
        self.add_branch("fever", "fever causes body temprature to be high elevated" +
                            " above 104 degrees farenheit")
        self.add_branch("cough", "frequent coughting and thick phlegm")
        self.add_branch("china", "travalled south east asia in the past year")
        self.add_branch("italy", "travelled europe in the past 3 4 months")
        self.add_branch("york", "travelled to new york in the past 5 6 months")
        self.add_branch("vomit", "vomitted threw up puked hurled uneasy stomach belly ")
        self.add_branch("cold", "chilly chills shivering shaking")
        self.add_branch("smell","loss of sense since recently")
        self.add_branch("taste","loss of sense since recently")
        self.add_branch("flight","travelled recently on an airplane")
        self.add_branch("cold","chills shivering or feeling chilly or a runny nose and sneezing")
        self.add_branch("ache","muscle body or headache")
        self.add_branch("congested", "runny nose")
        self.add_branch("diarrhea", "uncontrollable loose motion")
        self.add_branch("fatigue", "tired weak low energy")
        self.add_branch("nausea", "vomitted threw up puked hurled uneasy stomach belly ")



# Calculator of the suspicion level of the statement
def suspicion(wordList):
    tree = tree_of_symptoms()
    # The probability feature for suspicion of coronavirus if above 20 we say
    # it's definitely coronavirus
    suspicious = 0
    for word in wordList:
        suspicious += tree.parse(word)
    return suspicious

# Main Function for this code
def main():
    if(len(sys.argv)==1):
        statement = input("Describe your symptoms: ")
        symptoms = process_statement(statement)
        probability = suspicion(symptoms)

    else:
        arguments = list(set(sys.argv))
        arguments.remove(arguments[0])
        for word in arguments:
            if word in stopwords:
                arguments.remove(word)
        print(str(arguments))
        probability = suspicion(arguments)
    if (probability>30):
        print("Definitely CoVID-19")
    elif (probability>4):
        print("Possibly CoVID-19")
    else:
        print("Regular Patient")

if __name__ == "__main__":
    main()
