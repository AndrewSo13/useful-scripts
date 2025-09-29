// Перетворює рядок у URL-сумісний слаг: "Hello Web3!" -> "hello-web3"
function slugify(str) {
  return String(str)
    .normalize('NFKD')            // прибирає діакритику
    .replace(/[^\w\s-]/g, '')     // прибирає символи
    .trim()
    .replace(/\s+/g, '-')         // пробіли -> дефіси
    .toLowerCase();
}

if (typeof module !== 'undefined') {
  module.exports = { slugify };
}

// Приклад:
// console.log(slugify("Привіт, Світ Web3!"));
