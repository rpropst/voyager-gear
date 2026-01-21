import React from 'react'
import { useCheckout } from '@/contexts/CheckoutProvider'

export default function BillingInfoStep() {
  const { checkoutState, updateCheckoutState, goToNextStep, goToPreviousStep } =
    useCheckout()
  const {
    billingAddress,
    billingIsSameAsShipping,
    shippingAddress,
    isGift,
    giftMessage,
    giftWrap,
  } = checkoutState

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    goToNextStep()
  }

  const handleChange = (field: string, value: string) => {
    updateCheckoutState({
      billingAddress: {
        ...billingAddress,
        [field]: value,
      },
    })
  }

  return (
    <div className="billing-info-step">
      <h2 className="text-2xl font-bold mb-6">Billing Information</h2>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="mb-6">
          <label className="flex items-center">
            <input
              type="checkbox"
              checked={billingIsSameAsShipping}
              onChange={(e) =>
                updateCheckoutState({ billingIsSameAsShipping: e.target.checked })
              }
              className="mr-2"
            />
            <span className="text-sm font-medium">
              Billing address same as shipping
            </span>
          </label>
        </div>

        {!billingIsSameAsShipping && (
          <div className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium mb-1">
                  First Name *
                </label>
                <input
                  type="text"
                  required
                  value={billingAddress.firstName}
                  onChange={(e) => handleChange('firstName', e.target.value)}
                  className="w-full px-3 py-2 border rounded"
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">
                  Last Name *
                </label>
                <input
                  type="text"
                  required
                  value={billingAddress.lastName}
                  onChange={(e) => handleChange('lastName', e.target.value)}
                  className="w-full px-3 py-2 border rounded"
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium mb-1">
                Street Address *
              </label>
              <input
                type="text"
                required
                value={billingAddress.addressLine1}
                onChange={(e) => handleChange('addressLine1', e.target.value)}
                className="w-full px-3 py-2 border rounded"
              />
            </div>

            <div className="grid grid-cols-3 gap-4">
              <div>
                <label className="block text-sm font-medium mb-1">City *</label>
                <input
                  type="text"
                  required
                  value={billingAddress.city}
                  onChange={(e) => handleChange('city', e.target.value)}
                  className="w-full px-3 py-2 border rounded"
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">
                  State *
                </label>
                <input
                  type="text"
                  required
                  maxLength={2}
                  value={billingAddress.state}
                  onChange={(e) =>
                    handleChange('state', e.target.value.toUpperCase())
                  }
                  className="w-full px-3 py-2 border rounded"
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">
                  ZIP Code *
                </label>
                <input
                  type="text"
                  required
                  value={billingAddress.zipCode}
                  onChange={(e) => handleChange('zipCode', e.target.value)}
                  className="w-full px-3 py-2 border rounded"
                />
              </div>
            </div>
          </div>
        )}

        {isGift && (
          <div className="gift-options mt-8 p-6 bg-blue-50 border border-blue-200 rounded-lg">
            <h3 className="text-lg font-semibold mb-4">Gift Options</h3>
            <p className="text-sm text-gray-600 mb-4">
              This order is marked as a gift. Would you like to add gift wrapping
              or a personal message?
            </p>

            <div className="mb-4">
              <label className="flex items-center">
                <input
                  type="checkbox"
                  checked={giftWrap}
                  onChange={(e) =>
                    updateCheckoutState({ giftWrap: e.target.checked })
                  }
                  className="mr-2"
                />
                <span className="text-sm font-medium">
                  Add gift wrapping (+$5.00)
                </span>
              </label>
            </div>

            <div>
              <label className="block text-sm font-medium mb-2">
                Gift Message (optional)
              </label>
              <textarea
                rows={3}
                maxLength={200}
                placeholder="Write a personal message for the recipient..."
                value={giftMessage}
                onChange={(e) =>
                  updateCheckoutState({ giftMessage: e.target.value })
                }
                className="w-full px-3 py-2 border rounded"
              />
              <p className="text-xs text-gray-500 mt-1">
                {giftMessage.length}/200 characters
              </p>
            </div>
          </div>
        )}

        <div className="flex justify-between mt-6">
          <button
            type="button"
            onClick={goToPreviousStep}
            className="bg-gray-200 text-gray-800 py-3 px-6 rounded hover:bg-gray-300"
          >
            Back
          </button>
          <button
            type="submit"
            className="bg-blue-600 text-white py-3 px-6 rounded hover:bg-blue-700"
          >
            Continue to Payment
          </button>
        </div>
      </form>
    </div>
  )
}
