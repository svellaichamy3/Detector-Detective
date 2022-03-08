
import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Detector Detective: Investigating the Effect of Adversarial Examples on Object Detectors", layout="wide")
st. markdown("<h2 style='text-align: center; color: blue;'>Detector Detective: Investigating the Effect of Adversarial Examples on Object Detectors</h2>", unsafe_allow_html=True)
c1, c2,c3 = st.columns([1,3,1])

with c1:    
    name1 = st.selectbox('Choose an image: ',('Bear','Clock','Vase','Stop','Kite','Train','Sheep','Bear','Motorcycle'))
    
    st.image([Image.open("final_images/"+name1+"_Standard.png"),Image.open("final_images/"+name1+"_Attacked.png")],caption = ["Standard","Attacked"],width = 250)

with c2:
    
    page_names = ['Backbone','RPN','ROI']
    page = c2.radio('Select Module: ', page_names)
    if page == 'Backbone':        
        #output_num = c2.slider("The layer output of the backbone I would like to view is: ",2,6 )
        st.image(Image.open("final_images/FPN.png"),width = 550)
        images_on_page1= [Image.open("final_images/"+name1+"_P2_unperturbed.png"),
        Image.open("final_images/"+name1+"_P3_unperturbed.png"),
        Image.open("final_images/"+name1+"_P4_unperturbed.png"),
        Image.open("final_images/"+name1+"_P5_unperturbed.png"),
        Image.open("final_images/"+name1+"_P6_unperturbed.png")]
        images_on_page2 = [Image.open("final_images/"+name1+"_P2_perturbed.png"),
        Image.open("final_images/"+name1+"_P3_perturbed.png"),
        Image.open("final_images/"+name1+"_P4_perturbed.png"),
        Image.open("final_images/"+name1+"_P5_perturbed.png"),
        Image.open("final_images/"+name1+"_P6_perturbed.png")]
        st.image(images_on_page1, width = 200,caption = ["P2 Original","P3 Original","P4 Original","P5 Original","P6 Original"])
        st.image(images_on_page2, width = 200,caption = ["P2 Attacked","P3 Attacked","P4 Attacked","P5 Attacked","P6 Attacked"])
    elif page == 'RPN':
        ln = st.selectbox('Select Map: ',('Objectness Map','Anchor Deltas'))
        #layer_names = ['Objectness Map','Anchor Deltas']
        #ln = c2.radio('Select Map: ', layer_names)
        if (ln =='Objectness Map'):
            layer_input = 'Obj'
           
        elif (ln =='Anchor Deltas'):
            layer_input = 'AD'
        

        #output_num = c2.slider("View the "+ln+" from Output Layer: "+str(),2,6 )   
        st.image(Image.open("final_images/"+page+"_"+layer_input+".png"),width = 450)     
        st.image([
            Image.open("final_images/"+name1+"_"+layer_input+"P2_unperturbed.png"),
            Image.open("final_images/"+name1+"_"+layer_input+"P3_unperturbed.png"),
            Image.open("final_images/"+name1+"_"+layer_input+"P4_unperturbed.png"),
            Image.open("final_images/"+name1+"_"+layer_input+"P5_unperturbed.png"),
            Image.open("final_images/"+name1+"_"+layer_input+"P6_unperturbed.png")],
            caption = [ln+ " for P2 Original",ln+ " for P3 Original",ln+ " for P4 Original",
            ln+ " for P5 Original",ln+ " for P6 Original"],width = 200)
        st.image([
            Image.open("final_images/"+name1+"_"+layer_input+"P2_perturbed.png"),
            Image.open("final_images/"+name1+"_"+layer_input+"P3_perturbed.png"),
            Image.open("final_images/"+name1+"_"+layer_input+"P4_perturbed.png"),
            Image.open("final_images/"+name1+"_"+layer_input+"P5_perturbed.png"),
            Image.open("final_images/"+name1+"_"+layer_input+"P6_perturbed.png")],
            caption = [ln+ " for P2 Attacked",ln+ " for P3 Attacked",ln+ " for P4 Attacked",
            ln+ " for P5 Attacked", ln+ " for P6 Attacked"],width = 200)

    elif page == 'ROI':
        st.image(Image.open("final_images/ROI.png"),width = 500)
        st.image([Image.open('final_images/'+name1+'_Detection_unperturbed.png'),
        Image.open('final_images/'+name1+'_Detection_perturbed.png')],
        caption = ["Standard","Attacked"],width = 250)



op_names = ['Detection',"Gradcam","Gradients"]
op = c3.radio('Show the overall : ', op_names)
if (op=="Gradients"):
    op="Gradients1"

with c3:
    st.image(Image.open('final_images/'+name1+'_'+op+'_unperturbed.png'),caption = "Standard",width = 250)
    st.image(Image.open('final_images/'+name1+'_'+op+'_perturbed.png'),caption = "Attacked",width = 250)
