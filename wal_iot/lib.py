import atexit
import os

class WriteAheadLog:
    """
    WriteAheadLog class is responsible for managing the write-ahead log file.

    The layout of a log record is as follows:
    | +Index (4 bytes) | Length (4 bytes) | Data (Length bytes) |
    
    Where
    - Index: A 4-byte signed integer that is used to identify the record. 
    - Length: A 4-byte unsigned integer that is used to indicate the length of the data.
    - Data: The actual data that is written to the log.

    A special record with only negative value of index is used to indicate the corresponding record has been committed.
    | -Index (4 bytes) |
    """

    def __init__(self, log_file: str):
        """
        Initialize the WriteAheadLog object.

        :param log_file: The path to the log file.
        """
        self.log_file = log_file
        self._fd = open(log_file, 'w+b')
        atexit.register(self._fd.close)
        self._uncommitted_records = {}

        
    def compress(self):
        """
        Compress the log file by removing the committed records.
        """
        self._fd.seek(0)
        while True:
            b_i = self._fd.read(4)
            if not b_i :
                break
            i = int.from_bytes(b_i, signed=True)
            if i > 0:
                b_len = self._fd.read(4)
                l = int.from_bytes(b_len)
                b_data = self._fd.read(l)




                
            
            
                
                

            
