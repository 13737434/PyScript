import datetime
class CyclomaticItem:
    def __init__(self):
        self.no=''   #序号
        self.file_name=''  #文件名
        self.fun_name=''  #函数名
        self.serious_lv='一般' #严重程度
        self.find_sub='质量度量' #发现方式
        self.NCR_class='编码缺陷' #NCR分类
        self.find_time=datetime.datetime.now().strftime('%Y%m%d') #发现时间
        self.find_person='柴荣阳' #发现人
        self.question_describe='' #详细问题描述
        self.question_num='1' #问题个数
        self.deal_opinion='说明' #处理意见
        self.solution='代码经多轮测试验证，逻辑正确，符合设计' #解决措施
        self.confirm_person='王海南'#研发确认
        self.verify_time=datetime.datetime.now().strftime('%Y%m%d')  #验证时间
        self.state='closed'#状态


