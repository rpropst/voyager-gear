import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useCheckout } from '@/contexts/CheckoutProvider'

export default function ConfirmationStep() {
  const navigate = useNavigate()
  const { resetCheckout } = useCheckout()

  const handleContinueShopping = () => {
    resetCheckout()
    navigate('/products')
  }

  const handleViewOrders = () => {
    resetCheckout()
    navigate('/orders')
  }

  return (
    <div className="confirmation-step max-w-2xl mx-auto text-center py-12">
      <div className="mb-8">
        <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
          <svg
            className="w-10 h-10 text-green-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M5 13l4 4L19 7"
            />
          </svg>
        </div>
        <h2 className="text-3xl font-bold text-gray-900 mb-2">
          Order Confirmed!
        </h2>
        <p className="text-gray-600">
          Thank you for your purchase. Your order has been successfully placed.
        </p>
      </div>

      <div className="bg-gray-50 rounded-lg p-6 mb-8">
        <h3 className="text-lg font-semibold mb-4">What's Next?</h3>
        <div className="space-y-3 text-left">
          <div className="flex items-start">
            <div className="flex-shrink-0 w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center mr-3">
              <span className="text-blue-600 text-sm font-bold">1</span>
            </div>
            <div>
              <p className="font-medium">Order Confirmation</p>
              <p className="text-sm text-gray-600">
                You'll receive an email confirmation shortly
              </p>
            </div>
          </div>
          <div className="flex items-start">
            <div className="flex-shrink-0 w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center mr-3">
              <span className="text-blue-600 text-sm font-bold">2</span>
            </div>
            <div>
              <p className="font-medium">Processing</p>
              <p className="text-sm text-gray-600">
                We'll prepare your items for shipment
              </p>
            </div>
          </div>
          <div className="flex items-start">
            <div className="flex-shrink-0 w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center mr-3">
              <span className="text-blue-600 text-sm font-bold">3</span>
            </div>
            <div>
              <p className="font-medium">Shipping</p>
              <p className="text-sm text-gray-600">
                Track your package once it ships
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="flex flex-col sm:flex-row gap-4 justify-center">
        <button
          onClick={handleViewOrders}
          className="bg-blue-600 text-white py-3 px-6 rounded hover:bg-blue-700"
        >
          View Order History
        </button>
        <button
          onClick={handleContinueShopping}
          className="bg-gray-200 text-gray-800 py-3 px-6 rounded hover:bg-gray-300"
        >
          Continue Shopping
        </button>
      </div>
    </div>
  )
}
