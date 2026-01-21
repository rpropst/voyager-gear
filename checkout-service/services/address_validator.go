package services

import (
	"bytes"
	"checkout-service/models"
	"encoding/json"
	"fmt"
	"net/http"
)

type AddressValidator struct {
	validatorURL string
	client       *http.Client
}

func NewAddressValidator(validatorURL string) *AddressValidator {
	return &AddressValidator{
		validatorURL: validatorURL,
		client:       &http.Client{},
	}
}

func (av *AddressValidator) Validate(addr models.Address) error {
	fields := []struct {
		name  string
		value string
	}{
		{"street", addr.AddressLine1},
		{"city", addr.City},
		{"state", addr.State},
		{"zip", addr.ZipCode},
		{"country", addr.Country},
	}

	for _, field := range fields {
		if err := av.validateField(field.name, field.value); err != nil {
			return err
		}
	}

	return nil
}

func (av *AddressValidator) validateField(fieldName, value string) error {
	url := fmt.Sprintf("%s/validate/%s", av.validatorURL, fieldName)

	payload := map[string]string{"value": value}
	jsonData, err := json.Marshal(payload)
	if err != nil {
		return fmt.Errorf("failed to marshal payload: %w", err)
	}

	resp, err := av.client.Post(url, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		return fmt.Errorf("failed to validate %s: %w", fieldName, err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("validation failed for %s", fieldName)
	}

	var result struct {
		Field string `json:"field"`
		Valid bool   `json:"valid"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return fmt.Errorf("failed to decode validation response: %w", err)
	}

	if !result.Valid {
		return fmt.Errorf("%s is invalid", fieldName)
	}

	return nil
}
