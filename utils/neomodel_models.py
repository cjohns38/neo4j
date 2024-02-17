import neomodel
from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, FloatProperty

from neomodel.contrib.spatial_properties import PointProperty

class Geo(StructuredNode):
    location = PointProperty(crs='wgs-84')

class GeoRelationship(neomodel.StructuredRel):
    on_date = neomodel.DateProperty(default_now = True)

class Person(StructuredNode):
    uuid = StringProperty()
    fname = StringProperty()
    lname = StringProperty()
    username = StringProperty()
    is_vip = BooleanProperty()
    dob = DateProperty()
    ssn = StringProperty()
    phone = StringProperty()

    address = StringProperty()
    post_code = StringProperty()
    crs = FloatProperty()

    geo_data = neomodel.RelationshipTo("Geo", "LOCATED_AT", model=GeoRelationship)