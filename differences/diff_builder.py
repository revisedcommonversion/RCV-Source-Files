#!/usr/bin/python

####################################################################### License.
#  The Holy Bible: Revised Common Version
#  Copyright (c) 2026 William Masopust
#  http://www.revisedcommonversion.com
#  The source code of the RCV text is available at http://source.rcv.xyz.
#
#  This project and the accompanying materials are made available under the
#  terms of the Eclipse Public License 2.0 which is available at
#  https://www.eclipse.org/legal/epl-2.0/.
#
#  SPDX-License-Identifier: EPL-2.0
################################################################################

# Before running this script, make sure the proper database files are in the
#   same directory as this script.

import os

source_translation = "kjv"
compare_translation = "wbs"

sourcedb = source_translation + ".db"
compdb = compare_translation + ".db"
booksdb = "books.db"

# Load the source database file.
with open(sourcedb) as sourcedb_file:
    sourcedb_list = sourcedb_file.readlines()

# Strip the source database list of new line characters.
for i, line in enumerate(sourcedb_list):
    sourcedb_list[i] = line.strip()

# Load the compared database file.
with open(compdb) as compdb_file:
    compdb_list = compdb_file.readlines()

# Strip the compared database list of new line characters.
for i, line in enumerate(compdb_list):
    compdb_list[i] = line.strip()

# Load the books database file.
with open(booksdb) as booksdb_file:
    booksdb_list = booksdb_file.readlines()

# Strip the books database list of new line characters.
for i, line in enumerate(booksdb_list):
    booksdb_list[i] = line.strip()

books_list = []
for record in booksdb_list:
    split_book_record = record.split("|")
    books_list.append(split_book_record)

for book in books_list:
    book_file = book[0] + "_" + book[1].title() + ".adoc"
    os.system("touch " + book_file)

    with open(book_file, "a") as book_adoc_file:
        book_adoc_file.write("= " + book[3] + "\n")
        book_adoc_file.write(":toc:\n\n")

        for chapter in range(int(book[4])):
            book_adoc_file.write("== Chapter " + str(chapter+1) + "\n")
            book_adoc_file.write('\n[frame=ends,grid=rows,cols="10%,45%,45%"]\n')
            book_adoc_file.write("|===\n")
            book_adoc_file.write("|*Verse*\n")
            book_adoc_file.write("|*" + source_translation.upper() + "*\n")
            book_adoc_file.write("|*" + compare_translation.upper() + "*\n\n")

            for i, record in enumerate(sourcedb_list):
                split_source_record = record.split("|")
                source_verse_id = split_source_record[0].split(":")
                split_comp_record = compdb_list[i].split("|")
                comp_verse_id = split_comp_record[0].split(":")

                if source_verse_id[0] == book[2]:
                    if source_verse_id[1] == str(chapter+1):
                        if split_source_record[1] != split_comp_record[1]:
                            book_adoc_file.write("|**" + source_verse_id[1] + ":" + source_verse_id[2] + "**\n")
                            book_adoc_file.write("|" + split_source_record[1] + "\n")
                            book_adoc_file.write("|" + split_comp_record[1] + "\n\n")

            book_adoc_file.write("|===\n\n")
