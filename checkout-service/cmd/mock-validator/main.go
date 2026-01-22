package main

import (
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

type ValidateRequest struct {
	Value string `json:"value"`
}

type ValidateResponse struct {
	Field string `json:"field"`
	Valid bool   `json:"valid"`
}

func main() {
	gin.SetMode(gin.DebugMode)
	r := gin.Default()

	r.POST("/validate/:field", func(c *gin.Context) {
		time.Sleep(50 * time.Millisecond)

		field := c.Param("field")
		var req ValidateRequest

		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid request"})
			return
		}

		valid := len(req.Value) > 0

		c.JSON(http.StatusOK, ValidateResponse{
			Field: field,
			Valid: valid,
		})
	})

	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "healthy"})
	})

	log.Println("Mock Address Validator running on :5003")
	if err := r.Run(":5003"); err != nil {
		log.Fatal("Failed to start server:", err)
	}
}
