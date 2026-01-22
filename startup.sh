#!/bin/bash

# Script to start all services for Voyager Gear e-commerce platform
# Run with: ./startup.sh

echo "Starting Voyager Gear services..."

# Start Backend (FastAPI)
echo "Starting Backend on port 5001..."
cd backend && uvicorn app.main:app --host 0.0.0.0 --port 5001 --reload &
BACKEND_PID=$!
cd ..

# Start Mock Validator Service (Go)
echo "Starting Mock Validator on port 5003..."
cd checkout-service/cmd/mock-validator && /opt/homebrew/bin/go run main.go &
VALIDATOR_PID=$!
cd ../../..

# Start Checkout Service (Go)
echo "Starting Checkout Service on port 5002..."
cd checkout-service && export $(cat .env | xargs) && /opt/homebrew/bin/go run main.go &
CHECKOUT_PID=$!
cd ..

# Wait a moment for services to start
sleep 3

# Start Frontend (Vite)
echo "Starting Frontend on port 3000..."
cd frontend && pnpm dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "All services started!"
echo "Backend: http://localhost:5001"
echo "Checkout Service: http://localhost:5002"
echo "Mock Validator: http://localhost:5003"
echo "Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop all services"

# Trap Ctrl+C and stop all services
trap "echo 'Stopping services...'; kill $BACKEND_PID $VALIDATOR_PID $CHECKOUT_PID $FRONTEND_PID 2>/dev/null; exit" INT

# Wait for all background processes
wait
