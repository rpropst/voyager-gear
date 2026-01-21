import { ApiClient } from './api'
import { Order } from '@/types/checkout.types'

class OrderService {
  private api: ApiClient

  constructor() {
    this.api = new ApiClient()
  }

  async getUserOrders(): Promise<Order[]> {
    return this.api.get<Order[]>('/orders')
  }

  async getOrder(orderId: number): Promise<Order> {
    return this.api.get<Order>(`/orders/${orderId}`)
  }
}

export const orderService = new OrderService()
