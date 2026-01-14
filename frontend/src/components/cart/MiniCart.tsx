/**
 * Mini Cart Component
 * Dropdown preview of cart items from header
 */

import React, { useState, useRef, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useCart } from '@/hooks/useCart'
import { useAuth } from '@/hooks/useAuth'

const MiniCart: React.FC = () => {
  const { cart, guestCart, getSubtotal, getCartItemCount } = useCart()
  const { isAuthenticated } = useAuth()
  const [isOpen, setIsOpen] = useState(false)
  const dropdownRef = useRef<HTMLDivElement>(null)

  const cartItems = isAuthenticated && cart ? cart.items : guestCart
  const itemCount = getCartItemCount()
  const subtotal = getSubtotal()

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false)
      }
    }

    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  // Show first 5 items
  const displayItems = cartItems.slice(0, 5)
  const hasMoreItems = cartItems.length > 5

  return (
    <div className="relative" ref={dropdownRef}>
      {/* Cart Icon Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        onMouseEnter={() => setIsOpen(true)}
        className="relative p-2 text-white hover:bg-gray-700 rounded-lg transition-colors"
      >
        <svg
          className="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
          />
        </svg>
        {itemCount > 0 && (
          <span className="absolute -top-1 -right-1 bg-red-600 text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center">
            {itemCount > 9 ? '9+' : itemCount}
          </span>
        )}
      </button>

      {/* Dropdown */}
      {isOpen && (
        <div
          className="absolute right-0 mt-2 w-96 bg-white rounded-lg shadow-xl border border-gray-200 z-50"
          onMouseLeave={() => setIsOpen(false)}
        >
          <div className="p-4 border-b border-gray-200">
            <h3 className="text-lg font-semibold text-gray-900">
              Shopping Cart ({itemCount} {itemCount === 1 ? 'item' : 'items'})
            </h3>
          </div>

          {cartItems.length === 0 ? (
            <div className="p-8 text-center">
              <div className="text-4xl mb-2">🛒</div>
              <p className="text-gray-600">Your cart is empty</p>
            </div>
          ) : (
            <>
              {/* Cart Items */}
              <div className="max-h-96 overflow-y-auto">
                {displayItems.map((item) => {
                  const product = 'product' in item && item.product ? item.product : null
                  if (!product) return null

                  const itemKey = ('id' in item ? item.id : item.product_id) as number
                  
                  return (
                    <Link
                      key={itemKey}
                      to={`/products/${product.id}`}
                      onClick={() => setIsOpen(false)}
                      className="flex gap-3 p-4 hover:bg-gray-50 transition-colors border-b border-gray-100"
                    >
                      <img
                        src={product.image_url}
                        alt={product.name}
                        className="w-16 h-16 object-cover rounded"
                      />
                      <div className="flex-1 min-w-0">
                        <p className="text-sm font-medium text-gray-900 truncate">
                          {product.name}
                        </p>
                        <p className="text-sm text-gray-500">Qty: {item.quantity}</p>
                        <p className="text-sm font-semibold text-blue-600">
                          ${(product.price * item.quantity).toFixed(2)}
                        </p>
                      </div>
                    </Link>
                  )
                })}

                {hasMoreItems && (
                  <div className="p-3 text-center text-sm text-gray-600 bg-gray-50">
                    +{cartItems.length - 5} more {cartItems.length - 5 === 1 ? 'item' : 'items'}
                  </div>
                )}
              </div>

              {/* Footer */}
              <div className="p-4 border-t border-gray-200">
                <div className="flex justify-between items-center mb-4">
                  <span className="text-gray-600">Subtotal:</span>
                  <span className="text-xl font-bold text-gray-900">
                    ${subtotal.toFixed(2)}
                  </span>
                </div>

                <div className="space-y-2">
                  <Link
                    to="/cart"
                    onClick={() => setIsOpen(false)}
                    className="block w-full px-4 py-2 bg-blue-600 text-white text-center rounded-lg hover:bg-blue-700 transition-colors font-medium"
                  >
                    View Cart
                  </Link>
                  <button
                    onClick={() => setIsOpen(false)}
                    className="block w-full px-4 py-2 bg-gray-100 text-gray-700 text-center rounded-lg hover:bg-gray-200 transition-colors font-medium"
                  >
                    Continue Shopping
                  </button>
                </div>
              </div>
            </>
          )}
        </div>
      )}
    </div>
  )
}

export default MiniCart
