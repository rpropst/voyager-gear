/**
 * LocalStorage utilities for JWT token and guest cart management
 */

import type { GuestCartItem } from '@/types/cart.types'

const TOKEN_KEY = 'voyager_auth_token'
const CART_KEY = 'voyager_guest_cart'

/**
 * Get stored authentication token from localStorage
 */
export const getStoredToken = (): string | null => {
  try {
    return localStorage.getItem(TOKEN_KEY)
  } catch (error) {
    console.error('Error reading token from localStorage:', error)
    return null
  }
}

/**
 * Store authentication token in localStorage
 */
export const setStoredToken = (token: string): void => {
  try {
    localStorage.setItem(TOKEN_KEY, token)
  } catch (error) {
    console.error('Error storing token in localStorage:', error)
  }
}

/**
 * Remove authentication token from localStorage
 */
export const removeStoredToken = (): void => {
  try {
    localStorage.removeItem(TOKEN_KEY)
  } catch (error) {
    console.error('Error removing token from localStorage:', error)
  }
}

/**
 * Get guest cart from localStorage
 */
export const getStoredCart = (): GuestCartItem[] => {
  try {
    const cart = localStorage.getItem(CART_KEY)
    return cart ? JSON.parse(cart) : []
  } catch (error) {
    console.error('Error reading cart from localStorage:', error)
    return []
  }
}

/**
 * Store guest cart in localStorage
 */
export const setStoredCart = (cart: GuestCartItem[]): void => {
  try {
    localStorage.setItem(CART_KEY, JSON.stringify(cart))
  } catch (error) {
    console.error('Error storing cart in localStorage:', error)
  }
}

/**
 * Remove guest cart from localStorage
 */
export const removeStoredCart = (): void => {
  try {
    localStorage.removeItem(CART_KEY)
  } catch (error) {
    console.error('Error removing cart from localStorage:', error)
  }
}

/**
 * Add item to guest cart or increment quantity if exists
 */
export const addToGuestCart = (productId: number, quantity: number): void => {
  try {
    const cart = getStoredCart()
    const existingItem = cart.find((item) => item.product_id === productId)

    if (existingItem) {
      existingItem.quantity += quantity
    } else {
      cart.push({ product_id: productId, quantity })
    }

    setStoredCart(cart)
  } catch (error) {
    console.error('Error adding to guest cart:', error)
  }
}

/**
 * Update guest cart item quantity
 */
export const updateGuestCartItem = (productId: number, quantity: number): void => {
  try {
    const cart = getStoredCart()
    const item = cart.find((item) => item.product_id === productId)

    if (item) {
      item.quantity = quantity
      setStoredCart(cart)
    }
  } catch (error) {
    console.error('Error updating guest cart item:', error)
  }
}

/**
 * Remove item from guest cart
 */
export const removeFromGuestCart = (productId: number): void => {
  try {
    const cart = getStoredCart()
    const filteredCart = cart.filter((item) => item.product_id !== productId)
    setStoredCart(filteredCart)
  } catch (error) {
    console.error('Error removing from guest cart:', error)
  }
}
