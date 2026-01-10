# RCV Source Files

RCV Website: https://www.revisedcommonversion.com or https://rcv.us.com

This repository contains the source files for the RCV project. These files satisfy the "source code" that is to be made available as per the Eclipse Public License, version 2.0.

There are two different source file types in this repository:
1. A text database
2. The text presented in AsciiDoctor format

## Database

The database is a plain text file that is pipe (`|`) delimited into two fields: 1) verse ID, and 2) verse text. The verse ID is colon (`:`) delimited into three fields: 1) book abbreviation, 2) chapter number, and 3) verse number.

Example:
- `gen:1:1|In the beginning God created the heaven and the earth.`

## Text File

The text files are presented in AsciiDoctor format and include the full text of the RCV in paragraph form, with each book containing its own file. The `.txt` files are formatted with AsciiDoctor syntax and can be opened with a plain text editor. Changing the file extension from `.txt` to `.adoc` will allow text editors to utilize AsciiDoctor syntax highlighting and facilitate conversion to other formats using [AsciiDoctor](https://asciidoctor.org/#installation). I chose to upload these files as `.txt` files to prevent Github from showing the rednered file, and instead, show the text as "source code."

## Additional Resources

In addition to the source files, I have also included some additional resources.
- In the _Database_ folder, I have included a database file for the chapter outlines.
- There's a folder named _Differences_ that contains three subfolders. Each of these folders contains a comparison between two Biblical texts. There is a difference folder comparing the KJV and the Webster, one comparing the Webster and the RCV, and comparing for the KJV and the RCV. Here are a few notes on these files.
  - The files are in AsciiDoctor format and can be displayed in this repository.
  - The files contain tables showing only the verses that are different between the two translations.
  - Verses are displayed side by side in the table.

## Change Log

If you're interested in seeing a change log of the RCV text, visit the [Commits page](https://github.com/revisedcommonversion/revisedcommonversion.github.io/commits/master/) for the RCV website.

## License

Copyright © 2026 William Masopust

This work and the accompanying materials are made available under the terms of the Eclipse Public License 2.0. Information on this license may be found at https://www.eclipse.org/legal/epl-2.0/.

You are free to copy, display, distribute, quote, or share this work in part or in whole. You are also free to modify this work or create derivative works of your own based upon this work.

> Freely you have received, freely give.
> 
> ---Matthew 10:8

When quoting the RCV, you may simply use the "RCV" abbreviation with quotations, or you may note the Revised Common Version as a source for quotations, such as in a list of sources or a bibliography. When attributing this work in other modifications and derivative works, please retain all copyright notices and note that your work is a derivative of or based on the Revised Common Version. I would also appreciate a link to the RCV website with any attributions.

Any distribution of the RCV, with or without modifications or as derivative works, must be made under the terms of the Eclipse Public License 2.0. Please follow the above URL so that you may read the license and know your rights regarding the usage of this work. The full text of the license is also contained at the end of this book under the section, _License_, in the Appendix. The Eclipse Public License is a Copyleft license that ensures that everyone who receives a work under the license is given the same freedoms to use the work.

The title, _The Holy Bible: Revised Common Version_, and the RCV logo are unregistered trademarks. They may not be used for derivative works, except as may be necessary to comply with the attribution requirements of the license.

If you have any questions concerning the terms or usage of this text, please feel free to contact me via e-mail (`info@rcv.us.com`).

### Applying the EPL to the RCV Project

Program:
: When this license mentions the "Program," that refers to the Work, or the text of the RCV project, whether in AsciiDoc files, or in the other forms of ePub, MOBI, PDF, or any other format in which the RCV can be represented. This can also apply to the RCV website. So, "Program" can be substituted with "Work."

Source Code:
: The source code, or source text, for the RCV project is contained in the AsciiDoc files and/or the plain text database file hosted in this repository.
