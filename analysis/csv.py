from os import path, name

def launch_analysis(data_file):
    directory = path.dirname(path.dirname(__file__))
    path_to_file = path.join(directory,"data",data_file)

    try:
        with open(path_to_file,"r") as f:
            preview = f.readline()
            print("Here is the preview: {} ".format(preview))
    except FileNotFoundError as e:
        print("ow! file not found")
    except:
        print("destination unknown")


if __name__ == "__main__":
    launch_analysis('current_mps.csv')

