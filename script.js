// tipos primitivos 
// boolean
 var boolean = false;

 var prof; 
 console.log("Texto "+ boolean + "texto ");
 // template string
console .log(`A variável ${boolean} tem o tipo ${typeof(boolean)}`);

var numero = 1;
console .log(`A variável ${numero} tem o tipo ${typeof(numero)}`)
 
// var; // variavel global ou local - valor incial pode ser nulo
// let; // variavel local de bloco - valor inicial pode ser nulo
// const; // variavel local de bloco - valor inicial é obrigatório

// var prof = 'Lucas';
// var prof = 'Lucas sousa';
 
// left Sobrenome ='Sousa';

// Sobrenome = ' Borges de Sousa';

// const profissão = 'prfessor';

// profissão = 'programador';

// const profissão = 'testador';
var nome = 'Lucas';

// Usando variavel local
function nomeDafuncao(){
     var Sobrenome = 'Sousa';
     console.log(Sobrenome)
}

console.log(nome);
nomeDafuncao();

// operadores de comparação
var comparação = '0' == 0;
console.log(comparação);

var comparaçãoIdentica ='0' === 0;
console.log(comparaçãoIdentica);

var mult = 5 * 9;
console.log(mult);

var divisao = 15 / 3;
console.log(divisao);

// operadores relacionais
// >, <, >=, <=, !=
// maior ou igual
var maiorOuigual = 5 >= 16;
console.log(maiorOuigual);

var diferente = 5 != 8;
console.log(diferente);