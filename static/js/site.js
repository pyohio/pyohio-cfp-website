$(document).ready(function() {
    var urlPath = window.location.pathname;

    if(urlPath.match('login')) {
        handleLoginErrors();
    }

    if(urlPath.match('speaker')) {
        handleSpeakerProfileForm();
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

function handleSpeakerProfileForm() {
    // First, handle help text
    var formItems = $('div.form-group');
    formItems.each(function(index) {
        var helpText = $(formItems[index]).find('p.help-block');
        if(helpText) {
            var prev = helpText.prev();

            // Set up describedby relationship
            helpText.attr('id', prev.attr('id') + '-help');
            prev.attr('aria-describedby', helpText.attr('id'));
        }
    });
}
