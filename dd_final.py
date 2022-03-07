import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Detector Detective", layout="wide")
st. markdown("<h1 style='text-align: center; color: blue;'>Detector Detective</h1>", unsafe_allow_html=True)
c1, c2,c3 = st.columns([1,2,1])

with c1:    
    name1 = st.selectbox('Choose an image: ',('Bear','Clock','Vase','Stop','Kite','Train','Sheep','Bear','Motorcycle'))
    st.write('You selected:', name1)
    st.image([Image.open("final_images/"+name1+"_Standard.png"),Image.open("final_images/"+name1+"_Attacked.png")],caption = ["Standard","Attacked"])

with c2:
    
    page_names = ['Backbone','RPN','ROI']
    page = c2.radio('Zoom in to: ', page_names)
    if page == 'Backbone':        
        output_num = c2.slider("The layer output of the backbone I would like to view is: ",2,6 )
        st.image(Image.open("final_images/P"+str(output_num)+".png"))
        images_on_page= [Image.open("final_images/"+name1+"_P"+str(output_num)+"_unperturbed.png"), Image.open("final_images/"+name1+"_P"+str(output_num)+"_perturbed.png")]
        st.image(images_on_page, width = 450,caption = ["Standard","Attacked"])
    elif page == 'RPN':
        
        layer_names = ['Objectness Map','Anchor Deltas']
        ln = c2.radio('Select layer: ', layer_names)
        if (ln =='Objectness Map'):
            layer_input = 'Obj'
           
        elif (ln =='Anchor Deltas'):
            layer_input = 'AD'
        

        output_num = c2.slider("View the "+ln+" from Output Layer: "+str(),2,6 )   
        st.image(Image.open("final_images/"+page+"_"+layer_input+"_P"+str(output_num)+".png"),use_column_width  = True)     
        st.image([Image.open("final_images/"+name1+"_"+layer_input+"P"+str(output_num)+"_unperturbed.png"),Image.open("final_images/"+name1+"_"+layer_input+"P"+str(output_num)+"_perturbed.png")],caption = ["Standard","Attacked"],width = 450)

    elif page == 'ROI':
        st.image(Image.open("final_images/ROI.png"))
        st.image([Image.open('final_images/'+name1+'_Detection_unperturbed.png'),Image.open('final_images/'+name1+'_Detection_perturbed.png')],caption = ["Standard","Attacked"],width = 500)



op_names = ['Detection','Gradients',"Gradients1","Gradcam"]
op = c3.radio('Show the overall : ', op_names)

with c3:
    st.image(Image.open('final_images/'+name1+'_'+op+'_unperturbed.png'),caption = "Standard",use_column_width = True)
    st.image(Image.open('final_images/'+name1+'_'+op+'_perturbed.png'),caption = "Attacked",use_column_width = True)
