import fees_backend

all_data = fees_backend.view()

for rows in all_data:
    print(rows)