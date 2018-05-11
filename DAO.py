from abc import ABC, abstractmethod
from csv import DictReader, DictWriter
import os

TABLE_STRUCTURE = {
        'user': ['id', 'name', 'location', 'password'],
        'post': ['id', 'name', 'original_price', 'current_price', 'location'],
        'post-user': ['post_id', 'uid']
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
        with open(os.path.join(self.root_path, 'table', table + '.csv'), 'r') as csv:
            return  [ dict(entry) for entry in DictReader(csv) ]


    def write(self, table, payload):
        with open(os.path.join(self.root_path, 'table', table + '.csv'), 'a') as csv:
            writer = DictWriter(csv, TABLE_STRUCTURE[table])
            if csv.tell() == 0:
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
