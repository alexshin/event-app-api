FROM alexshin/docker-django-asgi-daphne:latest

LABEL maintainer="Alex Shinkevich <alex.shinkevich@gmail.com>"

# Create directory for the app
RUN mkdir -p /opt/app/event-app

# Some app-specific settings
ENV APP_WORKDIR=/opt/app/event-app
ENV APP_ASGI_ENTRYPOINT=_app.asgi:application
ENV DJANGO_SETTINGS_MODULE=_app.settings

# Add files to image
COPY . ${APP_WORKDIR}

# Install all requirements
USER root
RUN pip install --no-cache-dir -r ${APP_WORKDIR}/requirements.txt

USER ${DAPHNE_USER}

# Setup workdir for an entrypoint
WORKDIR /opt/app/event-app/src
