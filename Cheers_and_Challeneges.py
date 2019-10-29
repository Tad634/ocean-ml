from datetime import date
from datetime import timedelta
from itertools import cycle
no_session = { date(2019,11,5), date(2019,11,7), date(2019,11,28), date(2019,12,26),
              date(2020,1,2), date(2020,1,9), date(2020,1,30), date(2020,2,27),
              date(2020,2,20), date(2020,4,2), date(2020,4,9), date(2020,4,16),
              date(2020,6,4)
             }
start = date(2019, 10, 22)
end = date(2020, 6, 6)
names= ['Kai','Lynette','Isabel','Shanique','Tadelin','Gladys']
name_cycle =cycle(names)
week=timedelta(days = 7)

i=date.today()
while i <= end:
	if i not in no_session:
		print(i,next(name_cycle))
		i+=week

