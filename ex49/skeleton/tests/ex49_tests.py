from nose.tools import *
try:
    from ex48 import lexicon, ex49
except ImportError:
    import sys
    sys.path.append("..")
    from ex48 import lexicon, ex49


def test_Sentence():
    result = ex49.Sentence(('noun', 'bear'), ('verb', 'go'), ('direction', 'north'))
    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'go')
    assert_equal(result.object, 'north')

def test_peek():
    word_list = lexicon.scan("go north")
    assert_equal(ex49.peek(word_list), 'verb')

    word_list = lexicon.scan("")
    assert_equal(ex49.peek(word_list), None)

def test_match():
    word_list = lexicon.scan("go north")
    assert_equal(ex49.match(word_list, 'verb'), ('verb', 'go'))

    word_list = lexicon.scan("go north")
    assert_equal(ex49.match(word_list, 'direction'), None)

    word_list = lexicon.scan("")
    assert_equal(ex49.match(word_list, 'verb'), None)

def test_parse_verb():
    word_list = lexicon.scan("go to north")
    assert_equal(ex49.parse_verb(word_list), ('verb','go'))

    word_list = lexicon.scan("WSAD")
    assert_raises(ex49.ParserError, ex49.parse_verb, word_list)

def test_parse_object():
    word_list = lexicon.scan("bear go to the north")
    assert_equal(ex49.parse_object(word_list), ('noun','bear'))

    word_list = lexicon.scan("go north")
    assert_raises(ex49.ParserError, ex49.parse_object, word_list)

def test_parse_subject():
    word_list = lexicon.scan("go north")
    result = ex49.parse_subject(word_list, ('noun', 'bear'))
    assert_equal(result.subject,'bear')
    assert_equal(result.object,'north')
    assert_equal(result.verb,'go')

def test_parse_sentence():
    word_list = lexicon.scan('bear go north')
    assert_equal(ex49.parse_sentence(word_list).__dict__, {'verb':'go', 'object':'north', 'subject':'bear'})
