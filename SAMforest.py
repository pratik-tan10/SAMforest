import streamlit as st
from streamlit_image_comparison import image_comparison
#import cv2


st.set_page_config("Segment All Model For segmenting forest", "")

st.header("Satellite Image compared with Segmented Forest")

#st.image(
#    cv2.cvtColor(cv2.imread("imgs/cover.png"), cv2.COLOR_BGR2RGB),
#)


st.write("")
"[Segment Anything Model (SAM) from Meta AI Research](https://github.com/facebookresearch/segment-anything), FAIR, was used to segment forest area masks on high resolution satellite images obtained from [DeepGlobe LandCover Classification Dataset](https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset). These segments were genereted in real-time with less 15 point prompts each. Images with small patches for either forest or non forest required more points for acceptable segmentaion than images with large patches for both forest and non-forest."
st.write("")


st.markdown("### Sparse Forest")
image_comparison(
    img1="imgs/Tthird.jpg",
    img2="imgs/third.png",
    label1="Satellite Image",
    label2="Segmented Forest",
)

st.markdown("### Forest with Agriculture")
image_comparison(
    img1="imgs/Tninth.jpg",
    img2="imgs/ninth.png",
    label1="Satellite Image",
    label2="Segmented Forest",
)

st.markdown("### Forest with Agriculture and Barren")
image_comparison(
    img1="imgs/Tfifth.jpg",
    img2="imgs/fifth.png",
    label1="Satellite Image",
    label2="Segmented Forest",
)


st.markdown("### Forest with Agriculture")
image_comparison(
    img1="imgs/Tsixth.jpg",
    img2="imgs/sixth.png",
    label1="Satellite Image",
    label2="Segmented Forest",
)

st.markdown("### Mostly forest")
image_comparison(
    img1="imgs/Teighth.jpg",
    img2="imgs/eighth.png",
    label1="Satellite Image",
    label2="Segmented Forest",
)

st.markdown("### Forest with Barren and Agriculture")
image_comparison(
    img1="imgs/Tfirst.jpg",
    img2="imgs/first.png",
    label1="Satellite Image",
    label2="Segmented Forest",
)


st.markdown("### Discrete Patches")
image_comparison(
    img1="imgs/Tsecond.jpg",
    img2="imgs/second.png",
    label1="Satellite Image",
    label2="Segmented Forest",
)

st.markdown("### Discrete Patches")
image_comparison(
    img1="imgs/Tseventh.jpg",
    img2="imgs/seventh.png",
    label1="Satellite Image",
    label2="Segmented Forest",
)
