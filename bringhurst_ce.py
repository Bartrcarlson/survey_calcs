import classy_program as survey
from classy_program import Angle


runs = [
    Angle(['N',[56,8,0],'E']),
    Angle(['S',[33,52,0],'E']),
    Angle(['S',[56,8,0],'W']),
    Angle(['S',[33,52,0],'E']),
    Angle(['N',[55,0,0],'E']),
    Angle(['S',[33,52,0],'E']),
    Angle(['N',[0,54,20],'E']),
    Angle(['N',[85,85,0],'W']),
    Angle(['N',[40,14,15],'W']),
    Angle(['N',[90,0,0],'W']),
    Angle(['S',[0,0,0],'E']),
    Angle(['N',[90,0,0],'E']),
    Angle(['S',[33,52,0],'E']),
    ]


for i in runs:
    print(i.ang)

