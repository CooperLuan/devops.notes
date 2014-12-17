'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class RefundRefuseRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.refund_id = None
		self.refund_phase = None
		self.refund_version = None
		self.refuse_message = None
		self.refuse_proof = None

	def getapiname(self):
		return 'taobao.refund.refuse'

	def getMultipartParas(self):
		return ['refuse_proof']
