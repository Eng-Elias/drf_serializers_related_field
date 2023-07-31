# Simplifying CRUD Operations with Django REST Framework Serializers and RelatedFields

![Django](https://img.shields.io/badge/Django-4.2.1-brightgreen.svg)
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.14.0-brightgreen.svg)

## Overview

This repository contains a Django project that demonstrates how to build a powerful CRUD API using Django REST Framework (DRF) serializers, with a focus on utilizing the RelatedField feature. DRF serializers provide a convenient way to handle data transformation and make data exchange more efficient, enabling developers to concentrate on the core logic of their applications.

The main purpose of this project is to showcase how to use the RelatedField in DRF to handle ForeignKey fields in models. With a simple serializer setup, we can easily transform data representations and receive data from various formats, such as integers, strings, or objects, while maintaining data integrity.

## Medium Article

For a detailed explanation and walkthrough of the code in this repository, you can read the accompanying Medium article: ["Simplifying CRUD Operations with Django REST Framework Serializers and RelatedFields"](https://medium.com/@eng_elias/simplifying-crud-operations-with-django-rest-framework-serializers-and-relatedfields-fe333bb09b3c)

## Getting Started

To run this project locally on your machine, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Eng-Elias/drf_serializers_related_field.git
```

2. Create a virtual environment (optional but recommended):

```bash
cd drf_serializers_related_field
python -m venv venv
```

3. Activate the virtual environment:

- For Windows:

```bash
.\venv\Scripts\activate
```

- For macOS/Linux:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

Now, you should have the Django application up and running locally at `http://127.0.0.1:8000/`.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request. Your contributions are highly appreciated!

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for exploring our project! We hope you find it helpful and insightful. If you have any questions or feedback, please don't hesitate to reach out. Happy coding!
