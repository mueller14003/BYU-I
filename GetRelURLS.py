class Invalid(Exception):
    pass


urla = "https://www.lds.org/scriptures/"

scriptdict = {
    # The Old Testament
    "Genesis":"ot/gen/",
    "Exodus":"ot/ex/",
    "Leviticus":"ot/lev/",
    "Numbers":"ot/num/",
    "Deuteronomy":"ot/deut/",
    "Joshua":"ot/josh/",
    "Judges":"ot/judg/",
    "Ruth":"ot/ruth/",
    "1 Samuel":"ot/1-sam/",
    "2 Samuel":"ot/2-sam/",
    "1 Kings":"ot/1-kgs/",
    "2 Kings":"ot/2-kgs/",
    "1 Chronicles":"ot/1-chr/",
    "2 Chronicles":"ot/2-chr/",
    "Ezra":"ot/ezra/",
    "Nehemiah":"ot/neh/",
    "Esther":"ot/esth/",
    "Job":"ot/job/",
    "Psalms":"ot/ps/",
    "Proverbs":"ot/prov/",
    "Ecclesiastes":"ot/eccl/",
    "Song of Solomon":"ot/song/",
    "Isaiah":"ot/isa/",
    "Jeremiah":"ot/jer/",
    "Lamentations":"ot/lam/",
    "Ezekiel":"ot/ezek/",
    "Daniel":"ot/dan",
    "Hosea":"ot/hosea/",
    "Joel":"ot/joel/",
    "Amos":"ot/amos/",
    "Obadiah":"ot/obad/",
    "Jonah":"ot/jonah/",
    "Micah":"ot/micah/",
    "Nahum":"ot/nahum/",
    "Habakkuk":"ot/hab/",
    "Zephaniah":"ot/zeph/",
    "Haggai":"ot/hag/",
    "Zechariah":"ot/zech/",
    "Malachi":"ot/mal",
    # The New Testament
    "Matthew":"nt/matt/",
    "Mark":"nt/mark/",
    "Luke":"nt/luke/",
    "John":"nt/john/",
    "Acts":"nt/acts/",
    "Romans":"nt/rom/",
    "1 Corinthians":"nt/1-cor/",
    "2 Corinthians":"nt/2-cor/",
    "Galatians":"nt/gal/",
    "Ephesians":"nt/eph/",
    "Philippians":"nt/philip/",
    "Colossians":"nt/col/",
    "1 Thessalonians":"nt/1-thes/",
    "2 Thessalonians":"nt/2-thes/",
    "1 Timothy":"nt/1-tim/",
    "2 Timothy":"nt/2-tim/",
    "Titus":"nt/titus/",
    "Philemon":"nt/philem/",
    "Hebrews":"nt/heb/",
    "James":"nt/james/",
    "1 Peter":"nt/1-pet/",
    "2 Peter":"nt/2-pet/",
    "1 John":"nt/1-jn/",
    "2 John":"nt/2-jn/",
    "3 John":"nt/3-jn/",
    "Jude":"nt/jude/",
    "Revelation":"nt/rev/",
    # The Book of Mormon
    "1 Nephi":"bofm/1-ne/",
    "2 Nephi":"bofm/2-ne/",
    "Jacob":"bofm/jacob/",
    "Enos":"bofm/enos/",
    "Jarom":"bofm/jarom/",
    "Omni":"bofm/omni/",
    "The Words of Mormon":"bofm/w-of-m/",
    "Words of Mormon":"bofm/w-of-m/",
    "Mosiah":"bofm/mosiah/",
    "Alma":"bofm/alma/",
    "Helaman":"bofm/hel/",
    "3 Nephi": "bofm/3-ne/",
    "4 Nephi": "bofm/4-ne/",
    "Mormon":"bofm/morm/",
    "Ether":"bofm/ether/",
    "Moroni":"bofm/moro/",
    # The Doctrine and Covenants
    "Doctrine and Covenants": "dc-testament/dc/",
    "D&C": "dc-testament/dc/",
    # The Pearl of Great Price
    "Moses":"pgp/moses/",
    "Abraham":"pgp/abr/",
    "Joseph Smith—Matthew":"pgp/js-m/",
    "Joseph Smith—History":"pgp/js-h/",
    "Articles of Faith":"pgp/a-of-f/",
}


def read_file(rfilename,url_list):
    file = open(rfilename,"r")
    for line in file:
        words = line.split(' ')
        try:
            book,rest = get_book(words)
        except Invalid:
            print("ERROR: Invalid scripture. Repent or go to Hell.")
            file.close()
            return
        url_maker(book,rest,url_list)
    file.close()


def write_file(wfilename,url_list):
    file = open(wfilename, "w")
    file.writelines(url_list)
    file.close()


def get_book(words):
    book = ""
    rest = ' '.join(words).strip()
    for word in words:
        book += word + ' '
        if book.strip() in scriptdict.keys():
            return book.strip(),rest.replace(book.strip(),'').strip()
    raise Invalid


def url_maker(book,rest,url_list):
    url = urla + scriptdict[book]
    if rest.strip() == "":
        url_list.append(url + "1" + '\n')
    elif ':' not in rest:
        if '-' not in rest:
            url_list.append(url + rest.strip() + '\n')
        else:
            for i in range(int(rest.strip()[0]),int(rest.strip()[2::])+1):
                url_list.append(url + str(i) + '\n')
    else:
        url_list.append(url + rest.split(':')[0].strip() + '.' + rest.split(':')[1].strip() + '\n')


def main():
    url_list = []
    rfilename = "REL.txt"
    wfilename = "URL.txt"
    if input("Use default filenames? (y/n) ") == 'n':
        rfilename = input("Please enter the filename of the file to be opened: ")
        wfilename = input("Please enter the filename of the file to be written to: ")
    read_file(rfilename,url_list)
    write_file(wfilename,url_list)


if __name__ == "__main__":
    main()
