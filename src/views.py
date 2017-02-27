# -*- coding: utf-8 -*-
import re, time, json, logging, hashlib, base64, asyncio
from src.core.webcore import get,post
from src.models import User

@get('/')
async def index():
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
    