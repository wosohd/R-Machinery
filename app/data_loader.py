import csv
import os
from datetime import datetime
from app import create_app, db
from app.models import Machine

# Create and configure the Flask app
app = create_app()

# CSV file path
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'sample_data', 'machines.csv')

def load_machines_from_csv():
    with app.app_context():
        # Clear the existing machine data
        print("Deleting existing machines from the database...")
        Machine.query.delete()
        db.session.commit()

        # Load new data from the CSV
        print(f"Loading machines from: {CSV_FILE_PATH}")
        with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                machine = Machine(
                    name=row['name'],
                    year=int(row['year']),
                    make_model=row['make_model'],
                    serial_number=row['serial_number'] or None,
                    category=row['category'],
                    description=row['description'],
                    created_at=datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S')
                )
                db.session.add(machine)
                count += 1

            db.session.commit()
            print(f"{count} machines successfully loaded.")

if __name__ == '__main__':
    load_machines_from_csv()

