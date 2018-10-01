
def test_person(yaml_content):
    print("Test for %s" % yaml_content['test'])
    for person in yaml_content['persons']:
        assert person['age'] == 20, "I am %s" % person['name']
