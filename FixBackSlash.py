def ReplaceBackslash(Pathname):
    ''' (str) -> str

    Reads a file name and path with '\' slashes and returns the same name
    with '/' slashes. Make sure to begin string input with 'r' so it is read as
    a raw string which prevents python from converting certain backslash 
    characters

    >>> 'C:\Osers\Tim'
    'C:/Osers/Tim'
    '''

    Pathname = 'r' + Pathname
    
    return Pathname.replace("\\","/")
