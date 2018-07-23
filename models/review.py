#!/usr/bin/python3
'''
    Implementation of the Review class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = 'reviews'
    user_id = Column(String(60), ForeignKey('users.id', ondelete='cascade'), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id', ondelete='cascade'), nullable=False)
    text = Column(String(1024), nullable=False)
