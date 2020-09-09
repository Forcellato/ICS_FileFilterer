def _check_in(obj, string):
    for i in obj:
        if i in string:
            return True
    return False


def _check_not_in(obj, string):
    for i in obj:
        if i in string:
            return False
    return True


def create_condition(dictionary):
    res = Condition()
    res.locations['in'] = dictionary['location']['in']
    res.locations['not_in'] = dictionary['location']['not_in']
    res.summaries['in'] = dictionary['summaries']['in']
    res.summaries['not_in'] = dictionary['summaries']['not_in']
    res.descriptions['in'] = dictionary['descriptions']['in']
    res.descriptions['not_in'] = dictionary['descriptions']['not_in']
    res.dtstarts['in'] = dictionary['dtstarts']['in']
    res.dtstarts['not_in'] = dictionary['dtstarts']['not_in']
    res.dtends['in'] = dictionary['dtends']['in']
    res.dtends['not_in'] = dictionary['dtends']['not_in']
    res.exdates['in'] = dictionary['exdates']['in']
    res.exdates['not_in'] = dictionary['exdates']['not_in']
    return res


class Condition:
    def __init__(self):
        self.locations = {"in": [], "not_in": []}
        self.summaries = {"in": [], "not_in": []}
        self.descriptions = {"in": [], "not_in": []}
        self.dtstarts = {"in": [], "not_in": []}
        self.dtends = {"in": [], "not_in": []}
        self.exdates = {"in": [], "not_in": []}

    def check_location(self, string):
        return _check_in(self.locations['in'], string) or _check_not_in(self.locations['not_in'], string)

    def check_summaries(self, string):
        return _check_in(self.summaries['in'], string) or _check_not_in(self.summaries['not_in'], string)

    def check_descriptions(self, string):
        return _check_in(self.descriptions['in'], string) or _check_not_in(self.descriptions['not_in'], string)

    def check_dtstarts(self, string):
        return _check_in(self.dtstarts['in'], string) or _check_not_in(self.dtstarts['not_in'], string)

    def check_dtends(self, string):
        return _check_in(self.dtends['in'], string) or _check_not_in(self.dtends['not_in'], string)

    def check_exdates(self, string):
        return _check_in(self.exdates['in'], string) or _check_not_in(self.exdates['not_in'], string)
