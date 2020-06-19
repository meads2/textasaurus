RUN echo'Bulding Docker Image'
RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
RUN python -m textasaurus
