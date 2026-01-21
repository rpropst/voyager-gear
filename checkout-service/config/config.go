package config

import (
	"log"
	"os"
)

type Config struct {
	SecretKey       string
	FastAPIBaseURL  string
	ValidatorAPIURL string
	Port            string
}

func Load() *Config {
	secretKey := os.Getenv("SECRET_KEY")
	if secretKey == "" {
		log.Fatal("SECRET_KEY environment variable is required")
	}

	fastAPIURL := os.Getenv("FASTAPI_BASE_URL")
	if fastAPIURL == "" {
		fastAPIURL = "http://localhost:5001"
	}

	validatorURL := os.Getenv("VALIDATOR_API_URL")
	if validatorURL == "" {
		validatorURL = "http://localhost:5003"
	}

	port := os.Getenv("PORT")
	if port == "" {
		port = "5002"
	}

	return &Config{
		SecretKey:       secretKey,
		FastAPIBaseURL:  fastAPIURL,
		ValidatorAPIURL: validatorURL,
		Port:            port,
	}
}
