class Model:
    def __init__(self,seriouslv,findsub,NCRclass,findtime,findperson,questionnum,dealopinion,solution,confirmperson,verifytime,stated):
        self.no=''   #序号
        self.filename=''  #文件名
        self.funname=''  #函数名
        self.seriouslv=seriouslv #严重程度
        self.findsub=findsub #发现方式
        self.NCRclass=NCRclass #NCR分类
        self.findtime=findtime #发现时间
        self.findperson=findperson #发现人
        self.questiondescribe='' #详细问题描述
        self.questionnum=questionnum #问题个数
        self.dealopinion=dealopinion #处理意见
        self.solution=solution #解决措施
        self.confirmperson=confirmperson #研发确认
        self.verifytime=verifytime  #验证时间
        self.stated=stated #状态
