from duckduckpy import query


# put query in dict
def validPrez(prez):
    #prez = "Obama"
    response = query('presidents of the united states', container='dict')  # search duckduckgo for presidents

    # search for prez in data
    for i in response['related_topics']:
        if prez in i['text']:
            return "yes"



