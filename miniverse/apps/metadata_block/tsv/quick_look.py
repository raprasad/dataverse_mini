import csv

ftype_map = dict(text='CharField'\
                , textbox='TextField'\
                , date='DateField'\
                , url='URLField'\
                , email='EmailField'\
                )

class RowInfo:
    attrs = ['datasetField', 'name', 'title', 'description', 'watermark', 'fieldType', 'displayOrder', 'advancedSearchField', 'allowControlledVocabulary', 'allowmultiples', 'facetable', 'showabovefold', 'required', 'parent', 'metadatablock_id']
    
    def __init__(self, row_info):
        for idx, attr in enumerate(self.attrs):
            self.__dict__[attr] = row_info[idx]


    def get_defn(self):
        if self.allowmultiples == 'TRUE':
            if self.required == 'FALSE':
                defn = '%s = models.ManyToManyField(blank=True, null=True)' % (self.name)
            else:
                defn = '%s = models.ManyToManyField()' % (self.name)
            return defn
            
        if self.required == 'FALSE':
            req= 'blank=True'
        else:
            req = ''
            
        defn = '%s = models.%s(%s, help_text="%s")' % (self.name, ftype_map[self.fieldType], req, self.description)
        if defn.find('CharField') > -1:
            defn = defn.replace('(', '(max_length=255')
            if defn.find('255blank') > -1:
                defn=defn.replace('255blank', '255, blank')
        return defn
    
    @staticmethod
    def get_num_fields():
        return len(RowInfo.attrs)
    
fname = 'citation2.tsv'
num_fields_per_row = RowInfo.get_num_fields()
with open(fname) as tsv:
    cnt = 0
    for line in csv.reader(tsv, dialect="excel-tab"): 
        cnt +=1
        if cnt == 1: continue
        if len(line) == num_fields_per_row:
            ri = RowInfo(line)
            if ri.fieldType:
                #print '%s = models. ' % (ri.name, )
                print ri.get_defn()