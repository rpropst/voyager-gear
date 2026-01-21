import React from 'react'
import ReactDOM from 'react-dom/client'
import './global.css'

import VoyagerApp from './App'
import { AuthProvider } from './contexts/AuthProvider'
import { CartProvider } from './contexts/CartProvider'

const root = ReactDOM.createRoot(document.getElementById('root')!)

// MSW mock server disabled - using real backend API
// Uncomment below to use mock data instead of real backend
/*
import('../mocks/browser')
  .then(async ({ worker }) => {
    return worker.start()
  })
  .then(() => {
    root.render(
      <AuthProvider>
        <CartProvider>
          <VoyagerApp />
        </CartProvider>
      </AuthProvider>,
    )
  })
*/// Render app directly without MSW
root.render(
  <AuthProvider>
    <CartProvider>
      <VoyagerApp />
    </CartProvider>
  </AuthProvider>,
)