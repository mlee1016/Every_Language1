from typing import List
import random
import schedule
from All_Phrases.Japanese_Phrases.J_Linked_List2 import LinkedList,Node
import streamlit as st
from All_Phrases.Japanese_Phrases.All_Japanese_ph import *






import pandas as pd
options:str = st.selectbox("Pick a list to study:",(
                                                


  f"1.1 {korean_useful_polite.getDefault_Name()}",#"1.6 korean useful polite words",
  f"2.1 {korean_particle_polite.getDefault_Name()}",#"2.6 korean particle polite words",
  f"3.1 {korean_past_polite2.getDefault_Name()}",#"3.6 korean past polite words 2",
  f"4.1 {korean_present_polite.getDefault_Name()}",#"4.6 korean present polite words",
  f"5.1 {korean_future_polite.getDefault_Name()}",#"5.6 korean future polite words",
  f"6.1 {korean_future_polite2.getDefault_Name()}",#"6.6 korean future polite words 2",
  f"7.1 {korean_past_polite.getDefault_Name()}",#"7.2 korean past polite words",
  ),index=None,placeholder="Select List")

#if options != None or options == "":

        
if options != None or options == "":
    
    studying_list = []
    if (int(options[2])%2 != 0): 
        studying_list:list = All_korean_lists[int(str(options[0]))-1].de_ko_List
    
        df1 = pd.DataFrame(studying_list)
        sol = df1.columns.tolist()
        en_ko = df1[[sol[1],sol[0]]].to_numpy().tolist()
    #st.write(*en_ko)
    else:
      studying_list:list = list(All_words_korean[int(str(options[0]))-1]) 

    
    List_ko = [["Really?",  "진짜요 / 진짜?"],
    ["Of course.",  "당연하죠 / 당연하지."] ,
    ["What's wrong?", "왜 그래요? / 왜 그래? "],
    ["Are you okay?",  "괜찮아요? /  괜찮아?"],
    ["I'm okay / It's okay",  "괜찮아요. / 괜찮아"],
    ["Right?",  "그쵸 / 그치?"],
    ["I don't know.",  "몰라요  / 몰라."],
    ["I know.","알아요.  /  알아."],
    ["Yes","네 / 응."],
    ["No.","아니요 / 아니."]]


    
    
    
    
    
    try:
        Ko_Linked_list2= LinkedList()
        Ko_Linked_list = LinkedList()
        on = st.toggle("Korean -> English")
        if on:
            st.write("Feature activated!")
            
            
            #st.session_state.KO_List = Ko_Linked_list
        
            st.session_state.KO_List1 = Ko_Linked_list
            #st.session_state.ind = 0
            studying_list = en_ko
            

            deleted_linked_list = LinkedList()
    
            Ko_Linked_list.head = Node(studying_list[0])

            for i in range(1,len(studying_list)):   
                Ko_Linked_list.append(studying_list[i])
        #Ko_Linked_list.print_list()
        
    #print(random.choice(List_ko))
    #print("success")



    #def add(a:int) -> int:
        #def add_again(e:int) -> int:

            #return a + e 
        #return add_again




    #r = add(2)
    #print(r(7))



        
            #st.write(Ko_Linked_list.print_list(),"-------------------")
            def task(data:str):
                pass
                #deleted_linked_list = LinkedList()
                deleted_linked_list.append(data)
            def task2():

                Ko_Linked_list.append(deleted_linked_list.data)



            schedule.every().day.at('00:00').do(task2)


            if 'ind' not in st.session_state:
                st.session_state.ind = 0
            if 'KO_List' not in st.session_state:
                st.session_state.KO_List1 = Ko_Linked_list
            sA = False

            def nextPhrases():
                st.session_state.ind +=1
            ph = st.container()
            
            if st.session_state.KO_List1.get_node(st.session_state.ind) == None:
                st.session_state.KO_List1 = Ko_Linked_list
            
            
            ph.write(f"{str(st.session_state.ind+1)}/{str(len(studying_list))}")

            ph.subheader(st.session_state.KO_List1.get_node(st.session_state.ind).data[0])

            if st.button("Show Answer:",use_container_width=True):
                
                ph.text(st.session_state.KO_List1.get_node(st.session_state.ind).data[1])


                
                #col2, col3 = st.columns([7,1])

                
                #with col2:

                st.button("again",on_click=nextPhrases)

                    
                        #st.session_state.inde +=1
                
                #with col3:
                    #if st.button("1 day",on_click=nextPhrases):
                        #st.session_state.KO_List.delete_node(st.session_state.inde) <---- working on this
                        #pass

                    
                        #st.session_state.inde +=1
      #for i in range (len(list(en_ko[st.session_state.a][1]))):
      #shuffle_list = list(en_ko[st.session_state.inde][1])
      #random.shuffle((shuffle_list))
      #st.write(*shuffle_list)
      
        
        
        else:  


            Ko_Linked_list2.head = Node(studying_list[0])

            for i in range(1,len(studying_list)):   
                Ko_Linked_list2.append(studying_list[i])
        #Ko_Linked_list.print_list()
        
    #print(random.choice(List_ko))
    #print("success")



    #def add(a:int) -> int:
        #def add_again(e:int) -> int:

            #return a + e 
        #return add_again




    #r = add(2)
    #print(r(7))



        
            #st.write(Ko_Linked_list.print_list(),"-------------------")
            def task(data:str):
                pass
                #deleted_linked_list = LinkedList()
                deleted_linked_list.append(data)
            def task2():

                Ko_Linked_list2.append(deleted_linked_list.data)



            schedule.every().day.at('00:00').do(task2)


            if 'inde' not in st.session_state:
                st.session_state.inde = 0
            if 'KO_List' not in st.session_state:
                st.session_state.KO_List2 = Ko_Linked_list2
            sA = False

            def nextPhrases():
                st.session_state.inde +=1
            ph2 = st.container()
            
            if st.session_state.KO_List2.get_node(st.session_state.inde) == None:
                st.session_state.KO_List2 = Ko_Linked_list2
            
            #print("-------------------------------------------")
            #st.write(st.session_state.KO_List.print_list())
            ph2.write(f"{str(st.session_state.inde+1)}/{str(len(studying_list))}")
            ph2.subheader(st.session_state.KO_List2.get_node(st.session_state.inde).data[0])

            if st.button("Show Answer:",use_container_width=True):
                
                ph2.text(st.session_state.KO_List2.get_node(st.session_state.inde).data[1])


                
                #col2, col3 = st.columns([7,1])

                
                #with col2:

                if st.button("again",on_click=nextPhrases):

                    
                    st.session_state.inde +=1
                
                #with col3:
                    #if st.button("Day",on_click=nextPhrases):
                        #st.session_state
                        #st.session_state.KO_List.delete_node(st.session_state.KO_List.get_node(st.session_state.inde)) #<---- working on this
                        #

                    
                        #st.session_state.inde +=1
            
            #print("sssssssssssssssssssssssssssss")    
            #st.write(st.session_state.KO_List.get_length())
    except(AttributeError,NameError):
        st.cache_data.clear()
        #st.session_state.KO_List = Ko_Linked_list
        st.session_state.KO_List2 = Ko_Linked_list2
        st.session_state.KO_List1 = Ko_Linked_list
        st.session_state.inde = 0
        st.session_state.ind = 0
        st.rerun()
        #if not GA_answer:
    #   st.stop()
    #else:   
#   get_Answer()
#    GA_answer = False



#st.write(Ko_Linked_list.print_list())
#except(AttributeError):
        
        #st.success("Done")


#if  __name__ == '__main__':
   # '''l_list = LinkedList()
    #l_list.head = Node(1)
    #second = Node(2)
    #third = Node(3)

    #l_list.head.next = second
    #second.next = third

    # Get the next node of the head
    #next_node = l_list.head.next
    #print(next_node.data)  # Output: 2'''

    #main()
