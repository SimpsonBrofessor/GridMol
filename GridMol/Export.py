import os

#----------------------------------------#
#----- EXPORT                       -----#
#----- save MOL text file           -----#
#----------------------------------------#
def Export(mol_file, export_directory):
    if not os.path.isdir(export_directory):
            os.makedirs(export_directory)
    
    export_filepath = os.path.join(export_directory, 'output.mol')

    try:
        with open(export_filepath, 'w') as output_file:
            output_file.write(mol_file)

    except:
        print(f'EXPORT ERROR: OUTPUT MOL FILE {export_directory}') 