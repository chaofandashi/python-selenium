# -*- coding: utf-8 -*-
# @Author  : leizi
from bussinses.blo import Zaohui_tes
import unittest,time,os,ddt
from util import log
from selenium import webdriver
from util.gettestdata import huoqu_test
path=os.getcwd()
case_path=path+'\\data\\case.xlsx'
casedata=huoqu_test(case_path,2)
@ddt.ddt
class Testzhaohui(unittest.TestCase):
    def setUp(self):
        title=u'找回密码测试'
        self.logs=log.log_message(title)
        self.derve=webdriver.Firefox()
        self.zhaohui_fun=Zaohui_tes(self.derve)
    @ddt.data(*casedata)
    def test_zhaohui_1(self,casedata):
        self.username=casedata['username']
        self.email=casedata['email']
        self.suc=casedata['suc']
        self.assert_vale=casedata['assert_vale']
        self.retu_data=self.zhaohui_fun.zhaohui(self.username,self.email,self.suc)
        self.derve.get_screenshot_as_file(path+'\\testreposepang\\%s.png'%casedata['id'])
        self.logs.info_log('inptut name:%s,email:%s,assert:%s'%(self.username,self.email,self.assert_vale))
        time.sleep(1)
        self.assertEqual(self.retu_data, self.assert_vale)
    def tearDown(self):
        self.derve.quit()