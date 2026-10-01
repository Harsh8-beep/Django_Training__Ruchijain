document.addEventListener("DOMContentLoaded", function () {
    /* =====================================================
       STUDENTHUB UI INTERACTIONS
       Existing functionality preserved.
       ===================================================== */

    /* MOBILE MENU */
    const menuBtn = document.getElementById("menuBtn");
    const navLinks = document.querySelector(".nav-links");

    if (menuBtn && navLinks) {
        menuBtn.setAttribute("aria-expanded", "false");

        menuBtn.addEventListener("click", function () {
            const open = navLinks.classList.toggle("show");
            menuBtn.setAttribute("aria-expanded", String(open));
        });

        navLinks.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                navLinks.classList.remove("show");
                menuBtn.setAttribute("aria-expanded", "false");
            });
        });
    }

    /* PASSWORD SHOW / HIDE */
    document.querySelectorAll(".password-toggle").forEach(function (button) {
        button.addEventListener("click", function () {
            const targetId = button.getAttribute("data-target");
            const input = document.getElementById(targetId);

            if (!input) return;

            const visible = input.type === "password";
            input.type = visible ? "text" : "password";
            button.textContent = visible ? "🙈" : "👁";
            button.setAttribute("aria-label", visible ? "Hide password" : "Show password");
        });
    });

    /* PASSWORD STRENGTH */
    const signupPassword = document.getElementById("signup_password");
    const strengthBars = document.querySelectorAll(".strength-bars span");

    if (signupPassword && strengthBars.length) {
        signupPassword.addEventListener("input", function () {
            const password = signupPassword.value;
            let strength = 0;

            if (password.length >= 8) strength++;
            if (/[A-Z]/.test(password)) strength++;
            if (/[0-9]/.test(password)) strength++;
            if (/[^A-Za-z0-9]/.test(password)) strength++;

            strengthBars.forEach(function (bar, index) {
                bar.style.background = index < strength
                    ? "var(--primary)"
                    : "#e5e7eb";
            });
        });
    }

    /* PHONE NUMBER */
    const phoneInput = document.querySelector('input[name="phone"]');
    if (phoneInput) {
        phoneInput.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, "").slice(0, 10);
        });
    }

    /* PIN CODE */
    const pinInput = document.querySelector('input[name="pincode"]');
    if (pinInput) {
        pinInput.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, "").slice(0, 6);
        });
    }

    /* REGISTRATION FORM PROGRESS */
    const registrationForm = document.querySelector(".registration-card form");

    if (registrationForm) {
        const inputs = registrationForm.querySelectorAll(
            "input:not([type='checkbox']), select, textarea"
        );
        const progressBar = document.querySelector(".completion-card .progress-bar");
        const progressText = document.querySelector(".completion-card strong");

        function updateProgress() {
            let filled = 0;
            let total = 0;

            inputs.forEach(function (input) {
                if (input.type === "hidden" || input.type === "submit") return;

                total++;

                if (String(input.value || "").trim() !== "") {
                    filled++;
                }
            });

            if (!total) return;

            const percentage = Math.round((filled / total) * 100);

            if (progressBar) progressBar.style.width = percentage + "%";
            if (progressText) progressText.textContent = percentage + "%";
        }

        inputs.forEach(function (input) {
            input.addEventListener("input", updateProgress);
            input.addEventListener("change", updateProgress);
        });

        updateProgress();
    }

    /* SOFT REVEAL — visual only */
    const cards = document.querySelectorAll(".feature-card, .registration-card");

    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("ui-visible");
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.08 });

        cards.forEach(function (card) {
            card.classList.add("ui-reveal");
            observer.observe(card);
        });
    }
});
