################################################################################
#   This python script will only work on systems containing the grep command. In
#       the future, I may change the code to not rely on grep, but for now, grep
#       suits my purposes for this script.
################################################################################

import sys
import os

def main():
    def main_menu():
        print("*"*30)
        print("  Please choose an option.")
        print("  1) Passage lookup")
        print("  2) Database search")
        print("  0) Quit")
        print("*"*30)
        selection = input("> ")
        
        if selection == "1":
            print("\nPlease enter a passage.")
            passage = input("> ")
            print()
            lookup(passage)
        elif selection == "2":
            print("\nPlease enter a search query.")
            query = input("> ")
            print()
            search_db(query)
        elif selection == "0":
            quit()
        else:
            print("Invalid input.")
    
    def lookup(passage):
        # Split the provided passage at the space character(s). Passages are supplied in the format of
        #   book, chapter, verse (or verse range), each separated by a space. If the verse is not supplied,
        #   the full chapter will be displayed.
        #   Examples: eph 2 8
        #             eph 2 8-10
        #             eph 2
        passage_parts = passage.split()
        if len(passage_parts) == 2: # This assumes a book and chapter were supplied.
            passage_string = passage_parts[0] + ":" + passage_parts[1] + ":"
            os.system("grep --color=auto '" + passage_string + "' rcv.db")
            print()
        elif len(passage_parts) == 3: # This assumes a book, chapter, and verse or verse range were supplied.
            if "-" in passage_parts[2]: # Assume a verse range was supplied.
                # Split the verse range at the hyphen to get the first verse in the range and the last verse
                #   to be displayed.
                verse_range = passage_parts[2].split("-")
                current_verse = int(verse_range[0]) # Assing the first verse to current_verse.
                # Loop through each passage in the supplied verse range beginning with the first verse an up
                #   to and including the last verse.
                while current_verse <= int(verse_range[1]):
                    passage_string = passage_parts[0] + ":" + passage_parts[1] + ":" + str(current_verse) + "|"
                    os.system("grep --color=auto '" + passage_string + "' rcv.db")
                    current_verse += 1 # Increment by one to go to the next verse in the range.
                print()
            else:
                passage_string = passage_parts[0] + ":" + passage_parts[1] + ":" + passage_parts[2] + "|"
                os.system("grep --color=auto '" + passage_string + "' rcv.db")
                print()
        else:
            print("Invalid passage format.\n")
    
    def search_db(query):
        os.system("grep --color=auto '" + query + "' rcv.db")
        print()
    
    def quit():
        print("\n  Quitting...\n")
        sys.exit(0)
    
    while True:
        main_menu()

if __name__ == '__main__':
    main()
