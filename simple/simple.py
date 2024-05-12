from models.nb.nb import run



folder_path = "all_data"

acc, prec, rec = run(folder_path)


print(acc, prec, rec)