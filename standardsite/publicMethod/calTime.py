
from datetime import date, timedelta
from standardtime.models import Holiday

# Create your method here.
class CalTime():
			
	def calEndDay(self, begintime, period):
		period_now = period
		end_date = begintime + timedelta(days = period_now)
		holidays = Holiday.objects.all()
		for holiday in holidays:
			holiday_begin_date = holiday.begin_date
			if begintime <= holiday_begin_date and end_date >= holiday_begin_date:
				end_date = end_date + timedelta(holiday.days)				

		#判断是否周末
		weekno = end_date.weekday()
		if weekno == 5:
			end_date = end_date + timedelta(2)
		elif weekno == 6:
			end_date = end_date + timedelta(1)

		return end_date

	def getEndDay(self, begintime, period):
		period_now = period
		end_date = begintime + timedelta(days = period_now)
		holidays = Holiday.objects.all()
		for holiday in holidays:
			holiday_begin_date = holiday.begin_date
			if begintime <= holiday_begin_date and end_date >= holiday_begin_date:
				end_date = end_date + timedelta(holiday.days)				

		#判断是否周末
		weekno = end_date.weekday()
		if weekno == 5:
			end_date = end_date + timedelta(2)
		elif weekno == 6:
			end_date = end_date + timedelta(1)

		return end_date.strftime("%Y.%m.%d")



