# Filter NCBI headers by keywords
# AV - 25-3-22

import re
import sys

#  exact match + multiple key words
keywords = []
with open("key_words_env_source.txt") as list_of_keywords:
    for word in list_of_keywords:
        if word.strip():
            keywords.append(word.strip())
keywords = [word for word in keywords if "#" not in word]  # remove lines with #
keywords = [word.replace(" ", "_") for word in keywords]  # replace " " with "_"
keywords = [("_" + word + "_") for word in keywords]  # add "_" before and after each keyword
#print("\n".join(keywords))

# instead of == in string, can i check "in" line?
with open("all_origin_col1-.txt") as master_file:
    with open("filtered_NCBI_headers.txt", 'w') as search_results:
        for line in master_file:
            sub_line = "_" + re.sub(r'\W+', '_', line).rstrip("\n").lower() + "_"  # substitute all NON alphanumerics with "_"
            result = 0
            # for string_x in sub_line.split('_'):
                # if not (keyword.lower() in string.lower() for keyword in keywords):
            for keyword in keywords:
                if sub_line.find(keyword.lower()) != -1:
                    result += 1
            if result == 0:
                search_results.write(line)


# with open("filtered_NCBI_headers.txt") as file:
#     count = sum(1 for _ in file)
#     print(f"The number of entries is {count}")

with open("filtered_NCBI_headers.txt") as file:
    my_list = list(file)
    print(f"The number of entries is {len(my_list)}")
    print(f"The number of uniques entries is {len(set(my_list))}")

#############
## TESTING ##
#############

# keywords = []
# with open("key_words_env_source.txt") as list_of_keywords:
#     for word in list_of_keywords:
#         if word.strip():
#             keywords.append(word.strip())
# keywords = [word for word in keywords if "#" not in word] # remove lines with #
# #print(keywords)


# with open("all_origin_col1-.txt") as master_file:
#     with open("filtered_headers.txt", 'w') as search_results:
#         for line in master_file:
#             if not any(keyword in line for keyword in keywords):
#                 search_results.write(line)


# # filter out duplicates
# lines_seen = set() # holds lines already seen
# with open("filtered_headers.txt") as filtered_file:
#     with open("filtered_headers_uniq.txt", 'w') as search_results:
#         for line in filtered_file:
#             if line not in lines_seen:
#                 search_results.write(line)
#                 lines_seen.add(line)


#exact match

# with open("all_origin_col1-.txt") as master_file:
#     with open("filtered_headers_exact.txt", 'w') as search_results:
#         for line in master_file:
#             pattern = re.compile(f"^{word}\\b")
#             print(pattern)
#             if not any(pattern.search(line, re.IGNORECASE) for word in keywords):
#                 print(line)
#                 search_results.write(line)

# with open("all_origin_col1-.txt") as master_file:
#     with open("filtered_headers_exact.txt", 'w') as search_results:
#         for line in master_file:
#             for word in keywords:
#                 pattern = re.compile(f"\\b{word}\\b")
#                 print(pattern)
#                 #if not (line.startswith(pattern) for word in keywords):
#                 if not any(pattern.search(line, re.IGNORECASE)):
#                     search_results.write(line)


# with open('search.txt','r') as f1, open("keywords.txt") as f2:
#     st = set(map(str.rstrip, f2))
#     for line in f1:
#         if any(word.lower().strip() in st for word in line.split()):
#             print(line)


# #exact match
# with open("all_origin_col1-.txt") as master_file:
#     with open("filtered_headers_exact.txt", 'w') as search_results:
#         for line in master_file:
#             sub_line = re.sub(r'\W+', '_', line).rstrip("\n ") # substitute all NON alphanumeric with "_"
#             result = 0
#             for string_x in sub_line.split('_'):
#                 # if not (keyword.lower() in string.lower() for keyword in keywords):
#                 for keyword in keywords:
#                     if keyword.lower() == string_x.lower():
#                         result += 1
#             if result == 0:
#                 search_results.write(line)



