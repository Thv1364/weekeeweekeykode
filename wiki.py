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
    links = fetch_links(start_page)


start_page=wiki.page("Northwest Airlines Flight 255")
#target_page=wiki.page("Rugby station (North Dakota)")
target_page=wiki.page("West Caribbean Airways Flight 708")

#print(start_page.links)
#print(fetch_links(start_page))



womps=fetch_links(start_page)

for womp in womps:
    if womp==target_page.title:
        print("we found it! the name is", womp)
    #else:
    #    print("nope")
