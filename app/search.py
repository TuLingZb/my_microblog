from flask import current_app


"""
使用elasticsearch 使用
"""

def add_to_index(index,model):
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model,field)
    print("添加索引",index,model.id,payload)
    current_app.elasticsearch.index(index=index,id=model.id,body=payload,doc_type='doc')

def remove_from_index(index,model):
    if not current_app.elasticsearch:
        return
    print("删除索引",index,model.id)
    current_app.elasticsearch.delete(index=index,id=model.id,doc_type='doc')

def query_index(index,query,page,per_page):
    if not current_app.elasticsearch:
        return [],0

    # body = {'query':{'multi_match':{'query':str(query),'fields':['*']}},
    #           'from':(page-1)*per_page,'size':per_page}
    # body = {'query':{'match':{'body':str(query)}},
    #           'from':(page-1)*per_page,'size':per_page}
    body = {'query':{'wildcard':{'body':"*" + str(query) + "*"}},
              'from':(page-1)*per_page,'size':per_page}
    print("要查询的index",index,query,body)
    search = current_app.elasticsearch.search(
        index=index,
        body=body,
        doc_type='doc'
    )
    print(search)
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids,search['hits']['total']
