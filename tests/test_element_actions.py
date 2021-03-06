URL = 'http://the-internet.herokuapp.com'


def test_check_single_box(py):
    py.visit(f'{URL}/checkboxes')
    assert py.get('[type="checkbox"]').check().should().be_checked()
    assert py.get('[type="checkbox"]').uncheck().is_checked() is False


def test_check_many_boxes(py):
    py.visit(f'{URL}/checkboxes')
    assert py.find('[type="checkbox"]').check(allow_selected=True).are_checked()


def test_select_dropdown(py):
    py.visit(f'{URL}/dropdown')
    py.get('#dropdown').select('2')


def test_drag_to_with_selector(py):
    py.visit('https://the-internet.herokuapp.com/drag_and_drop')
    py.get('#column-a').drag_to('#column-b')
    assert py.get('#column-b > header').should().have_text('A')


def test_drag_to_with_element(py):
    py.visit('https://the-internet.herokuapp.com/drag_and_drop')
    column_b = py.get('#column-b')
    py.get('#column-a').drag_to_element(column_b)
    assert column_b.get('header').should().have_text('A')


def test_hover(py):
    py.visit('https://the-internet.herokuapp.com/hovers')
    assert py.get('.figure').hover().contains('View profile').should().be_visible()
