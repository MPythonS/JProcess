FROM python:3

WORKDIR /usr/src/app


# 1. pip freeze > requirements.txt (sukurti requirements.txt per terminala) sugeneruojame requirements.txt faila

COPY requirements.txt .

# saugome requirements.txt faila i dabartine direktorija


RUN pip install -r requirements.txt

# COPY appso koda i image, jei parašytume . . tai nukopijuotu viska
COPY JuicePro .

# su EXPOSE nurodomas portas, kuri naudosim ir jis susiejamas su konteineriu
EXPOSE 8000
# nurodome porto numeri per kuri vyks komunikacija expose 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
# kol CMD veikia, konteineris negali buti sustabdytas
# 2. tada vykdom komanda: docker build .
# 3. tada vykdom komanda: docker build . -t juicepro (juicepro - pavadinimas)
# 4. galime perziureti images: docker images, docker ps (perziureti dabar veikiancius image)
# 5. paleidziam image: docker run juicepro (jei kazkas ivyko netaip tada kartojame 2-5 zingsnius)
# 6. norint paleisti docer reikia sumapinti portus. komanda: docker run -d -p 8000:8000 juicepro
# bet tai padarysime su docker_compose.yml faile
# 7. sukuriame docker_compose.yml faila
# kai pakeičiame docker_compose.yml failą, tai nereikia rašyti CMD, nes jis jau yra docker_compose.yml faile
# toliau komanda terminale docker build
# docker build -t ptf . (ptf - pavadinimas)
# docker images (perziureti image)
# docker run ptf (paleisti image)
# docker ps (perziureti paleistus image)
# docker stop (sustabdyti image, jei nurodysime image id arba pavadinima)
# docker rm (istrinti image, jei nurodysime image id arba pavadinima)
# doker exec -it ptf bash (paleisti image ir patekti i terminala)
# docker exec per cmd paleidžiamas su kodu: docker exec -it ptf python manage.py shell
# -it - interaktyvus terminalas
# docker give name to container: docker run --name ptf ptf
# docker run -d -p 8000:8000 ptf (paleisti image ir nurodyti portus( -d - paleisti image fone))