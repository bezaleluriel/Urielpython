import re
pattern = 'el'
pre_pattern = '^he'
post_pattern = 'lo$'
char_counter_pattern = '.....'
# check if some letter from [] is good
is_some_letter_pattern = 'h[ea]llo'
range_pattern = '[b-j]ello'
or_pattern = '[he|bc]llo'
#
trick_pattern = '[1-9]0?'

#TODO - NOT PREFECT
phone_pattern = '^05'
phone_len_pattern = r'..\d\d\d\d\d\d\d\d'

# WORKS PERFECT
phone_pattern2 = r'^05\d-?\d{7}$'

phone_str = '0546597965'



string = 'hello'
# is in
print(re.search(pattern, string))
print(re.search(pre_pattern, string))
print(re.search(post_pattern, string))
print(re.search(char_counter_pattern, string))
print(re.search(is_some_letter_pattern, string))
print(re.search(range_pattern, string))
print(re.search(or_pattern, string))

print(re.search(phone_pattern and phone_len_pattern, phone_str))
print(re.search(phone_pattern2, phone_str))

phone_pattern3 = r'05\d-?\d{7}'
string = "uriel number is 0546597905 bla"
ans = re.search(phone_pattern3, string)
if ans is None:
    print(None)
else:
    #print(string[ans.start():ans.end()])
    print(ans[0])



def is_valid_email(email):
    # ^  # start of string
    # [a - zA - Z0 - 9._ % +-] +  # one or more alphanumeric characters, dots, underscores,
    #
    # # percentage signs, plus signs, or hyphens
    # @  # "@" symbol
    #
    # [a - zA - Z0 - 9. -] +  # one or more alphanumeric characters or dots
    # \.  # "." character (escaped with a backslash)
    # [a - zA - Z]
    # {2, }  # two or more alphabetical characters
    # $  # end of string
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

email = 'example@email.com'
if is_valid_email(email):
    print('Valid email address')
else:
    print('Invalid email address')


text = "we start at 08:00:00 and finish at 15:45:00, tommorow is 05-04-2023"
date_pattern = "(\d{2})-(\d{2})-(\d{4})"
x = re.search(date_pattern, text)
myday = x.group(1)
mymonth = x.group(2)
myyear = x.group(3)
print(myday, mymonth, myyear)

time_pattern = "(\d{2}):(\d{2}):(\d{2})"
x = re.search(time_pattern, text)
print(x)
x = re.findall(time_pattern, text)
print(x)
# get help on function
help(re.sub)
#TODO - NOT PERFECT
x = re.sub(time_pattern, "##:##:##", text)
print(x)

text = 'one is 1,   two is 2'
# in this regular expression split func we remove the space/s and the ',', and new lines and tabs
ans = re.split('[, \t\n]+', text)
print(ans)







