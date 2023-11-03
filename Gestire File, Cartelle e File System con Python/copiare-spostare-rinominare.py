import shutil
shutil.copy("percorso file da copiare","percorso file di destinazione")  #copiare file 

shutil.move("percorso file da spostare","percorso file di destinazione")  #spostare file

import os
os.unlink("percorso file da cancellare")  #cancellare file

os.rename("percorso file da rinominare","perscorso + novo nome")  #rinominare file