from configparser import ConfigParser
import os


class Config:
    def getPostgres(section='postgresql', filename='./Config/config.ini'):
        parser = ConfigParser(os.environ)
        parser.read(filename)
        # get section, default to postgresql
        all_params = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                all_params[param[0]] = param[1]
            return  {
                'host': all_params['host'],
                'user': all_params['user'],
                'database': all_params['database'],
                'password': all_params['password']
            }
        else:
            raise Exception('Section {} not found in the {} file'.format(section, filename))