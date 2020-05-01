user_name,single_character=input('enter user name and a single character comma seperated ').split(',')
print(f'length of name is:- {len(user_name)}')
print(f'character count {user_name.strip().lower().count(single_character.strip().lower())}')
