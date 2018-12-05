"""
 map() in Python:
"""
def multiply(x):
    return x*x

data=[1]
res= map(multiply,)

SELECT t.id, t.topic_name as title, tc.slug,tc.status, t.created_on, 1,t.sub_subject_id, t.subject_id, 1,tc.content as contents, tc.image,t.is_block,t.updated_on FROM `topic` as t, page_content tc WHERE t.id=tc.topic_id  
ORDER BY `tc`.`slug` ASC