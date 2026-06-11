function actualizar(id, accion, precio) {
    fetch(`/carrito/actualizar/${id}/${accion}/`)
        .then(res => res.json())
        .then(data => {
            if (data.eliminado) {
                document.getElementById(`fila-${id}`).remove();
            } else {
                document.getElementById(`cantidad-${id}`).innerText = data.cantidad;
                document.getElementById(`total-${id}`).innerText = `Precio Total: $ ${(data.cantidad * precio).toFixed(2)}`;
            }
        });
}