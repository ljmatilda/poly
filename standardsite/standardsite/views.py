from django.http import HttpResponse,StreamingHttpResponse
from django.conf import settings
import os
  
def download(request, filename1):
 # print("filename1: ", filename1)
 # filename = request.GET.get('file')
 filepath = os.path.join('media/', filename1)
 # print("filepath: ", filepath)
 fp = open(filepath, 'rb')
 response = StreamingHttpResponse(fp)
 # response = FileResponse(fp)
 response['Content-Type'] = 'application/octet-stream'
 response['Content-Disposition'] = 'attachment;filename="%s"' % filename1
 return response
 fp.close()