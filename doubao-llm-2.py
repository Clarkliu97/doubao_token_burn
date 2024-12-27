'''
Usage:
Ark v3 sdk
pip install volcengine-python-sdk
pip install requests
'''

from __future__ import print_function
from volcenginesdkarkruntime import Ark
from pprint import pprint
import time
import random
import os
import datetime


ENDPOINT = 'ep-20240703070454-jknm5'
APIKEY = 'db2291c9-f7de-4894-8b58-b3598ed6bc26'
client = Ark(base_url="https://ark.cn-beijing.volces.com/api/v3", api_key=APIKEY)
    
num = 500000

def startProcess(logFile, pid):
    print(f'start processing with num : {num}')
    time_start = time.time()
    
    sysPrompt1 = """
# 角色
 - 你是一个信息提取专家，善于从用户提供的文档中提取出所需的信息

# 任务
 - 从用户提供的企业主页中提取出企业的名称，并以JSON形式输出
 - 如果某个字段有多个值则输出多个
 - 期望的格式如下
{
"企业名称":"{{/*企业名称*/}}"
}

# 注意
 - 对于未找到相关信息的字段，输出“未知”
 - 对输出的内容要做基本的判断，如果信息明显不合理则输出“未知”，例如“某人”、”联系人“ 很明显不是合理的姓名
"""
    sysPrompt2 = """
# 角色
 - 你是一个信息提取专家，善于从用户提供的文档中提取出所需的信息

# 任务
 - 从用户提供的企业主页中提取出企业的名称、企业联系人或者负责人的姓名，并以JSON形式输出
 - 如果某个字段有多个值则输出多个
 - 期望的格式如下
{
"企业名称":"{{/*企业名称*/}}",
"联系人":"{{/*企业联系人或者负责人的姓名*/}}"
}

# 注意
 - 对于未找到相关信息的字段，输出“未知”
 - 对输出的内容要做基本的判断，如果信息明显不合理则输出“未知”，例如“某人”、”联系人“ 很明显不是合理的姓名
"""

    sysPrompt3 = """
# 角色
 - 你是一个信息提取专家，善于从用户提供的文档中提取出所需的信息

# 任务
 - 从用户提供的企业主页中提取出企业的名称、企业联系人或者负责人的姓名、电话，并以JSON形式输出
 - 如果某个字段有多个值则输出多个
 - 期望的格式如下
{
"企业名称":"{{/*企业名称*/}}",
"联系人":"{{/*企业联系人或者负责人的姓名*/}}",
"电话":"{{/*联系人或负责人的电话*/}}"
}

# 注意
 - 对于未找到相关信息的字段，输出“未知”
 - 对输出的内容要做基本的判断，如果信息明显不合理则输出“未知”，例如“某人”、”联系人“ 很明显不是合理的姓名
"""

    sysPrompt4 = """
# 角色
 - 你是一个信息提取专家，善于从用户提供的文档中提取出所需的信息

# 任务
 - 从用户提供的企业主页中提取出企业的名称、企业联系人或者负责人的姓名、电话和邮箱，并以JSON形式输出
 - 如果某个字段有多个值则输出多个
 - 期望的格式如下
{
"企业名称":"{{/*企业名称*/}}",
"联系人":"{{/*企业联系人或者负责人的姓名*/}}",
"电话":"{{/*联系人或负责人的电话*/}}",
"邮箱":"{{/*联系人或负责人的邮箱*/}}",
}

# 注意
 - 对于未找到相关信息的字段，输出“未知”
 - 对输出的内容要做基本的判断，如果信息明显不合理则输出“未知”，例如“某人”、”联系人“ 很明显不是合理的姓名
"""
    
    sysPrompts = [sysPrompt1, sysPrompt2, sysPrompt3, sysPrompt4]

    for i in range(1, num+1):
        try:
            sysPrompt = sysPrompts[random.randint(0, len(sysPrompts) - 1)]
            text = '生产流程不及格，导致产品出现质量问题。生产流程不及格，导致产品出现质量问题。' #
            randomTimes = random.randint(1, 1000)
            text1 = text * randomTimes
            webContent = page.replace('TTTTTTTTTT', text1)
            companyInfo = standardRequest(sysPrompt, webContent)
            time.sleep(2)
        except Exception as e:
            with open(logFile, 'a') as f:
                f.write(f'try {i} failed with error: {e}\n')
            continue
        if i % 100 == 0:
            with open(logFile, 'a') as f:
                f.write(f'{i}/{num} is processed \n')
        if i % 10 == 0:
                print(f'{i}/{num} is processed in pid {pid}')

    time_end = time.time()
    print(f'开始时间：{time_start}', end="\n")
    print(f'结束时间：{time_end}', end="\n")
    print(f'总耗时：{round((time_end - time_start), 2)}')

        
def standardRequest(sysPrompt:str, userPrompt:str):
    completion = client.chat.completions.create(
        model=ENDPOINT,
        messages=[
            {
                "role": "user",
                "content": sysPrompt,
            },
            {
                "role" : "assistant",
                "content" : userPrompt
            }
        ],
    )
    return completion.choices[0].message.content.strip()

        

page = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "//www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="//www.w3.org/1999/xhtml">
<head>
    

    
    <script type="application/ld+json">
        {
            "@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
            "@id": "http://www.likuso.com/city201/1026810.html",
            "title": "江苏一环集团环保工程有限公司",
            "images": [],
            "description": "江苏一环集团环保工程有限公司，于2002-12-20在江苏省注册成立。在法人杭浩宗经营下，目前公司处于在业，属于建筑业，主营行业为建筑业，我公司以其他的模式经营，加工方式为其他，服务领域为噪声治理; 专业制作声屏障;隔音、吸声材料;;;环保，员工人数100，注册资本2500万元人民币。江苏一环集团环保工程有限公司办公地址为宜兴环科园绿园路518号，如果您对我们的产品、技术或服务有兴趣，随时欢迎您的来电或上门咨询。TTTTTTTTTT",
            "pubDate": "2023-04-12T13:20:25",
            "upDate": "2024-12-05T08:30:07",
        }
    </script>
</head>

<body>

    

        </div>
    </header>
    <div class="w pcBreadNav clearfix">
        <a href="/" title="利酷搜">利酷搜</a>
        <span class="fl">&gt;</span>
        <a href="/city12/" title="江苏省">江苏省</a>

                <span class="fl">&gt;</span>
        <a href="/city201/" title="无锡市">无锡市</a>
                <span class="fl">&gt;</span>
        <a href="/city201/1026810.html" title="江苏一环集团环保工程有限公司">江苏一环集团环保工程有限公司</a>
    </div>

    <!-- 广告位2 -->
    <div id="dom2" style="width: 968px;margin: 0 auto 10px;">
    
    </div>
    <div class="w mt12 clearfix">
        <!--右侧-->
        <!--中间-->
        <div class="promain">
            <div class="profile">
                <div class="h1">
                    <h1>
                        江苏一环集团环保工程有限公司                        <a class="imga" href="#phonenum" title="企业电话">
                            <img src="//statics.likuso.com/statics/images/dh.png" alt="">
                        </a>
                        <a class="imga" href="#card" title="企业认证">
                            <img src="//statics.likuso.com/statics/images/v.png" alt="">
                        </a>
                        
                    </h1>
                    <span>--------&nbsp;&nbsp;无锡市企业简介</span>
                    
                </div>
                <!-- 广告位3 -->
                <div id="dom3">
    
                </div>
                <div class="litinfo">
                    <span class="dates">最近更新时间：<time>2024-12-05 08:30:07</time></span>
                </div>
                <div class="profile_con">
                    <div class="leftad"></div>
                                        <div class="profile_txt">
                        江苏一环集团环保工程有限公司，于2002-12-20在江苏省注册成立。在法人杭浩宗经营下，目前公司处于在业，属于建筑业，主营行业为建筑业，我公司以其他的模式经营，加工方式为其他，服务领域为噪声治理; 专业制作声屏障;隔音、吸声材料;;;环保，员工人数100，注册资本2500万元人民币。江苏一环集团环保工程有限公司办公地址为宜兴环科园绿园路518号，如果您对我们的产品、技术或服务有兴趣，随时欢迎您的来电或上门咨询。                    </div>
                                    </div>
            </div>

            <div class="shenqingcaozuo" style="color:#1E90FF;cursor: pointer">

                <!--<span><a href="/tousu/" target="_blank">申请更新</a></span>-->

                <span class="Span-on span-3" data-type="1">
                    在线采购产品
                </span>
                <span class="Span-on span-3" data-type="2">
                    让卖家联系我
                </span>
            </div>
            <!--工商信息-结束-->
            

            <!--地图-->
            <div id="map" class="company-info-block infoGroup scrolldiv" data-desc="地图">
                <h3 class="block-tit head">
                    <span class="cum-icon icon-location"></span>
                    江苏一环集团环保工程有限公司地址                 </h3>
                <div class="boxcontent">
                    江苏一环集团环保工程有限公司的最新地址是：宜兴环科园绿园路518号                </div>
                            </div>
                        <div class="mt12 clearfix infoGroup">
                <div class="wonderful">
                    <h2 class="head"><span class="cum-icon icon-info"></span> 小提示</h2>
                    <ul class="qysite">
                        <div class="box">
                            <div class="boxcontent" id="cotips">
                                本页是江苏一环集团环保工程有限公司在利酷搜网站的黄页介绍页，
                                <b>一切信息均为无锡市企业主动开放在互联网，或经工商网站可查。</b>

                                <br>如果您是这家无锡市企业的负责人或相关员工，若发现该无锡市企业信息有误，请点击【
                                <a rel="nofollow" href="//www.likuso.com/index.php?m=content&c=index&a=tousu" style="color:#E10000" target="_blank">信息纠错</a>
                                】
                                <br>如果您喜欢该无锡市企业，请您分享该企无锡市企业网址给您的朋友吧！

                            </div>
                        </div>
                    </ul>
                </div>
            </div>
                                </div>

        <!--左侧-->
        <div class="goldmain">
            <div class="_qitjir3gtm"></div>
            <script type="text/javascript">
                if ($BP.onInit()) {
                    (window.slotbydup = window.slotbydup || []).push({
                        id: "u6862319",
                        container: "_qitjir3gtm",
                        async: true
                    });
                }
            </script>
                
                    
        <div class="w footer">
            <div class="w50 mt12 clearfix statement">
                <div class="mzsm">
                    <div class="zsm-title"><i></i>免责声明：</div>
                    <div class="mzsm-con fr">
                        以上所展示的江苏一环集团环保工程有限公司信息由用户自行提供或网络收集，利酷搜不担保江苏一环集团环保工程有限公司信息的真实性、准确性和合法性。
                        利酷搜不涉及用户间因非本网站担保交易方式的交易而产生的法律关系及法律纠纷，纠纷由您自行协商解决。
                    </div>
                </div>
            </div>
            <div class="w50 footer">
                <div class="foot">
                    昆山龙博信息科技有限公司 联系邮箱： likusovip@163.com 电话 
                    <span id="phoneSpan"></span>
                    <span style="font-size:10px;color:gray">© 版权所有</span>
                    <span style="font-size:10px;color:gray">沪ICP备14042209号</span>&nbsp;&nbsp;2015-2022
                    <a href="//beian.miit.gov.cn/" rel="nofollow" target="_blank">苏ICP备17029377号-4</a> |

                    <a href="//www.likuso.com/tousu/" style="color:red" rel="nofollow" target="_blank">
                        纠错/删除
                    </a>&nbsp;&nbsp;
                    <a href="/" target="_blank" title="利酷搜黄页网">利酷搜黄页网</a>
                    <a href="//esphp.likuso.com/index/company/yinsi/" target="_blank">隐私政策</a>
                    <a href="//esphp.likuso.com/index/company/mianze/" target="_blank">免责声明</a>
                    <a href="//esphp.likuso.com/index/company/user_agree/" target="_blank">用户协议</a>
                    <a href="/sitemap.xml" target="_blank">最近更新</a>
                </div>
            </div>
        </div>
        <div style="display: none;" id="idmsg" data-cityid="201" data-comid="1026810"></div>
    </div>
    <div class="year_wrap">
        <div class="year_box">
            <div class="year_box_con"></div>
        </div>
    </div>
    <div class="ul_div" id="ul_div">
        <div class="get_custom">
            <img src="//static.likuso.com/statics/index/images/custom.gif" alt="" class="custom_img">
            <a class="custom_item cus_ot_one " data-type='5'>
                <div class="cus_icon"></div>
                <span class='cc'>在线联系</span>
            </a>
            <a class="custom_item cus_ot_two" href="#dh_phone">
                <div class="cus_icon"></div>
                <span class='cc'>联系方式</span>
            </a>
            <a class="custom_item cus_ot_thr" href="#card">
                <div class="cus_icon"></div>
                <span class='cc'>企业名片</span>
            </a>
        </div>
            </div>
</body>
</html>
"""

if __name__ == "__main__":
    # get pid
    pid = os.getpid()

    # create log file named by pid
    logFile = f'log-{pid}.txt'
    print(f'log file is {logFile}')
    with open(logFile, 'w') as f:
        f.write(f'{datetime.datetime.now()} start processing\n')

    startProcess(logFile, pid)
    
            