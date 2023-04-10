from romeo_and_juliet import PLAY

def get_words(text):
  text = text.lower()
  text = text.replace("\n", " ")
  text = text.replace(".", " ")
  text = text.replace(",", " ")
  text = text.replace(";", " ")
  splitted = text.split(' ')
  return splitted

def words_frequency(words):
  dict_words = {}
  for word in words:
    if word not in dict_words:
      dict_words[word] = 0
    dict_words[word] += 1
    if dict_words[word] == 72:
      del dict_words[word]
  return dict_words

def top_n_words(freq, n):
  tup_list = list(freq.items())
  counter = 0
  sorted_lst = sorted(tup_list, key=lambda x: x[1], reverse=True)

  for pair in sorted_lst:
    if counter < 50:
      print(f"{pair[0]}: {pair[1]}")
    counter += 1

  return sorted_lst

def main():
  play_script = get_words(PLAY[:1000])
  top_n_words(words_frequency(play_script),50)

if __name__ == "__main__":
  main()