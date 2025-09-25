# This code should be inside src/utils.py
import os
import dill

def save_object(file_path, obj):
    """
    This function saves a Python object to a file.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        # You should raise your CustomException here
        raise e