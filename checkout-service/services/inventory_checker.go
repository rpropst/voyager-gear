package services

import (
	"checkout-service/clients"
	"checkout-service/models"
	"fmt"
	"time"
)

type InventoryChecker struct {
	fapiClient *clients.FastAPIClient
}

func NewInventoryChecker(fapiClient *clients.FastAPIClient) *InventoryChecker {
	return &InventoryChecker{
		fapiClient: fapiClient,
	}
}

func (ic *InventoryChecker) ValidateStock(items []models.CartItem) error {
	for _, item := range items {
		product, err := ic.fapiClient.GetProduct(item.ProductID)
		if err != nil {
			return fmt.Errorf("failed to get product %d: %w", item.ProductID, err)
		}

		if product.Stock < item.Quantity {
			return fmt.Errorf(
				"insufficient stock for %s: requested %d, available %d",
				product.Name, item.Quantity, product.Stock,
			)
		}

		time.Sleep(20 * time.Millisecond)
	}

	return nil
}
