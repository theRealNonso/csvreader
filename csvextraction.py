import os, shutil
import glob 
import pandas
import redis 
import csv


class ReadCsv:
    cdir = ''
    outdir = ''
    redis_host = "localhost"
    redis_port = 6379
    redis_password = ""

    def save_to_redis(self, dir):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            with open(dir, 'rt') as f:
                reader = csv.reader(f)
                for row in reader:
                    r.lpush("key", bytes(row))
                    result = r.lrange("key", 0, 10)
                    print(result)
        except Exception as e:
            print(e)

    def move_file(self,source_file, dest_folder):
        shutil.move(source_file, dest_folder)
        return


    def concat_files(self, cdir, outfile):
        self.cdir = cdir
        self.outfile = outfile
        os.chdir(self.cdir)
        file_list = glob.glob("*.csv")
        dfList = []

        for filename in file_list:
            df = pandas.read_csv(filename, header=None, chunksize=5)
            for chunk in df:
                dfList.append(chunk)
        concatdf = pandas.concat(dfList, axis=0)
        concatdf.to_csv(outfile, index=None)
        self.save_to_redis(outfile)
        self.move_file(outfile, '/home/nonso/Desktop/finalcsv.csv')


