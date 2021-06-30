import re
from api.database import db, ma
from .answer import Answer
import datetime


class ExampleAnswer(db.Model):
    __tablename__ = "example_answer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    example_sentence = db.Column(db.String(200), nullable=False)
    answer_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Answer %r>" % self.name

    def getExampleAnswerList(request_dict):

        index_id = request_dict["index_id"]

        example_answer_list = (
            db.session.query(
                ExampleAnswer.id,
                ExampleAnswer.example_sentence,
                ExampleAnswer.answer_id,
                Answer.index_id,
            )
            .join(Answer, ExampleAnswer.answer_id == Answer.id)
            .filter(
                Answer.index_id == index_id,
            )
            .all()
        )

        if example_answer_list == None:
            return []
        else:
            return example_answer_list


class ExampleAnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ExampleAnswer
        load_instance = True
        fields = (
            "id",
            "example_sentence",
            "answer_id",
            "index_id",
        )
