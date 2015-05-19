'''
Created on 14/05/2015

@author: jeevananthamganesan
'''
import sys
import pandas as pd
from collections import defaultdict
from xml.etree import ElementTree


def filterextract(comp,x):
    d = defaultdict(dict)
    for i in comp.iter('Properties'):
        for j in i.iter('Configuration'):
            for l in j.iter('Mode'):
                if l.text == 'Simple':
                    for k in i.iter('DefaultAnnotationText'):
                        d[x]['Field'] = 'See the expression'
                        d[x]['Expression'] = k.text
                        d[x]['Function'] = 'Filter'
                elif l.text == 'Custom':
                    d[x]['Field'] = 'See the expression'
                    d[x]['Expression'] = j.find('Expression').text
                    d[x]['Function'] = 'Filter'
                x = x + 1
    return(d,x)
    

def formulaextract(comp,x):
    d = defaultdict(dict)
    for i in comp.iter('FormulaField'):
        FieldName = i.get('field')
        d[x]['Field'] = FieldName
        Expression = i.get('expression')
        d[x]['Expression'] = Expression
        d[x]['Function'] = 'Formula'
        x = x + 1
    return(d,x)


def treegeneration(AlteryxFileName):
    with open(AlteryxFileName, 'rt') as f:
        tree = ElementTree.parse(f)
    root = tree.getroot()
    mydf = {}

    x = 0
    for child in root.iter('Node'):
        for i in child.findall('GuiSettings'):
        #print i.attrib.get('Plugin')
            if i.attrib.get('Plugin') == 'AlteryxBasePluginsGui.Filter.Filter':
                out,x = filterextract(child,x)
                mydf.update(out)
                x = x + 1
            elif i.attrib.get('Plugin') == 'AlteryxBasePluginsGui.Formula.Formula':
                out,x = formulaextract(child,x)
                mydf.update(out)
                x = x + 1
            else:
                x = x + 1
                pass
    
    mydfv = pd.DataFrame(mydf)
    mydfv2 = mydfv.T    
    return mydfv2


if __name__ == '__main__':
    AlteryxFileName = sys.argv[1]
    outputcsv = sys.argv[2]
    mydfv2 = treegeneration(AlteryxFileName)
    mydfv2.to_csv(outputcsv)
