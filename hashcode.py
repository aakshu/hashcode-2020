def take_input():
    books_no, lib_no, total_days = map(int, input().split())
    book_scores = list(map(int, input().split()))
    list_of_lib = []

    def sortonscore(val):
        return book_scores[val]

    for i in range(lib_no):
        lib_info = tuple(map(int,input().split()))
        lib_books = list(map(int, input().split()))

        #lib_books has a list of the book ids for the books in that lib
        # sort this according to their scores ->

        lib_books.sort(key=sortonscore,reverse=True)

        list_item_to_add = [lib_info, lib_books]
        list_of_lib.append(list_item_to_add)
    return books_no,list_of_lib, total_days
        

#list_of_lib = [  [(5,2,2),[0,1,2,3,4]],  [(4,3,1),[3,2,5,0]]   ]
#books_to_scan = [1,2,3,6,5,4]

booksno,list_of_lib, total_days = take_input()
books_to_scan = list(range(0,booksno))

# [ (no_of_books,time_signup,scanning_rate),[bookslist..] ]
# check minimum number of days for signup

lib_no_and_signup_time=[]
i=0
for lib in list_of_lib:
    signup_time=lib[0][1]
    lib_no_and_signup_time.append((i,signup_time))
    i+=1

def sortSecond(val): 
    return val[1]

lib_no_and_signup_time.sort(key=sortSecond)

days_passed=0
lib_already_signed_up = []

for item in lib_no_and_signup_time:
    if(books_to_scan == []):
        break

    shipping_rate = list_of_lib[item[0]][0][2]
    no_books_in_lib = list_of_lib[item[0]][0][0]
    books_in_lib = list_of_lib[item[0]][1]
    if((set(books_in_lib)&set(books_to_scan)) and days_passed+item[1]<=total_days ):

        lib_already_signed_up.append([item[0]])
        days_passed+=item[1]


        days_remaining = total_days-days_passed
        if(no_books_in_lib <= (days_remaining * shipping_rate)):
            #scan all books blindly
            lib_already_signed_up[-1].append(books_in_lib) #results in a list of lists. [[lib_idx, books_scanned]]
            #remove respective books from book list needed
            for book in books_in_lib:
                if book in books_to_scan:
                    books_to_scan.remove(book)
        else:
            #compare book in lib with books_list_needed
            commonbooks = []
            for book in books_in_lib:
                if book in books_to_scan:
                    commonbooks.append(book)
            #sort books in descending order according to book score
            #remove days_remaining*shipping_rate no. of books
            lib_already_signed_up[-1].append(books_in_lib[0:days_remaining*shipping_rate])
            for book in books_in_lib[0:days_remaining*shipping_rate]:
                if book in books_to_scan[0:days_remaining*shipping_rate]:
                    books_to_scan.remove(book)

            #remove respective books from book list needed
    else:
        break 


no_of_lib_signedup = len(lib_already_signed_up)
print(no_of_lib_signedup)
for lib in lib_already_signed_up:
    print(str(lib[0]) + ' ' + str(len(lib[1]))) 
    for book in lib[1]:
        print(book, end=' ')
    print()