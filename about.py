from libs .animation import colorText #line:1
import os #line:2
import webbrowser #line:3
def about_msg ():#line:4
    print (colorText ('''

[[red]] [ 1 ] [[reset]] [[cyan]] Github - https://github.com/losinguh
[[red]] [ 2 ] [[reset]] [[cyan]] Youtube - https://github.com/losinguh
[[red]] [ 3 ] [[reset]] [[cyan]] Telegram - https://t.me/losinguhhh
[[red]] [ 4 ] [[reset]] [[cyan]] Instagram - https://instagram.com/losinguh
[[red]] [ 5 ] [[reset]] [[cyan]] EXIT 

    '''))#line:13
    OOO000OO00000O00O =input (" Select - ")#line:14
    if (int (OOO000OO00000O00O )==1 ):#line:15
        webbrowser .open ('https://github.com/T3AmSyNc')#line:16
        about_msg ()#line:17
    if (int (OOO000OO00000O00O )==2 ):#line:18
        webbrowser .open ('https://github.com/T3AmSyNc')#line:19
        about_msg ()#line:20
    if (int (OOO000OO00000O00O )==3 ):#line:21
        webbrowser .open ('https://t.me/losinguhhh')#line:22
        about_msg ()#line:23
    if (int (OOO000OO00000O00O )==4 ):#line:24
        webbrowser .open ('https://instagram.com/losinguh')#line:25
        about_msg ()#line:26
    if (int (OOO000OO00000O00O )==5 ):#line:27
        os .system ('python ReportBot.py'if os .name =='nt'else 'bash run.sh')#line:28
