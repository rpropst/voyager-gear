/**
 * Custom hook to access Cart context
 */

import { useContext } from 'react'
import { CartContext } from '@/contexts/CartProvider'
import type { CartContextType } from '@/types/cart.types'

/**
 * Hook to access cart context
 * Must be used within CartProvider
 */
export const useCart = (): CartContextType => {
  const context = useContext(CartContext)

  if (context === undefined) {
    throw new Error('useCart must be used within a CartProvider')
  }

  return context
}
