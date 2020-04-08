# censor_dispenser

codecademy project

https://www.codecademy.com/practice/projects/censor-dispenser

2.Write a function that can censor a specific word or phrase from a body of text, and then return the text.

Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms from the first email, email_one. Mr. Cloudy doesn’t care how you censor it, he just wants it done.

3.Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the te xt.

Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

4. The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”

Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

5.This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”

Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.
6.Great job! The Board of Investors is none the wiser to what is going on in the lab and Mr. Cloudy is very happy.

Take a moment to look over your functions, are they the best they can be? As a challenge, make sure they:

    Handle upper and lowercase letters.
    Handle punctuation.
    Censor words while preserving their length.


