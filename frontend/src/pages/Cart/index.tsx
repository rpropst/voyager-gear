/**
 * Shopping Cart Page
 * Displays cart items, saved items, and cart summary
 */

import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useCart } from '@/hooks/useCart'
import { useAuth } from '@/hooks/useAuth'

const Cart: React.FC = () => {
  const navigate = useNavigate()
  const { cart, guestCart, isLoading, getSubtotal, removeCartItem, updateCartItem, promoCode, applyPromoCode, removePromoCode, calculateShippingTax, shippingTax } = useCart()
  const { isAuthenticated } = useAuth()

  const [promoCodeInput, setPromoCodeInput] = useState('')
  const [zipCodeInput, setZipCodeInput] = useState('')
  const [promoCodeLoading, setPromoCodeLoading] = useState(false)
  const [shippingLoading, setShippingLoading] = useState(false)

  const cartItems = isAuthenticated && cart ? cart.items : guestCart
  const subtotal = getSubtotal()

  // Calculate discount amount
  const discountAmount = promoCode && promoCode.is_valid
    ? subtotal * (promoCode.discount_percentage / 100)
    : 0

  // Calculate free shipping progress
  const freeShippingThreshold = 50
  const freeShippingProgress = Math.min((subtotal / freeShippingThreshold) * 100, 100)
  const amountToFreeShipping = Math.max(freeShippingThreshold - subtotal, 0)

  const handleApplyPromoCode = async () => {
    if (!promoCodeInput.trim()) return

    setPromoCodeLoading(true)
    try {
      await applyPromoCode(promoCodeInput)
    } catch (error) {
      // Error already handled in context
    } finally {
      setPromoCodeLoading(false)
    }
  }

  const handleCalculateShipping = async () => {
    if (!zipCodeInput.trim()) return

    setShippingLoading(true)
    try {
      await calculateShippingTax(zipCodeInput)
    } catch (error) {
      // Error already handled in context
    } finally {
      setShippingLoading(false)
    }
  }

  const handleRemoveItem = async (itemId: number) => {
    if (isAuthenticated && cart) {
      try {
        await removeCartItem(itemId)
      } catch (error) {
        console.error('Failed to remove item:', error)
      }
    }
  }

  const handleUpdateQuantity = async (itemId: number, newQuantity: number) => {
    if (isAuthenticated && cart && newQuantity > 0) {
      try {
        await updateCartItem(itemId, newQuantity)
      } catch (error) {
        console.error('Failed to update quantity:', error)
      }
    }
  }

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
          <p className="mt-4 text-gray-600">Loading cart...</p>
        </div>
      </div>
    )
  }

  // Empty cart state
  if (cartItems.length === 0) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center max-w-md mx-auto px-4">
          <div className="text-6xl mb-4">🛒</div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Your cart is empty</h1>
          <p className="text-gray-600 mb-6">
            Looks like you haven't added anything to your cart yet.
          </p>
          <Link
            to="/products"
            className="inline-block px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            Continue Shopping
          </Link>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Breadcrumb */}
      <div className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <nav className="flex items-center space-x-2 text-sm">
            <Link to="/" className="text-blue-600 hover:text-blue-800">
              Home
            </Link>
            <span className="text-gray-400">/</span>
            <span className="text-gray-600">Shopping Cart</span>
          </nav>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Shopping Cart</h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Cart Items */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-lg shadow-md overflow-hidden">
              {cartItems.map((item) => {
                const product = 'product' in item && item.product ? item.product : null
                if (!product) return null

                const itemKey = ('id' in item ? item.id : item.product_id) as number
                const itemId = ('id' in item ? item.id : 0) as number

                return (
                  <div key={itemKey} className="p-6 border-b last:border-b-0">
                    <div className="flex gap-4">
                      {/* Product Image */}
                      <Link to={`/products/${product.id}`}>
                        <img
                          src={product.image_url}
                          alt={product.name}
                          className="w-24 h-24 object-cover rounded-lg"
                        />
                      </Link>

                      {/* Product Info */}
                      <div className="flex-1">
                        <Link
                          to={`/products/${product.id}`}
                          className="text-lg font-semibold text-gray-900 hover:text-blue-600"
                        >
                          {product.name}
                        </Link>
                        <p className="text-sm text-gray-500 mt-1">{product.category}</p>
                        <p className="text-xl font-bold text-blue-600 mt-2">
                          ${product.price.toFixed(2)}
                        </p>
                      </div>

                      {/* Quantity and Remove */}
                      <div className="flex flex-col items-end gap-2">
                        {/* Quantity Selector */}
                        {isAuthenticated && 'id' in item && (
                          <div className="flex items-center border border-gray-300 rounded-lg">
                            <button
                              onClick={() => handleUpdateQuantity(itemId, item.quantity - 1)}
                              className="px-3 py-1 text-gray-600 hover:bg-gray-100"
                            >
                              -
                            </button>
                            <span className="px-4 py-1 border-l border-r border-gray-300">
                              {item.quantity}
                            </span>
                            <button
                              onClick={() => handleUpdateQuantity(itemId, item.quantity + 1)}
                              className="px-3 py-1 text-gray-600 hover:bg-gray-100"
                            >
                              +
                            </button>
                          </div>
                        )}
                        {!isAuthenticated && (
                          <span className="px-4 py-1 text-gray-600">Qty: {item.quantity}</span>
                        )}

                        {/* Item Total */}
                        <p className="text-lg font-semibold text-gray-900">
                          ${(product.price * item.quantity).toFixed(2)}
                        </p>

                        {/* Remove Button */}
                        {isAuthenticated && 'id' in item && (
                          <button
                            onClick={() => handleRemoveItem(itemId)}
                            className="text-sm text-red-600 hover:text-red-800"
                          >
                            Remove
                          </button>
                        )}
                      </div>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>

          {/* Cart Summary */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-lg shadow-md p-6 sticky top-4">
              <h2 className="text-xl font-bold text-gray-900 mb-4">Order Summary</h2>

              {/* Free Shipping Progress */}
              {amountToFreeShipping > 0 ? (
                <div className="mb-4">
                  <div className="flex justify-between text-sm text-gray-600 mb-2">
                    <span>Free shipping progress</span>
                    <span>${amountToFreeShipping.toFixed(2)} to go</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div
                      className="bg-green-500 h-2 rounded-full transition-all"
                      style={{ width: `${freeShippingProgress}%` }}
                    ></div>
                  </div>
                </div>
              ) : (
                <div className="mb-4 p-3 bg-green-100 text-green-800 rounded-lg text-sm font-medium">
                  ✓ You qualify for free shipping!
                </div>
              )}

              {/* Subtotal */}
              <div className="flex justify-between py-2">
                <span className="text-gray-600">Subtotal</span>
                <span className="font-semibold">${subtotal.toFixed(2)}</span>
              </div>

              {/* Promo Code */}
              <div className="border-t pt-4 mt-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Promo Code
                </label>
                {!promoCode ? (
                  <div className="flex gap-2">
                    <input
                      type="text"
                      value={promoCodeInput}
                      onChange={(e) => setPromoCodeInput(e.target.value.toUpperCase())}
                      placeholder="Enter code"
                      className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <button
                      onClick={handleApplyPromoCode}
                      disabled={promoCodeLoading}
                      className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-blue-400"
                    >
                      {promoCodeLoading ? '...' : 'Apply'}
                    </button>
                  </div>
                ) : (
                  <div className="flex justify-between items-center p-3 bg-green-100 text-green-800 rounded-lg">
                    <span className="font-medium">{promoCode.code} ({promoCode.discount_percentage}% off)</span>
                    <button
                      onClick={removePromoCode}
                      className="text-green-600 hover:text-green-800"
                    >
                      ✕
                    </button>
                  </div>
                )}

                {promoCode && (
                  <div className="flex justify-between py-2 text-green-600">
                    <span>Discount</span>
                    <span>-${discountAmount.toFixed(2)}</span>
                  </div>
                )}
              </div>

              {/* ZIP Code for Shipping/Tax */}
              <div className="border-t pt-4 mt-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  ZIP Code (for shipping & tax)
                </label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={zipCodeInput}
                    onChange={(e) => setZipCodeInput(e.target.value)}
                    placeholder="Enter ZIP"
                    maxLength={10}
                    className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <button
                    onClick={handleCalculateShipping}
                    disabled={shippingLoading}
                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-blue-400"
                  >
                    {shippingLoading ? '...' : 'Calculate'}
                  </button>
                </div>

                {shippingTax && (
                  <div className="mt-4 space-y-2">
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-600">State: {shippingTax.state}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-gray-600">Tax ({(shippingTax.tax_rate * 100).toFixed(2)}%)</span>
                      <span className="font-semibold">${shippingTax.tax_amount.toFixed(2)}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-gray-600">Shipping</span>
                      <span className="font-semibold">
                        {shippingTax.shipping_cost === 0 ? 'FREE' : `$${shippingTax.shipping_cost.toFixed(2)}`}
                      </span>
                    </div>
                  </div>
                )}
              </div>

              {/* Total */}
              <div className="border-t pt-4 mt-4">
                <div className="flex justify-between items-center">
                  <span className="text-xl font-bold">Total</span>
                  <span className="text-2xl font-bold text-blue-600">
                    ${shippingTax ? shippingTax.total.toFixed(2) : (subtotal - discountAmount).toFixed(2)}
                  </span>
                </div>
              </div>

              {/* Checkout Button */}
              <button
                onClick={() => navigate('/checkout')}
                className="w-full mt-6 px-6 py-4 bg-blue-600 text-white text-lg font-semibold rounded-lg hover:bg-blue-700 transition-colors"
              >
                Proceed to Checkout
              </button>

              <Link
                to="/products"
                className="block text-center mt-4 text-blue-600 hover:text-blue-800"
              >
                Continue Shopping
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Cart
