# API Invoice Generation

This project is a FastAPI-based application designed to generate invoices in PDF format. It provides a simple and efficient way to create and manage invoices programmatically.

## Features

- Generate invoices in PDF format.
- RESTful API endpoints for invoice creation and retrieval.
- Customizable invoice templates.
- Lightweight and fast performance using FastAPI.

## Requirements

- Python 3.8+
- FastAPI
- ReportLab (or any other library for PDF generation)
- Uvicorn (for running the application)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/api-invoice-generation.git
    cd api-invoice-generation
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

3. Use the available endpoints to create and retrieve invoices.

## API Endpoints

### `POST /invoices/`
Create a new invoice. Provide the necessary details such as customer information, items, and total amount.

### `GET /invoices/{invoice_id}`
Retrieve an existing invoice by its ID.

## Example Request

### Create Invoice

```json
POST /invoices/
{
  "customer_name": "John Doe",
  "items": [
     {"description": "Product 1", "quantity": 2, "price": 50},
     {"description": "Product 2", "quantity": 1, "price": 100}
  ],
  "total_amount": 200
}
```

### Response

```json
{
  "invoice_id": "12345",
  "status": "Invoice generated successfully",
  "pdf_url": "/invoices/12345.pdf"
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or support, please contact Antonio at antonio@example.com.
