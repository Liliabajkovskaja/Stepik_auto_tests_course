
#Функция должна проверить вхождение строки substring
# в строку full_string с помощью оператора assert и,
# в случае несовпадения, предоставить исчерпывающее сообщение об ошибке
# . expected 'some_value' to be substring of 'fulltext'



def test_substring(full_string, substring):
    assert substring  in full_string, f"expected '{substring}' to be substring of '{full_string}'"
#assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
test_substring('some_text','some')