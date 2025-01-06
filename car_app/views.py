from django.shortcuts import render, redirect # type: ignore
from django.views.generic import ListView # type: ignore
from django.views import View # type: ignore
from django.urls import reverse_lazy, reverse # type: ignore
from .forms import CarForm
from django.http import Http404 # type: ignore

from django.db import connection # type: ignore

from .models import Car, InsurancePolicy

# Create your views here.

class StartingPageView(View):
    def get(self, request):
        return render(request, "car_app/index.html")

class ContactPageView(View):
    def get(self, request):
        return render(request, "car_app/contact.html")
# optimmize code done.
def cars_view(request):
    print("cars_view")
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                car.id AS car_id,
                car.vin,
                car.color,
                model.name AS model_name,
                model.year AS model_year,
                model.make_id
            FROM
                car_app_car AS car
            JOIN
                car_app_model AS model
            ON
                car.model_id = model.id;
            """)

        cars = cursor.fetchall()

    # Map query results to dictionary for easier access in template
    cars_data = [
        {
            'car_id': car[0],
            'vin': car[1],
            'color': car[2],
            'model_name': car[3],
            'model_year': car[4],
            'make_name': car[5]
        }
        for car in cars
    ]
    # Render the template with the sorted cars
    return render(request, "car_app/cars.html", {"cars": cars_data} )
# optimize code done
def car_detail_view(request, pk):
    # Fetch the car details using raw SQL
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
               car.id AS car_id,
                car.vin,
                car.color,
                model.name AS model_name,
                model.year AS model_year,
                make.name AS make_name,
                insurance.policy_number,
                insurance.company_name,
                insurance.coverage_type,
                insurance.expiration_date
            FROM
                car_app_car AS car
            JOIN
                car_app_model AS model
            ON
                car.model_id = model.id
            JOIN
                car_app_make AS make
            ON
                model.make_id = make.id
            LEFT JOIN
                car_app_insurancepolicy AS insurance
            ON
                car.id = insurance.car_id
            WHERE
                car.id = %s""", [pk])

        row = cursor.fetchone()
    if not row:
        raise Http404("Car not found")

    # Map query result to a dictionary for form initialization
    car_data = {
        'car_id': row[0],
        'color': row[2],
        'model': row[3],
        'model_year': row[4],
        'make_name': row[5],
        'policy_number': row[6],
        'company_name': row[7],
        'coverage_type': row[8],
        'expiration_date': row[9],
    }

    vin = row[1]  # Extract VIN for display but exclude from updates

    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            color = form.cleaned_data.get('color')
            model_name = form.cleaned_data.get('model_name')
            model_year = form.cleaned_data.get('model_year')
            make_name = form.cleaned_data.get('make_name')

            # Validate that no fields are missing
            if color and model_name and model_year and make_name:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE car_app_car
                        SET color = %s, model_id = (
                            SELECT id FROM car_app_model
                            WHERE name = %s AND year = %s
                        ), make_id = (
                            SELECT id FROM car_app_make
                            WHERE name = %s
                        )
                        WHERE id = %s
                    """, [color, model_name, model_year, make_name, pk])
                # Redirect to confirmation page
                print("Redirect to confirmation page")
                return redirect(reverse('update-success', args=[pk]))
            else:
                form.add_error(None, "One or more fields are missing. Please fill in all fields.")
    else:
        form = CarForm(initial=car_data)

    return render(request, "car_app/car-details.html", {'form': form, 'vin': vin, 'car_data': car_data})

# optimize code done
def update_detail_view(request, pk):
    # Fetch the car details using raw SQL
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, model_id, vin, color
            FROM car_app_car
            WHERE id = %s
            """, [pk])
        row = cursor.fetchone()
        print(row)

    if not row:
        raise Http404("Car not found")

    # Map the SQL row to a dictionary for form initialization
    car_data = {
        'model': row[1],  # Foreign key ID for Model
        'vin': row[2],
        'color': row[3],
    }
    vin = row[2]  # Extract VIN for display but exclude from updates

    if request.method == "POST":
        print("POST METHOD - UPDATE SUCCESS - DEFAULT METHOD..")
        form = CarForm(request.POST)
        if form.is_valid():
            # Extract color field to update
            color = form.cleaned_data.get('color')

            # Perform the update
            with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE car_app_car
                        SET color = %s
                        WHERE id = %s
                     """, [color, pk])

            # Store updated data in session for the success view
            request.session['updated_data'] = {'color': color}
            request.session['car_data'] = {**car_data, 'color': color}

            # Redirect to success page
            return redirect(reverse('update-success', args=[pk]))
        else:
            form.add_error(None, "One or more fields are missing. Please fill in all fields.")
    else:
        form = CarForm(initial=car_data)

    return render(request, "car_app/update-details.html", {'form': form, 'vin': vin})

def update_success_view(request, pk):
    # Retrieve data from the session
    car_data = request.session.pop('car_data', None)
    updated_data = request.session.pop('updated_data', None)

    # Fallback if session data is missing
    if not car_data:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, model_id, vin, color
                FROM car_app_car
                WHERE id = %s
            """, [pk])
            row = cursor.fetchone()

        if not row:
            raise Http404("Car not found")

        car_data = {'model': row[1], 'vin': row[2], 'color': row[3]}
        updated_data = {}  # No specific updates available

    return render(
        request,
        "car_app/update_success.html",
        {"pk": pk, "car_data": car_data, "updated_data": updated_data}
    )

# Delete View
def delete_car_view(request, pk):
    # Fetch the car details using raw SQL
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM car_app_car WHERE id = %s", [pk])
        row = cursor.fetchone()

    if not row:
        raise Http404("Car not found")

    # If the request is POST, delete the record
    if request.method == 'POST':
        # If not POST, show confirmation page
        print("GET POST  - DELETE SUCCESS - DEFAULT METHOD..")
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM car_app_insurancepolicy WHERE car_id = %s", [pk])
            cursor.execute("DELETE FROM car_app_car WHERE id = %s", [pk])

        # Redirect to car list page after successful deletion
        print("lets's to redirect now and confirm the delete with pk - delete-sucess...")
        return redirect(reverse('delete-success', args=[pk]))  # Redirect to the page where you confirm delete

    print("I should be here after post is done and redirect comes to here....")
    return render(request, "car_app/delete_success.html", {'car_id': pk})

def delete_success_view(request, pk):
    print(f"Rendering success page for car ID: {pk}")
    return render(request, "car_app/delete_success.html", {"pk": pk})
