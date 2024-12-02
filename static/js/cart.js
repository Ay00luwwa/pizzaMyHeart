
<script>
    document.addEventListener('DOMContentLoaded', function () {
        const quantityInputs = document.querySelectorAll('.quantity-input');
        
        quantityInputs.forEach(input => {
            input.addEventListener('input', function () {
                const price = parseFloat(this.dataset.price);
                const quantity = parseInt(this.value) || 1;  // Fallback to 1 if empty or invalid
                const totalCell = this.closest('tr').querySelector('.total');
                const newTotal = (price * quantity).toFixed(2);
                totalCell.textContent = `$${newTotal}`;
                
                // Update the subtotal
                updateSubtotal();
            });
        });

        function updateSubtotal() {
            let subtotal = 0;
            document.querySelectorAll('.total').forEach(cell => {
                subtotal += parseFloat(cell.textContent.replace('$', ''));
            });
            document.querySelector('#subtotal-value').textContent = `$${subtotal.toFixed(2)}`;
            updateGrandTotal(subtotal);
        }

        function updateGrandTotal(subtotal) {
            const deliveryFee = 5.00; // Static delivery fee
            const grandTotal = subtotal + deliveryFee;
            document.querySelector('#total-price-value').textContent = `$${grandTotal.toFixed(2)}`;
        }
    });
</script>
