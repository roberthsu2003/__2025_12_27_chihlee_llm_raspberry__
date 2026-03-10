// TypeScript 原始碼
function add(a: number, b: number): number {
    return a + b;
}

function greet(name: string): void {
    console.log(`Hello, ${name}!`);
}

// 使用函數
const result = add(1, 2);
console.log(`1 + 2 = ${result}`);

greet('World');

// 在瀏覽器中顯示結果
if (typeof document !== 'undefined') {
    const app = document.querySelector('#app');
    if (app) {
        app.textContent = `計算結果：${result}`;
    }
}