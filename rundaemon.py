import sys, daemon, time
from csvextraction import ReadCsv


class Daemon(daemon.Daemon):
    def run(self):
        obj = ReadCsv()
        while True:
            try:
                obj.concat_files('/home/nonso/Desktop/csvfiles', '/home/nonso/Desktop/files.csv')
            except Exception as e:
                print(e)
                time.sleep(1)

daemon = Daemon()

if 'start' == sys.argv[1]: 
    daemon.start()
elif 'stop' == sys.argv[1]: 
    daemon.stop()
elif 'restart' == sys.argv[1]: 
    daemon.restart()
