import detailedResultsDao
import resultByIDDao
import time
import csv

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def csvExport():
    dateTimeStamp = time.strftime('%Y%m%d%H%M%S')

    detailedResultsData = detailedResultsDao.DetailedResultsDao.get_table()

    f = open(dateTimeStamp + 'detailed_results_output.csv', 'w', newline="")
    writer = csv.writer(f,delimiter=',')
    writer.writerows(detailedResultsData)
    f.close()

    resultByIDData = resultByIDDao.ResultByIDDao.get_table()

    f = open(dateTimeStamp + 'result_by_id_output.csv', 'w', newline="")
    writer = csv.writer(f,delimiter=',')
    writer.writerows(resultByIDData)
    f.close()