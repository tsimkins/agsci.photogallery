from zope.interface import implements, Interface
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATTopic
from zope.component import getUtility, getMultiAdapter
from agsci.photogallery.browser.interfaces import *
from zope.component import getUtility


"""
    Interface Definitions
"""

class PhotoGalleryView(BrowserView):

    implements(IPhotoGalleryView)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        
    def getImages(self):
        if IATTopic.providedBy(self.context):
            # ATTopic like content
            # Call Products.ATContentTypes.content.topic.ATTopic.queryCatalog() method
            # This method handles b_start internally and
            # grabs it from HTTPRequest object
            return self.context.queryCatalog(contentFilter={'portal_type' : 'Image'}, batch=False, b_size=100)

        else:
            # Folder or Large Folder like content
            # Call CMFPlone(/skins/plone_scripts/getFolderContents Python script
            # This method handles b_start parametr internally and grabs it from the request object
            return self.context.getFolderContents(contentFilter={'portal_type' : 'Image'}, batch=False, b_size=100)

    def getAspectRatio(self, i, fmt=False):
        o = i.getObject()        

        if hasattr(o, 'getSize') and hasattr(o.getSize, '__call__'):
            (w,h) = o.getSize()
            
            ratio = float(w)/float(h)
            
            if fmt:
                return '%0.4f' % ratio

            return ratio
        
        return 1


    def getImageFit(self, i):

        ratio = self.getAspectRatio(i)
        
        fit = 'vertical'

        if ratio > 1 and ratio <= 3.0/2:
            fit = 'horizontal'

        return 'fit-%s' % fit
