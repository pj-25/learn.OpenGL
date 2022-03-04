from graphicsAI.base.attribute import Attribute


class Geometry(object):
    def __init__(self):
        self.attributes = {}
        self.vertexCount = None
        
    def addAttribute(self, dataType, varName, data): 
        self.attributes[varName] = Attribute (dataType, data)
        
    def countVertices(self):
        attrib = list( self.attributes.values() )[0]
        self.vertexCount = len( attrib.data )

    # transform the data in an attribute using a matrix 
    def applyMatrix(self, matrix, varName="vertexPos"):
        oldPositionData = self.attributes[varName].data 
        newPositionData = []
        for oldPos in oldPositionData: 
            newPos = oldPos.copy() 
            newPos.append(1) 
            newPos = matrix @ newPos 
            newPos = list( newPos[0:3] ) 
            newPositionData.append( newPos )

        self.attributes[varName].data = newPositionData 
        self.attributes[varName].uploadData()

    # merge data from attributes of other geometry into this object; 
    # requires both geometries to have attributes with same names 
    def merge(self, otherGeometry):
        for varName, attrObject in self. attributes.items(): 
            attrObject.data += otherGeometry.attributes[varName].data 
            attrObject.uploadData()
            
        self.countVertices()