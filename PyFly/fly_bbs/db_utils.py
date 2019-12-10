from bson import ObjectId

from .extensions import mongo


def get_option(code, default=None):
    return mongo.db.options.find_one({'code': code}) or default


def _process_filter(filter1):
    if filter1 is None:
        return 
    _id = filter1.get('_id')
    if _id and not isinstance(_id, ObjectId):
        filter1['_id'] = ObjectId(_id)


def get_list(collection_name, sort_by=None, filter1=None, size=None):
    _process_filter(filter1)
    result = mongo.db[collection_name].find(filter1)
    if sort_by:
        result = result.sort(sort_by[0], sort_by[1])
    if size:
        result = result.limit(size)
    return list(result)


