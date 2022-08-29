// Armazena um item pegando chave e o valor do input
function adicionar() {
    localStorage.setItem(txtChave.value, txtValor.value)
}
function remover() {
    localStorage.removeItem(txtChave.value)
    alert('Item removido.')
}

// limpa todos os itens do localStorage
function limpar() {
    localStorage.clear()
    alert('')
}

function addToCart(id) {
    
    console.log(id)
    var qtd = parseInt(document.getElementsByName('qtd')[0].value);
    var carts = [];
    if (localStorage.length > 0) {
        carts = JSON.parse(localStorage.getItem('carts'));
        var filtro = carts.filter(function(obj) { return obj.id == id; });
        if (filtro.length == 0) {
            carts.push({
                id: id,
                qtd: qtd
            });
        } 
        else if (filtro[0].qtd < qtd) {
            carts.forEach(element => {
                if (element.id == id) {
                    element.qtd = qtd;
                }
            });
        }
    } else {
        carts = [{ id: id, qtd: qtd }];
    };
    localStorage.setItem('carts', JSON.stringify(carts));
    href = '/carrinho?carts=' + JSON.stringify(carts);
    var link = document.querySelector('#cart');
    link.setAttribute('href', href);
    alert('Produto adicionado ao carrinho.');
}