# Getting Started
# API Documentation

## 1. Serve the Frontend
GET /
- Serves the frontend of the application.
- Response: index.html page

## 2. Create a New Overlay
POST /overlays
- Creates a new overlay for the livestream.
- Request Body (JSON):
  {
      "content": "Overlay content (e.g., text, logo)",
      "height": 20,
      "width": 30,
      "left": 10,
      "top": 10
  }
- Response:
  {
      "message": "Overlay created successfully!"
  }

## 3. Get All Overlays
GET /overlays
- Retrieves a list of all overlays.
- Response:
  {
      "overlays": [
          {
              "_id": { "$oid": "overlayId1" },
              "content": "Sample Text",
              "height": 10,
              "width": 15,
              "left": 5,
              "top": 5
          }
      ]
  }

## 4. Update an Existing Overlay
PUT /overlays/<id>
- Updates an overlay by ID.
- Path Parameter: `id` (The ID of the overlay to update)
- Request Body (JSON):
  {
      "content": "Updated content",
      "height": 25,
      "width": 35,
      "left": 10,
      "top": 5
  }
- Response:
  {
      "message": "Overlay updated successfully!"
  }

## 5. Delete an Overlay
DELETE /overlays/<id>
- Deletes an overlay by ID.
- Path Parameter: `id` (The ID of the overlay to delete)
- Response:
  {
      "message": "Overlay deleted successfully!"
  }


# USER Documentation
To get started with the Livestream Overlays app, follow these simple steps:

1. Clone the app repository by running the following command in your terminal:

   ```bash
   git clone https://github.com/rohitkumar4826/RTSV_Streaming.git

   ```

2. Navigate to the root directory of the app.

   ```bash
   cd rtsp
   ```

3. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

4. Navigate to frontend and build project by running:

   ```bash
   cd frontend
   npm i
   npm run build
   cd ..
   ```

5. Start the app by running:

   ```bash
   python index.py
   cd frontend/
   npm run dev
   ```

6. Open your web browser and visit [http://localhost:10000](http://localhost:10000/) to use the Livestream Overlays app.

# Quickstart

```bash
   git clone https://www.github.com/melvinjariwala/livestream_app.git
   cd livestream_app
   pip install -r requirements.txt
   cd frontend
   npm i
   npm run build
   cd ..
   python index.py
```

Open your web browser and visit [http://localhost:10000](http://localhost:10000/) to use the Livestream Overlays app.
