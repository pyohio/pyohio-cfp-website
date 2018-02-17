$(document).ready(function() {
    var urlPath = window.location.pathname;

    if(urlPath.match(/2018\/$/)) {
        handleHomeAlert();
    }

    if(urlPath.match(/login/)) {
        handleLoginErrors();
    }

    if(urlPath.match(/speaker\/.+/) ||
            urlPath.match(/proposals\/.+\/[submit|edit]/)) {
        handleCommonTalkDataForm();
    }

    if(urlPath.match(/proposals\/.+\/speakers/)) {
        handleAddlSpeakerForm();
    }

    if(urlPath.match(/account\/signup/) ||
            urlPath.match(/account\/password/)) {
        handleSignupErrors();
    }

    if(urlPath.match(/sponsors\/apply/) ||
            urlPath.match(/sponsors\/\d.+/)) {
        handleSponsorErrors();
    }

    if(urlPath.match(/reviews\/.+\/notification/)) {
        handleResultNotificationElements();
    }
});

function handleHomeAlert() {
    // Notification for confirmation email sent

    var banner = $('div.alert');
    if(banner) {
        banner.attr('role', 'alert');
    }
}

function handleResultNotificationElements() {
    var templateSelect = $('select[name="notification_template"]');
    var toggleAll = $('#action-toggle');
    var toggleOneList = $('input[type="checkbox"][name="_selected_action"]');

    templateSelect.attr('aria-label', 'notification email template');

    // FIXME: remove these when real hidden labels are added and column
    // scope is added to this table
    toggleAll.attr('aria-label', 'select all proposals');
    toggleOneList.attr('aria-label', 'select this proposal');
}

/*
 * In all of the following:
 * - Create link between any inputs and their help text via aria-describedby
 * - Locate any errors and apply role="alert"
 * - Create link between errors and their associated inputs
 */

function handleLoginErrors() {
    var globalError = $('div.alert');

    if(globalError) {
        globalError.attr('role', 'alert');
        globalError.attr('id', 'login-error');

        var passwordInput = $('input[type="password"]');
        passwordInput.attr('aria-invalid', 'true');
        passwordInput.attr('aria-describedby', 'login-error');

        // Use native focus
        document.querySelector('input[type="password"]').focus();
    }
}

function handleSignupErrors() {
    var globalError = $('div.alert');
    var formItems = $('div.form-group');

    // This form is complicated:
    // * Can have global error
    // * Can have inline error
    // * Global doesn't tie direct to input
    // User potentially has to error twice to hear both.
    if(globalError) {
        globalError.attr('role', 'alert');
    }

    if(formItems) {
        formItems.each(function(index) {
            if($(formItems[index]).hasClass('has-error')) {
                var errorMessage = $(formItems[index]).find('span.help-block');
                var errorInput = errorMessage.prev();

                errorInput.attr('aria-invalid', 'true');
                errorInput.attr('aria-describedby', errorInput.attr('id') + '-error');
                errorMessage.attr('id', errorInput.attr('id') + '-error');
                errorMessage.attr('role', 'alert');
            }
        });
    }

    if($('input[aria-invalid]').length) {
        // Use native focus
        // Won't work right until reconciled w/ pinax-theme-bootstrap
        document.querySelector('input[aria-invalid]').focus();
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

    if($('input[aria-invalid]').length) {
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

        // Use native focus
        document.querySelector('input[aria-invalid]').focus();
    }
}

function handleSponsorErrors() {
    // Like other forms, but has div wrappers for a two-column form
    // Also has a global sometimes
    var formItems = $('div.form-group');
    var globalError = $('div.alert');

    if(globalError) {
        globalError.attr('role', 'alert');
    }

    formItems.each(function(index) {
        if($(formItems[index]).hasClass('has-error')) {
            var errorMessage = $(formItems[index]).find('span.help-block');
            var errorInput = errorMessage.prev();

            errorInput.attr('aria-invalid', 'true');
            errorInput.attr('aria-describedby', errorInput.attr('id') + '-error');
            errorMessage.attr('id', errorInput.attr('id') + '-error');
            errorMessage.attr('role', 'alert');
        }
    });

    if($('input[aria-invalid]').length) {
        // Use native focus
        document.querySelector('input[aria-invalid]').focus();
    }
}
