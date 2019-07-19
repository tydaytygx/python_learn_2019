import os

class TABFILE:
    def __init__(self, filename, dest_file = None):
        self.filename = filename
        if not dest_file:
            self.dest_file = filename
        else:
            self.dest_file = dest_file
        self.filehandle = None
        self.content = []
        self.initflag = False
        self.column = 0
        self.row = 0
        self.data = []
    def Init(self):
        try: 
            self.filehandle = open(self.filename, 'r')
            self.initflag = self._load_file()
        except: 
            pass
        else:
            self.initflag = True
        return self.initflag

    def UnInit(self):
        if self.initflag:
            self.filehandle.close()
        
    def _load_file(self):
        if self.filehandle:
            self.content = self.filehandle.readlines()
            self.row = len(self.content) - 1
            head = self.content[0].split('\t')
            self.column = len(head)
            for line in self.content:
                #这里需要去掉末尾的换行
                #line = line - '\n\r'
                self.data.append(line.rstrip().split('\t'))
            return True
        else:
            return False

    def GetValue(self, row, column):
        if 0 < row < self.row and 0 < column < self.column:
            return self.data[row][column - 1]
        else:
            return None

    def SetValue(self, row, column, value):
        if 0 < row < self.row and 0 < column < self.column:
            self.data[row][column] = value
        else:
            return False

    def SaveToFile(self):
        filewrite = open(self.dest_file, 'w')
        if not filewrite:
            return False
        sep_char = '\t'
        for line in self.data:
            filewrite.write(sep_char.join(line)+'\n')
        filewrite.close()
        return True
