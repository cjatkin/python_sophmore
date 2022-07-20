import redis

#sending a file over redis (from drone to commander)

#Part1 --------------------------------------------------------------------
def copy_logs_to_redis(conn, path, channel, count = 10, limit = 2**30, quit_when_done= True):
	bytes_in_redis = 0
	waiting = deque()	#deque() is a doubly ended queue
				#

	create_chat(conn, 'source', map(str, range(count)), '', channel)

	count = str(count)

	for logfile in sorted(os.listdir(path)):

	full_path = os.path.join(path, logfile)

	fsize = os.stat(full_path).st_size

	while bytes_in_redis + fsize > limit:
		cleaned = _clean(conn, channel, waiting, count)
		if cleaned:
			bytes_in_redis -= cleaned
		else:
			time.sleep(.25)

	with open(full_path, 'rb') as inp:
		block = ' '
		while block:
			block = inp.read(2**17)
			conn.append(channel+logfile, block)

	send_message(conn, channel, 'source', logfile)

	bytes_in_redis += fsize
	waiting.append((logfile, fsize))

#Part2 -------------------------------------------------------------
if quit_when_done:
	send_message(conn, channel, 'source', ':done')

#Part3 --------------------------------------------------------------
while waiting:
	cleaned = _clean(conn, channel, waiting, count)
	if cleaned:
		bytes_in_redis -= cleaned
	else:
		time.sleep(.25)

def _clean(conn, channel, waiting, count):
	if not waiting:
		return 0
	w0 = waiting[0][0]
	if conn.get(channel + w0 + ':done') == count:
		conn.delete(channel + w0, channel + w0 + ':done')
		return waiting.popleft()[1]
	return 0






