from wal_iot import WriteAheadLog
from unittest import TestCase
import tempfile



class TestWriteAheadLog(TestCase):

    def test_sanity(self):
        test_items = [
            1,
            1.0,
            'hello world',
            {'a': 1, 'b': 2},
            [1, 2, 3, 'data'],
            (1, 2, 3, 'data'),
            set(),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = temp_dir + '/wal.log'
            wal = WriteAheadLog(log_file)
            wal.init()

            ids = []
            for item in test_items:
                i = wal.stage(item)
                ids.append(i)
            wal.close()

            wal = WriteAheadLog(log_file)
            wal.init()
            for i, (_, item) in enumerate(wal.iter_records()):
                self.assertEqual(item, test_items[i])
            
            for i in ids:
                wal.commit(i)
            wal.close()

            wal = WriteAheadLog(log_file)
            wal.init()
            self.assertEqual(len(list(wal.iter_records())), 0)