#input a filename
filename = input()

#create dictionary for tv_shows
tv_shows_dictionary = {}

#import filename as a text file
with open(filename, 'r') as textfile:
    list_of_shows = textfile.readlines()
    for show in range(len(list_of_shows)):
        list_of_shows[show] = list_of_shows[show].strip('\n')
    for show in range(len(list_of_shows)):
        if show % 2 == 0 and (list_of_shows[show] not in tv_shows_dictionary):
            tv_shows_dictionary[list_of_shows[show]] = [list_of_shows[show+1]]
        elif show % 2 == 0 and (list_of_shows[show] in tv_shows_dictionary):
            tv_shows_dictionary[list_of_shows[show]] += [list_of_shows[show+1]]
print(tv_shows_dictionary)
with open('output_keys.txt', 'w') as output_keys:
    for key in sorted(tv_shows_dictionary.keys()):
        string1 = key.lstrip('0') + ': '
        output_keys.write(string1)
        for value in range(len(tv_shows_dictionary[key])):
            if value < len(tv_shows_dictionary[key])-1:
                string2 = tv_shows_dictionary[key][value] + '; '
                output_keys.write(string2)
            else:
                string3 = tv_shows_dictionary[key][value] + '\n'
                output_keys.write(string3)
with open('output_titles.txt', 'w') as output_titles:
    show_list = []
    for value in tv_shows_dictionary.values():
        show_list += value
    show_list.sort()
    for show in show_list:
        string4 = show + '\n'
        output_titles.write(string4)

