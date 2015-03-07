# This is the main file that will hold all of the tables for stories and related tables

# Pen names
db.define_table('PenName',
  Field('author', 'reference auth_user', requires=IS_IN_DB(db, 'auth_user.id', '%(username)s')),
  Field('name', 'string', requires=IS_NOT_IN_DB(db, 'PenName.name')),
  Field('rating', 'double', requires=IS_FLOAT_IN_RANGE(0, 10)),
  Field('numberOfVotes', 'double', default=0),
  Field('stories', 'list:reference Story', requires=IS_IN_DB(db, 'Story.id', '%(title)s by %(author)s', multiple=True)),
  Field('description', 'text'),
  Field('picture', 'upload', requires=(IS_IMAGE() or not IS_NOT_EMPTY())),
  Field('followers', 'list:reference auth_user', requires=IS_IN_DB(db, 'auth_user.id', '%(username)s', multiple=True)),
  format='%(name)s'
)

# The story node
db.define_table('Story',
  Field('title', 'string', requires=IS_NOT_EMPTY()),
  Field('author', 'reference PenName', requires=IS_IN_DB(db, 'PenName.id', '%(name)s')),
  Field('timestamp', 'datetime', requires=IS_NOT_EMPTY()),
  Field('children', 'list:reference Story', requires=IS_IN_DB(db, 'Story.id', '%(title)s by %(author)s', multiple=True)),
  Field('numberOfChildren', 'double', default=0),
  Field('parent', 'reference Story', requires=IS_EMPTY_OR(IS_IN_DB(db, 'Story.id', '%(title)s by %(author)s'))),
  Field('text', 'text'),
  Field('tags', 'list:string'),
  Field('genre', 'list:string'),
  Field('rating', 'double', requires=IS_FLOAT_IN_RANGE(0, 10)),
  Field('numberOfVotes', 'double', default=0),
  Field('views', 'integer'),
  format='%(title)s by %(author)s'
)

# Comments about stories
db.define_table('Comment',
  Field('author', 'reference PenName', requires=IS_IN_DB(db, 'PenName.id', '%(name)s')),
  Field('timestamp', 'datetime', requires=IS_NOT_EMPTY()),
  Field('text', 'text'),
  Field('story', 'reference Story'),
  Field('comments', 'list:reference Comment', requires=IS_IN_DB(db, 'Comment.id', '%(text)s by %(author)s', multiple=True)),
  format='%(text)s by %(author)s'
)
