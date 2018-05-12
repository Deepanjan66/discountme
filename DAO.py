from abc import ABC, abstractmethod
import csv
from csv import DictReader, DictWriter
import os
from config import *

TABLE_STRUCTURE = {
        USERS : ['id', 'name', 'location', 'password','email'],
        POSTS : ['id', 'name', 'original_price', 'current_price', 'location', 'category', 'unit', 'expiration'],
        USER_POST : ['uid', 'post_id']
}


class DAO():
    def __init__():
        pass

    @abstractmethod
    def read(table):
        pass

    '''
    Payload is gonna be a list of dictionary
    with csv title as key
    '''
    @abstractmethod
    def write(table, payload):
        pass


class csvDAO(DAO):
    def __init__(self, root_path):
        self.root_path = root_path

    def read(self, table):
        with open(os.path.join(self.root_path, table), 'r') as csv_in:
            return  [ dict(entry) for entry in DictReader(csv_in) ]


    def write(self, table, payload, mode='a'):
        with open(os.path.join(self.root_path, table), mode) as csv_out:
            """
            writer = csv.writer(csv_out)
            for row in payload:
                writer.writerow(row)
            """
            print(TABLE_STRUCTURE[table])
            writer = DictWriter(csv_out, TABLE_STRUCTURE[table])
            if csv_out.tell() == 0:
                writer.writeheader()
            writer.writerows(payload)
        '''
        # THIS IS A NAIVE VERSION
        # TODO: do replacing/updating when try to write duplicated entry

        # read out old stuff
        assert(table in TABLE_STRUCTURE.keys())
        old_vals = list(DictReader(self.files[table]))
        
        for entry in payload:
            old_vals.append(entry)

        # rewrite whole file
        self.files[table].truncate()
        self.files[table].seek(0)
        with DictWriter(self.files[table], TABLE_STRUCTURE[table]) as writer:
            writer.writeheader()
            writer.writerows(payload)
        '''
