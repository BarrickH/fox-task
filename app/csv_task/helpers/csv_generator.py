import csv
import os
import random
import secrets
import string

from datetime import datetime


class CsvGenerator:

    def __init__(self):
        out = input('run csv task? (y/n)')
        if out != 'y':
            print('csv task skipped')
            # exit(0)
        # declare variables
        self.rows = input('rows:') or 50
        if not isinstance(self.rows, int):
            self.rows = 50
        print(f'csv rows: {self.rows}')
        self.output_path = input('output_path:') or os.getcwd()
        print(f'file output to: {self.output_path}')
        self.column_input = []

    def main(self):
        # handle column input
        self.handle_column_input()

        # generate csv to the given directory
        self.generate_csv()

    def handle_column_input(self):
        col_id = 1
        self.get_current_column_input(col_id)
        # specified column multiple times
        while True:
            c_flag = input(f'column-{col_id}: {self.column_input[col_id-1]}, need more columns? (y/n)')
            if c_flag.lower() != 'y':
                return
            col_id += 1
            self.get_current_column_input(col_id)

    def get_current_column_input(self,col_id):
        column_input = input(f'column-{col_id}:')
        if self.column_input_validate(column_input):
            self.column_input.append(' '.join(column_input.split()[:2]))
        else:
            self.handle_column_input_error(column_input)

    def handle_column_input_error(self,column_input):
        if not self.column_input_validate(column_input):
            current_input = input(f"please enter column with column name and column type respectively, "
                                  f"a space is needed in between. column type can be integer or string.")
            self.handle_column_input_error(current_input)
        else:
            self.column_input.append(' '.join(column_input.split()[:2]))

    def column_input_validate(self,column_input):
        if len(column_input.split()) <2:
            return False
        if column_input.split()[1] not in ['integer', 'string']:
            return False
        return True

    def generate_csv(self):
        payload = [self.generate_one_row() for _ in range(self.rows)]
        # YYYY-MM-DD-HH_MM_SS
        filename = datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
        if self.output_path:
            filename = self.output_path + "/" + filename
        self.save_to_csv(payload,filename)

    def generate_one_row(self):
        column_dict = {}
        # example = ["company string", "name string", "age integer"]
        headers = [col.split()[0] for col in self.column_input]
        duplicate_names = list(set([x for x in headers if headers.count(x) > 1]))
        duples_names_check = []
        for col in self.column_input:
            name = col.split()[0]
            if name in duplicate_names:
                duples_names_check.append(name)
                count = duples_names_check.count(name)
                index = f"-{count}" if count else ''
                name = f"{name}{index}"
            col_type = col.split()[1]
            value = self.random_col_value(col_type)
            column_dict[name] = value
        return column_dict

    @staticmethod
    def random_col_value(type):
        string_col = ''.join(secrets.choice(string.ascii_letters) for _ in range(random.randint(1, 10)))
        integer_col = random.randint(1, 300000)
        return string_col if type == 'string' else integer_col

    @staticmethod
    def save_to_csv(payload,file_name):
        import csv
        keys = payload[0].keys()
        with open(f'{file_name}.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(payload)
