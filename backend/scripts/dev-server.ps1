Param(
    [int]$Port = 8000
)

Write-Host "Starting Strategy Visualizer backend on port $Port..."
uvicorn app.main:app --reload --port $Port

