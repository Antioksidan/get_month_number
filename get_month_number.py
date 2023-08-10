def get_month_number(year, week_number):
    date_obj = datetime.strptime(f'{year}-W{week_number}-1', '%Y-W%W-%w')
    month_number = date_obj.month
    return month_number