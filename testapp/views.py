from django.shortcuts import render
import xml.etree.ElementTree as et
from xml.etree import cElementTree as ElementTree
from testapp.utils import XmlDictConfig


def show(request):
    return render(request,'show.html')
def handle_xml_upload(request):
    xmlfile = request.FILES['xmlfile']
    print(type(xmlfile))
    # tree = et.parse(xmlfile)
    # print(tree)
    # r
    tree = ElementTree.parse(xmlfile)
    root = tree.getroot()
    xmldict = XmlDictConfig(root)
    if xmldict['Policy']['Preferences']['PluginsPreferences']['item']:
        dict1=xmldict['Policy']['Preferences']['PluginsPreferences']['item']
        print(dict1)
        return render(request,'index.html',{'dict1':dict1})
    msg='Invalid Data'
    return render(request, 'show.html', {'msg':msg})