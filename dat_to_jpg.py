import matplotlib.pyplot as plt
import os
from tkinter import filedialog, messagebox


def convert_data_to_jpeg(file_adr: str, file_name: str, jpeg_dir: str):
    data_x = []
    data_y = []
    with open(file_adr) as f:
        for line in f:
            tmp = [float(x) for x in line.split()]
            data_x.append(tmp[0])
            data_y.append(tmp[1])

    plt.plot(data_x, data_y)
    file_nm = file_name.split(sep='.')[0]
    plt.savefig(os.path.join(jpeg_dir, file_nm + '.jpg'))
    data_x.clear()
    data_y.clear()
    plt.close()


if __name__ == "__main__":
    dat_dir = filedialog.askdirectory(title='Папка с файлами .dat')
    if dat_dir:
        print(dat_dir)

    jpeg_dir = filedialog.askdirectory(title='Папка c указанием куда сохранять')
    if jpeg_dir:
        print(jpeg_dir)

    filelist = {'file': [], 'root': str()}
    for root, dirs, files in os.walk(dat_dir):
        filelist['root'] = root
        for file in files:
            if(file.split(sep='.')[1] == 'dat'):
                filelist['file'].append(file)
        break

    for file in filelist['file']:
        convert_data_to_jpeg(os.path.join(filelist['root'], file), file, jpeg_dir)

    messagebox.askokcancel('Finished', 'Converting finished')
