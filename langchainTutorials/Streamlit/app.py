# import streamlit as st
# import pandas as pd

# st.write("Here's our first attempt at using data to create a table:")
# # st.write(pd.DataFrame({
# #     'first column': [1, 2, 3, 4],
# #     'second column': [10, 20, 30, 40]
# # }))
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

# st.table(df)
# # st.dataframe(df)

#################################################################

# import streamlit as st
# import numpy as np
# import pandas as pd

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))

#####################################################################

# import streamlit as st
# import numpy as np
# import pandas as pd

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

#####################################################################


# import streamlit as st
# import numpy as np
# import pandas as pd

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)


###################################################################


# import streamlit as st
# import numpy as np
# import pandas as pd

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

############################################################################

# import streamlit as st
# import time

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'


###########################################################


# import streamlit as st

# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# st.session_state.counter += 1

# st.header(f"This page has run {st.session_state.counter} times.")
# st.button("Run it again")

################################################################

import streamlit as st
import pandas as pd
import numpy as np

# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

#https://console.cloud.google.com/auth?project=tough-gearing-367303
# RandomData

import streamlit as st

if st.experimental_user.is_logged_in:
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.markdown(f"# {st.experimental_user.name}")
    st.write("Email : ",st.experimental_user.email)
    if st.button("Log out"):
        st.logout()
    
else:
    if st.button("Log in"):
        st.login("google")

        
st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

    
    
    