def get_val(collection, key, default='git'):
    """
   хххххх
    """
    for key_,value in collection.items():
        if key_==key:
                return value

    return default