import datetime
class TheSameItem:
    def __init__(self):
        self.no=''   #序号
        self.file_name=''  #文件名
        self.test_skill='编码规则检查'  #测试技术
        self.disqualification=''  #不合格项
        self.disqualification_num=''  #不合格项个数
        self.disqualification_lv='建议'  #不合格项等级
        self.verify_time=datetime.datetime.now().strftime('%Y%m%d')  #验证时间
        self.deal_way='说明'#处理方式
        self.explanation='经分析，实现逻辑正确，符合设计'#研发说明
        self.confirm_person='王海南'#研发确认
        self.test_person='柴荣阳'#测试者
        self.state='closed'#状态