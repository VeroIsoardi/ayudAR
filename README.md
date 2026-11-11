# AyudAR

A prototype that helps people in Buenos Aires province find donation centres (clothes, food, plasma, blood): where they are on a map, opening hours, contact details and each municipality's lockdown phase, plus booking a visit.

Built by a team of 4 for *Proyecto de Software* (Licenciatura en Sistemas, UNLP, 2020).

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js_2-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)

## Two apps

- **Public app** ([`web/`](web/), Vue.js): browse centres, book a visit, suggest a new centre, see site statistics.
- **Admin app** ([`app/`](app/), Flask + Bootstrap): user management, donation-centre CRUD, system configuration.

Both were deployed on the university's servers during the course; those deployments are no longer online.

## Run it

```bash
# Admin app + API
pip install -r requirements.txt
python run.py

# Public app
cd web
npm install
npm run serve
```
