# filter_NCBI_header_by_keywords

The script takes a list of keywords (one keyword per line) and a list of NCBI headers (that includes an environmental source from which
this sequence has been isolated) and keeps only those headers that do not have a matching word in the list of keywords.


## Python script to search for strings (words) in a PDF document and highlight them

## AV 28-3-2022

#### Python version.

3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)]

### Input files
1. A txt file with a list of keywords (e.g. blood), one keyword per line. (e.g. key_words_env_source.txt)
2. A txt file with a list of headers with NCBI that includes (e.g. all_origin_col1-.txt)
e.g. Homo sapiens|DSM:22607|type strain of Christensenella minuta|Japan|**feces**|2012

The file with headers is the output of the bash command:
select lines with “|”, split fields/columns by “|”, print all columns but the first one,
grep "|" input_file | awk -F"|" '{$1=""; print $0}' | sort | uniq > aoutput.file

### Output files
- Filtered headers file (e.g. "filtered_headers.txt")
