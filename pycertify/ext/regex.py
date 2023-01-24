import re

#função regex, sem utilizade no código por enquanto
def answers_regex(answers):
    answers_re = re.search('(^[a-z])', answers).group()
    return answers_re
