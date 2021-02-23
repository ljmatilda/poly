
import datetime 

class FlowTimeList():

	def getTimeList(self, date_pair):

		result = []

		for item in date_pair:
			date1 = datetime.datetime.strptime(item[0], '%Y.%m.%d')
			date2 = datetime.datetime.strptime(item[1], '%Y.%m.%d')
			day = date2.date() - date1.date()

			result.append(day.days)

		return result
		