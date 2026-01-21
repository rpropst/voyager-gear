import React from 'react'
import { useCheckout } from '@/contexts/CheckoutProvider'
import { useCart } from '@/hooks/useCart'

export default function CartReviewStep() {
  const { goToNextStep } = useCheckout()
  const { cart, guestCart, getCartItemCount, getSubtotal } = useCart()

  const items = cart?.items || guestCart || []
  const itemCount = getCartItemCount()
  const subtotal = getSubtotal()

  if (items.length === 0) {
    return (
      <div className="cart-review-step">
        <h2 className="text-2xl font-bold mb-6">Review Your Order</h2>
        <div className="text-center py-12">
          <p className="text-gray-600 mb-4">Your cart is empty</p>
          <a href="/products" className="text-blue-600 hover:underline">
            Continue Shopping
          </a>
        </div>
      </div>
    )
  }

  return (
    <div className="cart-review-step">
      <h2 className="text-2xl font-bold mb-6">Review Your Order</h2>

      <div className="space-y-4 mb-8">
        {items.map((item: any) => {
          const product = item.product || {}
          const quantity = item.quantity || 1
          const price = product.price || 0

          return (
            <div
              key={item.id || item.product_id}
              className="flex items-center gap-4 p-4 border rounded"
            >
              {product.image_url && (
                <img
                  src={product.image_url}
                  alt={product.name}
                  className="w-20 h-20 object-cover rounded"
                />
              )}
              <div className="flex-1">
                <h3 className="font-semibold">{product.name}</h3>
                <p className="text-sm text-gray-600">Quantity: {quantity}</p>
              </div>
              <div className="text-right">
                <p className="font-semibold">${(price * quantity).toFixed(2)}</p>
                <p className="text-sm text-gray-600">${price.toFixed(2)} each</p>
              </div>
            </div>
          )
        })}
      </div>

      <div className="border-t pt-4 mb-8">
        <div className="flex justify-between items-center mb-2">
          <span className="text-gray-600">Subtotal ({itemCount} items):</span>
          <span className="text-xl font-bold">${subtotal.toFixed(2)}</span>
        </div>
        <p className="text-sm text-gray-500">
          Tax and shipping will be calculated in the next steps
        </p>
      </div>

      <button
        onClick={goToNextStep}
        className="w-full bg-blue-600 text-white py-3 px-4 rounded hover:bg-blue-700"
      >
        Continue to Delivery
      </button>
    </div>
  )
}
