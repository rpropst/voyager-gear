/**
 * Cart types for shopping cart functionality
 */

import { Product } from './product.types'

export interface CartItem {
  id: number
  cart_id: number
  product_id: number
  quantity: number
  product: Product
  created_at: string
  updated_at: string
}

export interface SavedItem {
  id: number
  cart_id: number
  product_id: number
  quantity: number
  product: Product
  created_at: string
}

export interface Cart {
  id: number
  user_id: number
  items: CartItem[]
  saved_items: SavedItem[]
  created_at: string
  updated_at: string
}

export interface GuestCartItem {
  product_id: number
  quantity: number
  product?: Product
}

export interface PromoCode {
  code: string
  discount_percentage: number
  is_valid: boolean
  message?: string
}

export interface ShippingTaxInfo {
  zip_code: string
  state: string
  tax_rate: number
  shipping_cost: number
  subtotal: number
  tax_amount: number
  shipping_amount: number
  total: number
}

export interface CartState {
  cart: Cart | null
  guestCart: GuestCartItem[]
  isLoading: boolean
  error: string | null
  promoCode: PromoCode | null
  shippingTax: ShippingTaxInfo | null
}

export interface CartContextType {
  // State
  cart: Cart | null
  guestCart: GuestCartItem[]
  isLoading: boolean
  error: string | null
  promoCode: PromoCode | null
  shippingTax: ShippingTaxInfo | null

  // Cart operations
  addToCart: (productId: number, quantity: number) => Promise<void>
  updateCartItem: (itemId: number, quantity: number) => Promise<void>
  removeCartItem: (itemId: number) => Promise<void>
  clearCart: () => Promise<void>
  refreshCart: () => Promise<void>

  // Saved items operations
  saveForLater: (itemId: number) => Promise<void>
  restoreSavedItem: (savedId: number) => Promise<void>
  removeSavedItem: (savedId: number) => Promise<void>

  // Promo code operations
  applyPromoCode: (code: string) => Promise<void>
  removePromoCode: () => void

  // Shipping & tax operations
  calculateShippingTax: (zipCode: string) => Promise<void>

  // Utility functions
  getCartItemCount: () => number
  getSubtotal: () => number
}

// API request/response types
export interface AddToCartRequest {
  product_id: number
  quantity: number
}

export interface UpdateCartItemRequest {
  quantity: number
}

export interface GuestCartMergeRequest {
  items: GuestCartItem[]
}

export interface ValidatePromoCodeRequest {
  code: string
}

export interface CalculateShippingTaxRequest {
  zip_code: string
  subtotal: number
}
