import csv

class handler:
    def opener():
        with open(r"C:\Users\maoya\OneDrive\ドキュメント\3D_BlockPacking\blocks.csv","r") as f:
            data = csv.reader(f)
            output = []
            for row in data:
                output.append(row)
            return output
        
    def intize(cFile):
        for ii in range(len(cFile)):
            for jj in range(len(cFile[0])):
                cFile[ii][jj] = int(cFile[ii][jj])
        return cFile
    
    def initializeCSV(maxsize):
        with open(r"C:\Users\maoya\OneDrive\ドキュメント\3D_BlockPacking\outtest.csv","a",newline="") as f:
            writer = csv.writer(f)
            f.truncate(0)
            keyword = ['ThisIsAKey.']
            writer.writerow(keyword)
            writer.writerow(maxsize)
    
    def writeCSV(matrix):
        with open(r"C:\Users\maoya\OneDrive\ドキュメント\3D_BlockPacking\outtest.csv","a",newline="") as f:
            writer = csv.writer(f)
            for ii in range(len(matrix)):
                writer.writerow(matrix[ii])
