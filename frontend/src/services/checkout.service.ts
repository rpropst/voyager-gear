import { ApiClient } from './api'
import { CheckoutData, CheckoutResponse } from '@/types/checkout.types'

const CHECKOUT_URL = import.meta.env.VITE_CHECKOUT_URL || 'http://localhost:5002'

class CheckoutService {
  async processCheckout(data: CheckoutData): Promise<CheckoutResponse> {
    const response = await fetch(`${CHECKOUT_URL}/api/checkout/process`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${ApiClient.getToken()}`,
      },
      body: JSON.stringify(data),
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.error || 'Checkout failed')
    }

    return response.json()
  }
}

export const checkoutService = new CheckoutService()
