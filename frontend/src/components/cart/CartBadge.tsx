/**
 * Cart Badge Component
 * Shows the number of items in the cart
 */

import React from 'react'
import { useCart } from '@/hooks/useCart'

const CartBadge: React.FC = () => {
  const { getCartItemCount } = useCart()
  const itemCount = getCartItemCount()

  if (itemCount === 0) {
    return null
  }

  return (
    <span className="absolute -top-2 -right-2 bg-red-600 text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center">
      {itemCount > 9 ? '9+' : itemCount}
    </span>
  )
}

export default CartBadge
