from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    read = fields.Bool(required=True)

class BookUpdateSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    read = fields.Bool()
    