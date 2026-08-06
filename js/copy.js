// Adiciona a funcionalidade de "copiar" a todos os botões com a classe .copy-btn
document.querySelectorAll(".copy-btn").forEach((button) => {
    button.addEventListener("click", () => {
        const targetId = button.getAttribute("data-target");
        const codeEl = document.getElementById(targetId);
        if (!codeEl) return;

        navigator.clipboard.writeText(codeEl.innerText).then(() => {
            const originalText = button.textContent;
            button.textContent = "Copiado!";
            button.classList.add("copied");

            setTimeout(() => {
                button.textContent = originalText;
                button.classList.remove("copied");
            }, 2000);
        }).catch((err) => {
            console.error("Não foi possível copiar o código:", err);
        });
    });
});
