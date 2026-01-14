/**
 * Cart service for API calls
 */

import type {
  Cart,
  AddToCartRequest,
  UpdateCartItemRequest,
  GuestCartMergeRequest,
  PromoCode,
  ShippingTaxInfo,
  ValidatePromoCodeRequest,
  CalculateShippingTaxRequest,
} from '@/types/cart.types'
import { apiClient } from './api'

export const cartService = {
  /**
   * Get user's cart with all items
   * Requires authentication
   */
  async getCart(): Promise<Cart> {
    return apiClient.get<Cart>('/api/cart', { requiresAuth: true })
  },

  /**
   * Add item to cart or increment quantity if exists
   * Requires authentication
   */
  async addToCart(productId: number, quantity: number): Promise<Cart> {
    const data: AddToCartRequest = { product_id: productId, quantity }
    return apiClient.post<Cart>('/api/cart/items', data, { requiresAuth: true })
  },

  /**
   * Update cart item quantity
   * Requires authentication
   */
  async updateCartItem(itemId: number, quantity: number): Promise<Cart> {
    const data: UpdateCartItemRequest = { quantity }
    return apiClient.put<Cart>(`/api/cart/items/${itemId}`, data, { requiresAuth: true })
  },

  /**
   * Remove item from cart
   * Requires authentication
   */
  async removeCartItem(itemId: number): Promise<Cart> {
    return apiClient.delete<Cart>(`/api/cart/items/${itemId}`, { requiresAuth: true })
  },

  /**
   * Merge guest cart with user cart on login
   * Requires authentication
   */
  async mergeGuestCart(items: GuestCartMergeRequest['items']): Promise<Cart> {
    const data: GuestCartMergeRequest = { items }
    return apiClient.post<Cart>('/api/cart/merge', data, { requiresAuth: true })
  },

  /**
   * Clear entire cart
   * Requires authentication
   */
  async clearCart(): Promise<void> {
    return apiClient.post<void>('/api/cart/clear', undefined, { requiresAuth: true })
  },

  /**
   * Move cart item to saved for later
   * Requires authentication
   */
  async saveForLater(itemId: number): Promise<Cart> {
    return apiClient.post<Cart>(`/api/cart/items/${itemId}/save`, undefined, { requiresAuth: true })
  },

  /**
   * Restore saved item back to cart
   * Requires authentication
   */
  async restoreSavedItem(savedId: number): Promise<Cart> {
    return apiClient.post<Cart>(`/api/cart/saved/${savedId}/restore`, undefined, { requiresAuth: true })
  },

  /**
   * Delete a saved item
   * Requires authentication
   */
  async removeSavedItem(savedId: number): Promise<Cart> {
    return apiClient.delete<Cart>(`/api/cart/saved/${savedId}`, { requiresAuth: true })
  },

  /**
   * Validate a promo code
   * No authentication required
   */
  async validatePromoCode(code: string): Promise<PromoCode> {
    const data: ValidatePromoCodeRequest = { code }
    return apiClient.post<PromoCode>('/api/promo-codes/validate', data)
  },

  /**
   * Calculate shipping and tax based on ZIP code and subtotal
   * No authentication required
   */
  async calculateShippingTax(zipCode: string, subtotal: number): Promise<ShippingTaxInfo> {
    const data: CalculateShippingTaxRequest = { zip_code: zipCode, subtotal }
    return apiClient.post<ShippingTaxInfo>('/api/shipping/calculate', data)
  },
}
