import io

# What is IO
# byte IO (AKA file object, stream object, file-like object.)
    # Files on disk are a series of 1 and 0.
    # For simplicity, we'll think of them as a series of bytes.
    # We'll also consider stdin and stout to be a special type of file.
    # textual data and byte data are not the same.
        # a binary io procedure takes in binary data (bytes/bytearray)
            # binary data is written directly into disk
        # this data is written to the file unmodified
        # the bytes in your program are represented identically on disk
        '''https://www.youtube.com/watch?v=cIaOisyd7lE'''
        
#methods (acces or serve)
        # read-only
        # write-only
        # read-write
        # arbitrary random access (seeking forwards or backwards to any location)
        # only sequential access (like a socket or pipe)
        '''https://docs.python.org/3/library/io.html#io.StringIO'''
        
# Text I/O
    # The generic function for this library is open()
    # if a file descriptor is given, it is closed when the  returned IO object is closed
    # unless closedfd is set to False.
        # mode
        # file
        # encoding in text mode, if encoding is not specified the encoding used is platform-dependent
            # locale.getpreferredcoding(False)
        # For reading and writing raw bytes use binary mode and leave encoding unspecified.
        #
# byte type data specified by b''
yy = b'deltoi'
yy.__class__

    # Converting to hex
yy.hex()
    # Changing to capital letters:
yy.swapcase()

# I/O common operator "open()"
    '''https://docs.python.org/3/tutorial/inputoutput.html#tut-files'''

open(, mode="r", encoding="UTF-18")

open( , mode="w")

# Writing some binary data:
open( , 'b', )

# textual IO (AKA file object, stream object, file-like object.)
    # in python 2 is UNICODE.
    # in python 3 is str
    # this data is first encoded into a series of bytes. Those bytes are then written into the memory.
    # The text in your program is represented by encoded bytes on disk.
        '''https://www.youtube.com/watch?v=cIaOisyd7lE'''


output = io.StringIO()
output.write('Frist Line.\n')
print('Second line.', file=output)

# Retrieve file content -- this will be
# 'First line. \nSecond line.
    '''https://docs.python.org/3/library/io.html#io.StringIO'''
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
    '''https://docs.python.org/3/library/io.html#io.StringIO'''
output.close()


        

