#There are general test questions in this program.
test = {
    "Question(Soru) 1":{
        "Question": "Which team won the most trophies in Turkey?(Türkiye'de en çok  kupa kazanan takım hangisidir?)",
        "answer": "Galatasaray"
    },"Question(Soru) 2":{
        "Question": "What Netflix show had the most streaming views in 2021?(Netflix'de 2021 yılında en çok izlenen programı nedir?)",
        "answer": "Squid Game"
    },"Question(Soru) 3":{
        "Question": "Which email service is owned by Microsoft?(Hangi e-posta hizmeti Microsoft'a aittir?)",
        "answer": "Hotmail"
    },"Question(Soru) 4 ":{
        "Question": "Which fashion brand made the “Genius Jeans” that became part of the Guinness World Records?(Guinness Rekorlar Kitabı'na giren Genius Jeans'i hangi moda markası yaptı?)",
        "answer": "Gucci"
    },
}
score = 0
for key, value in test.items():
    print(value['Question'])
    answer = input("Answer(Cevap)?")
    
    if answer.lower() == value['answer'].lower():
        print('Correct(Doğru)')
        score = score + 1
        print("Your score is(Skorun):" + str(score))
    else:
        print("Wrong(Yanlış)!")
        print("The answer is(Cevabı) :" + value['answer'])
        print("Your score is(Skorun):" + str(score))

#Open source code, edited by Yağız Köylü with additions.

        