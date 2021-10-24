from presidents import *
import pytest

# testing to see if the function can be called
def test_canCall_Presidents():
    validPrez("shmeka")

@pytest.mark.parametrize("prez", ["Donald Trump" , "Barack Obama" , "George W. Bush" , "Bill Clinton" , "Bush" ,
                                  "Ronald Reagan" , "Jimmy Carter" , "Gerald Ford" , "Richard Nixon" , "Lyndon B. Johnson" ,
                                  "John F. Kennedy" , "Dwight D. Eisenhower", "Harry S. Truman" , "Franklin D. Roosevelt" ,
                                  "Herbert Hoover" , "Calvin Coolidge" , "Warren G. Harding" , "Woodrow Wilson" , "Howard Taft" ,
                                  "Theodore Roosevelt" , "William McKinley" , "Grover Cleveland" , "Benjamin Harrison" ,
                                  "Grover Cleveland" , "Chester A. Arthur" , "Garfield" , "Rutherford B. Hayes" ,
                                  "Ulysses S. Grant" , "Andrew Johnson" , "Abraham Lincoln" , "James Buchanan" ,
                                  "Franklin Pierce" , "Millard Fillmore", "Zachary Taylor" , "James K. Polk" ,
                                  "John Tyler" , "William Henry Harrison" , "Martin Van Buren" , "Andrew Jackson" ,
                                  "John Quincy Adams" ,"James Monroe" , "James Madison" , "Thomas Jefferson" , "John Adams" , "George Washington"])
def test_president_in_list(prez):
    president = validPrez(prez)
    assert president == ('yes')

