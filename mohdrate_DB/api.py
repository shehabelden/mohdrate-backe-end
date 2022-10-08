from rest_framework.generics import GenericAPIView, RetrieveAPIView,ListAPIView
from mohdrate_DB.serilizer import *
class seesion_api(RetrieveAPIView,GenericAPIView):
    queryset = session_db.objects.all()
    serializer_class = one_session_ser
    lookup_field = "session_name"
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
class scientific_material_api(ListAPIView,GenericAPIView):
    queryset = scientific_material_db.objects.all()
    serializer_class = scientific_material_ser
    def get(self,request,*args,**kwargs):
      return  self.list(request, *args, **kwargs)
class one_scientific_material_api(RetrieveAPIView,GenericAPIView):
    queryset = scientific_material_db.objects.all()
    serializer_class = one_scientific_material_ser
    lookup_field = "scientific_material_name"
    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)
class one_akhtbar_material_api(RetrieveAPIView,GenericAPIView):
    queryset = session_db.objects.all()
    serializer_class = one_akhtbar_material_ser
    lookup_field = "session_name"
    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)