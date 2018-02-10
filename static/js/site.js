$(document).ready(function() {
    var urlPath = window.location.pathname;

    if(urlPath.match('login')) {
        handleLoginErrors();
    }
});

function handleLoginErrors() {
    var globalError = $('div.alert');

    if(globalError) {
        // Apply:
        // role="alert"
        // id for reference
        globalError.attr('role', 'alert');
        globalError.attr('id', 'login-error');

        var passwordInput = $('input[type="password"]');
        passwordInput.attr('aria-invalid', 'true');
        passwordInput.attr('aria-describedby', 'login-error');

        // Use native focus
        document.querySelector('input[type="password"]').focus();
    }
}
