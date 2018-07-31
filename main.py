import json

from file_utils import FileUtils

FILE_NAME = 'data/jsons/Aareal-AnnualReport-2010.json'
TYPE = 'type'
PARAGRAPH = 'paragraph'
CONTENT = 'content'

try:
    with open(FILE_NAME) as f:
        data = json.load(f)
        for item in data:
            typeDoc = item[TYPE]
            if typeDoc == PARAGRAPH:
                content = item[CONTENT]
                print content
except:
    FileUtils.fix_json(FILE_NAME)
    with open(FILE_NAME) as f:
        data = json.load(f)
        for item in data:
            typeDoc = item[TYPE]
            if typeDoc == PARAGRAPH:
                content = item[CONTENT]
                print content