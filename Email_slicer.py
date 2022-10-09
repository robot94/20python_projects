#This is an email slicer

email_input = input('Enter an email address: ')
print(f"The emial that you inputed is: {email_input}") 

# 👇️ split with @ separator
first_split = email_input.split('@')
print(first_split)

prefix, suffix = first_split

# 👇️ split with . separator
second_split = suffix.split('.')
print(second_split)

Second_level_domain, TLD = second_split
print(f"The top level Domain of this emial address is: {TLD}")
print(f"The second level Domain of this emial address is: {Second_level_domain}")