import re

def answers_regex(answers):
    answers_re = re.search('(^[a-z])', answers).group()
    return answers_re