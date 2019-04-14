def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def is_num_type(num):
	if type(num) is type(int()) or type(num) is type(float()):
		return True
	return False

def listAvg(list_):
	if type(list_) is type([]):
		sum_=0

		for num in list_:
			if type(num) is type(0) or type(num) is type(0.1):
				sum_ += num

		return sum_ / len(list_)
	return 0

def reciprocal(num):
	if is_num_type(num):
		try:
			return 1/num
		except Exception:
			return 0
	return None