FROM postgres:alpine
ENV POSTGRES_USER=dbadmin
ENV POSTGRES_PASSWORD=admin
EXPOSE 5432
COPY ./dbinit.sql /docker-entrypoint-initdb.d/dbinit.sql