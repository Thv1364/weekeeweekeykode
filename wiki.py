from queue import Queue
import wikipediaapi
import time
#pip3 install wikipedia-api
#*# put that into terminal #*#

user_agent="p3_wiki (jmonson6@outlook.com)"
wiki=wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links=page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    print("working on it.....")
    start_time=time.time()

    queue=Queue()#queue for which items to check next
    visited=set()#keeps track of the visited links
    parent={}#dictionary to keep track of parent

    #starts off by adding the start page to our queue and visited
    queue.put(start_page.title)
    visited.add(start_page.title)


    while not queue.empty():
        current_page_title=queue.get()

        if current_page_title == target_page.title:
            break
        current_page=wiki.page(current_page_title)
        links=fetch_links(current_page)

        for link in links:
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link]=current_page_title
    
    path=[]
    page_title=target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        path_title = parent[page_title]


    path.append(start_page.title)
    path.reverse()

    end_time=time.time()
    print("this algorithm took",end_time-start_time, "seconds.")
    return path

start_page=wiki.page(input("Start: \n"))
#target_page=wiki.page("Rugby station (North Dakota)")
target_page=wiki.page(input("End: \n"))
path = wikipedia_game_solver(start_page, target_page)
print(path)
#print(start_page.links)
#print(fetch_links(start_page))     