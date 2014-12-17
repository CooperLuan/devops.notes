'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class HotelCityGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.country = None

	def getapiname(self):
		return 'taobao.hotel.city.get'
