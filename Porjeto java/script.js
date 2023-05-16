const dino = document.getElementById("dino");
const cactus = document.getElementById("cactus");
let alreadyJump = false;


let isAlive = setInterval(() => {
    let randomTime = Math.random() * 6000; //criar cactus de maneira aleatória

    // dino posição
    let dinoTop = parseInt(window.getComputedStyle(dino).getPropertyValue("top"));

    // cactus posição
    let cactusLeft = parseInt(window.getComputedStyle(cactus).getPropertyValue("left"));

    // analisar se ambos se tocam
    if (cactusLeft < 50 && cactusLeft > 0 && dinoTop >= 140) {
        alert("GAME-OVER");
        document.body.innerHTML = '<h1 class="game-over""> Atualize a página e jogue novamente (F5)! </h1>';
    // criando título ao final do jogo
    }

    setTimeout(isAlive, randomTime);
}, 10);

document.addEventListener("keydown", (e) => {
    if ((e.code === "ArrowUp") | (e.code === "Space")) {
        jump();
    }
});

function jump() {
    if (!dino.classList.contains("jump")) {
        dino.classList.add("jump");
        alreadyJump = true;

        setTimeout(() => {
            dino.classList.remove("jump");
            alreadyJump = false;
        }, 300);
    }
}