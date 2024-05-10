/* atv 1 */
function imprimir_nome() {
    console.log("relou uorde   ! ");
}

imprimir_nome()


/* atv 2 */

function idade(num){ 

console.log("idada de de coisinha é", num);
}

idade(4)


/* atv 3 */

function soma(a,b){
    console.log( "resultado é ", a + b);
}

soma( 1, 2)

/* atv 4 */

function num_aleatorio(nume){
    console.log(Math.random() * nume);
}

num_aleatorio(10);

/* atv 5 */

function auto_escola(idade){

    if (idade>=18){
        console.log("pode dirigir");
    }
    else{
        console.log("nao pode dirigir");
    }
}

auto_escola(19)
auto_escola(10)

/* atv 6 */

function tipo(palavra){
    console.log("o tipo dados dessa palavra é ",typeof palavra);
}

tipo(1)
tipo("palavraa")
tipo(true)

/* atv 7 */

function positivo(number){
    console.log(Math.abs(number));
}

positivo(-5)
positivo(6)


/* atv 8 */

function caractereres(texto) {
    if (texto.length > 10) {
        console.log("Texto muito longo");
    } else {
        console.log("Texto dentro do limite");
    }
}

caractereres("aaaaa"); 
caractereres("bbbbbbbbbbbbbbbbbbbbbbbbbb");

/* atv 9*/

function potencia(x,y){
    const z=x
    for (y; y>1; y=y-1){
        x=x*z
    }
    console.log("o resultado é", x);
}

potencia(3,4)

/* atv 10*/

function decrementa(numero){
    for (numero; numero>0; numero=numero-1){
        if (numero%2==0){
            console.log("numero", numero, "é par");
        }
    }
}
decrementa(10)