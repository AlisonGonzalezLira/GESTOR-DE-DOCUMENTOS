function togglePassword() {
    const passwordInput = document.getElementById('password');
    const toggleBtn = document.querySelector('.password-toggle');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.textContent = '🙈';
    } else {
        passwordInput.type = 'password';
        toggleBtn.textContent = '👁';
    }
}

function forgotPassword() {
    alert('Redirigiendo a recuperación de contraseña...');
    // Aquí iría la lógica para recuperar contraseña
}

function register() {
    alert('Redirigiendo a registro...');
    // Aquí iría la lógica para registro
}

document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const user = document.getElementById('user').value;
    const password = document.getElementById('password').value;
    
    if (user && password) {
        alert('Iniciando sesión...');
        // Aquí iría la lógica de autenticación
    } else {
        alert('Por favor, completa todos los campos');
    }
});

// Validación en tiempo real para el campo de usuario
document.getElementById('user').addEventListener('input', function() {
    const user = this.value;
    
    if (user.length > 0 && user.length < 3) {
        this.style.borderColor = '#dc2626';
    } else {
        this.style.borderColor = '#ddd';
    }
});

// Animación suave al cargar la página
window.addEventListener('load', function() {
    const loginContainer = document.querySelector('.login-container');
    loginContainer.style.opacity = '0';
    loginContainer.style.transform = 'translateY(20px)';
    
    setTimeout(() => {
        loginContainer.style.transition = 'all 0.6s ease';
        loginContainer.style.opacity = '1';
        loginContainer.style.transform = 'translateY(0)';
    }, 200);
});