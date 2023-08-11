def head(text, num_lines):
  output = text.split('\n')
  first = output[:n]
  my_str = '\n'.join(first)
  return my_str

def tail(text, num_lines):
  output = text.split('\n')
  last = output[-n:]
  my_str = '\n'.join(last)
  return my_str
