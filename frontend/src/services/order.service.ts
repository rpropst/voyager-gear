import { apiClient } from './api'
import { Order } from '@/types/checkout.types'

class OrderService {
  async getUserOrders(): Promise<Order[]> {
    return apiClient.get<Order[]>('/api/orders', { requiresAuth: true })
  }

  async getOrder(orderId: number): Promise<Order> {
    return apiClient.get<Order>(`/api/orders/${orderId}`, { requiresAuth: true })
  }
}

export const orderService = new OrderService()
