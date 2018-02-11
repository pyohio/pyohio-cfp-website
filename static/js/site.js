$(document).ready(function() {
    var urlPath = window.location.pathname;

    if(urlPath.match('login')) {
        handleLoginErrors();
    }

    if(urlPath.match(/speaker\/.+/) ||
            urlPath.match(/proposals\/.+\/[submit|edit]/)) {
        handleCommonTalkDataForm();
    }

    if(urlPath.match(/proposals\/.+\/speakers/)) {
        handleAddlSpeakerForm();
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

function handleCommonTalkDataForm() {
    var formItems = $('div.form-group');
    formItems.each(function(index) {
        var helpText = $(formItems[index]).find('p.help-block');
        if($(formItems[index]).hasClass('has-error')) {
            // Errors may have multiple "help" blocks

            var errorMessage = helpText.prev();
            var errorInput = errorMessage.prev();
            var errorID = errorInput.attr('id') + '-error';
            var helpID = errorInput.attr('id') + '-help';

            errorInput.attr('aria-invalid', 'true');
            errorInput.attr('aria-describedby', errorID + ' ' + helpID);
            helpText.attr('id', helpID);
            errorMessage.attr('id', errorID);
            errorMessage.attr('role', 'alert');
        }
        else {
            // Handle help text

            if(helpText) {
                var prev = helpText.prev();

                // Set up describedby relationship
                helpText.attr('id', prev.attr('id') + '-help');
                prev.attr('aria-describedby', helpText.attr('id'));
            }
        }
    });

    if($('input[aria-invalid]')) {
        // Use native focus
        document.querySelector('input[aria-invalid]').focus();
    }
}

function handleAddlSpeakerForm() {
    // Extremely similar to the login form.

    var errorItem = $('div.has-error');
    if(errorItem) {
        var errorMessage = errorItem.find('span.help-block');
        var errorInput = errorMessage.prev();

        errorInput.attr('aria-invalid', 'true');
        errorInput.attr('aria-describedby', errorInput.attr('id') + '-error');
        errorMessage.attr('id', errorInput.attr('id') + '-error');
        errorMessage.attr('role', 'alert');

        document.querySelector('input[aria-invalid]').focus();
    }
}
