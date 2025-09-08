# Supply Chain Management Prototype
This project is a **sample supply chain management system** built to demonstrate database integration, CRUD operations, QA testing (manual + automated), and documentation following the **Systems Development Life Cycle (SDLC)**.

---

## ⚙️ Features
- **Database integration** with SQLite  
- **CRUD operations** for orders and warehouse inventory  
- **Console interaction** to place, check, and update orders  
- **Manual testing** documented in Excel  
- **Automated testing** with `pytest` 

---

## 🗄️ Database
The system uses two tables defined in `schema.sql`:  
- **orders** → order ID, client name, product, SKU, quantity, status  
- **warehouse_inventory** → SKU, product name, available stock  

Run `run-schema-sql.py` to reset and seed the database.  

---

## 🧪 Testing

### Manual Testing
See `docs/manual-testing.xlsx` for scenario-based test cases with preconditions, steps, expected/actual results.  

### Automated Testing
- **pytest**: for lightweight tests (`testing/tests/`)  

Run tests:
```bash
pytest -q
