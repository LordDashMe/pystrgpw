import pystrgpw


def test_it_should_generate_random_char_with_length():
    strgpw = pystrgpw.Generator()
    strgpw.length(100)
    strgpw.generate()
    assert len(strgpw.get()) == 100
