#!/usr/bin/env python
#-*-coding: utf-8 -*-

def ninty_nine_songs():
    """Print 99 bottles of beer song.

    This program prints the popular long trip folk song of United States and Canada
    about 99 beers. The song was originated from around mid-20th century.

    More information:
    https://en.wikipedia.org/wiki/99_Bottles_of_Beer#References_in_computer_science

    """
    # first 98 lines
    for i in range(99,1,-1):
	    print('{0} bottles of beer on the wall, {0} bottles of beer.'.format(i))
	    print('Take one down, pass it around, {0} bottles of beer on the wall...\n'.format(i-1))

    # second last line
    print('1 more bottles of beer on the wall, 1 more bottles of beer.')
    print('Take one down, pass it around, no more bottles of beer on the wall...\n')

    # last line
    print('No more bottles of beer on the wall, no more bottles of beer.')
    print('We\'ve taken them down and passed them around; now we\'re drunk and passed out!')

if __name__ == '__main__':
	ninty_nine_songs()
