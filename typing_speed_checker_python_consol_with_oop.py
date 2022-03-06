# created by pavan 2022
import re
import time
import random

t1 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."
t2 = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form,"
t3 = "All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary,"
t4 = "encompasses the social behavior and norms found in human societies, as well as the knowledge, beliefs, arts, laws, customs"
t5 = "India is a country in South Asia whose name comes from the Indus River. The name 'Bharata' is used as a designation for the country in their constitution"
lista = [t1, t2, t3, t4, t5]
text = random.choice(lista)  # this function from random module that randomly select script
splt_text = re.split("\s", text)  # using reg ex's split function convert string into list with respect to space
splt_text_length = (len(splt_text))  # actual words in string in int
#lets apply object oriented programing here
class type:
    def wpma_pass (self,host, guest, length):  # this function takes two lists and compare every element of host with guest
        flag_1 = 0
        flag_2 = 0
        while True:
            for i in range(length):
                if guest[i] in host:
                    flag_1 = flag_1 + 1
                if guest[i] not in host:
                    flag_2 = flag_2 + 1
            return [flag_1, flag_2];
            break;

    def lengt_of_user_In(self,userin):
        i = len(userin)
        return i;

    def wpmcalculator(self,right_word, time_that_user_took_in_minutes):
        iowa = right_word[0] / time_that_user_took_in_minutes
        return iowa;

    def wrong_words(self,rightwords):
        return (print("you hit:\ ", rightwords[1], "wrong words"));

    def right_q(self,righwords):
        return (print("you hit ☺ ", righwords[0], "correct words"));

    def secon_to_minute_converter(self,sec):
        minutes = sec / 60
        return minutes;

    def accuracy(self,correct, length):
        i = correct / length * 100
        return i;

    def speed_reaction(self,wpmspeed):
        if wpmspeed > 50:
            return print("you are genius");
speed=type()#creating object named speed
print("welcome to 'type speed metre' check your typing speed and accurecy")
response = str(input("would you like to begine with thise test:/|\: (yes/no)"))
response_1=(response.lower())
if response_1 == "yes":
    print("-------------------------------------------------------------------------")
    print("we will throw 1 line at time ready!!!!!!!!!")
    print("-------------------------------------------------------------------------")
    res = str(input(" will start ready (yes/no)"))
    res_1=(res.lower())
    if res_1 == "yes":
        print(text)
        start = time.time()
        user_respose = str(input())
        end = time.time()
        time_to_type_sec = (end - start)
        split_user_response = re.split("\s", user_respose)
        length_of_user_response = speed.lengt_of_user_In(split_user_response)
        right_words = speed.wpma_pass(splt_text, split_user_response, length_of_user_response)
        time_to_type_min = speed.secon_to_minute_converter(time_to_type_sec)
        wpmspeed = speed.wpmcalculator(right_words, time_to_type_min)
        wrong = (speed.wrong_words(right_words))
        right = (speed.right_q(right_words))
        acc=speed.accuracy(right_words[0],splt_text_length)
        print("you are accuracy is ",acc)
        fs=(speed.speed_reaction(wpmspeed))
        print("you type around ", wpmspeed, " words per minutes ",fs)
    else:
        print("bye")
else:
    print("bye")





