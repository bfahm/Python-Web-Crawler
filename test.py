stri = "Taleb Tawatha (or Twatha, Arabic: طالب طواطحه‎, Hebrew: טאלב טוואטחה‎; born 21 June 1992)"
def rem_parenthesis(paragraph):
    paragraph = str(paragraph)
    open_par = paragraph.find("(")
    print(open_par)
    close_par = paragraph.find(")")
    print(close_par)


rem_parenthesis(stri)