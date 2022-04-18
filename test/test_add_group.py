from model.group import Group


def test_add_group(app):
    app.group.create(Group(name='dgfdgf', header='fdgfdg', footer='gfgfh'))


def test_add_empty_group(app):
    app.group.create(Group(name='', header='', footer=''))