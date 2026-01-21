#!/bin/bash

  # Terminal 1 - Backend
  cd backend && source venv/bin/activate && python run.py

  # Terminal 2 - Mock Validator
  cd checkout-service/cmd/mock-validator && go run main.go

  # Terminal 3 - Checkout Service
  cd checkout-service && go run main.go

  # Terminal 4 - Frontend
  cd frontend && pnpm dev
