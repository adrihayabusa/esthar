const toggleSwitch = $('#themeButton');
const resume = $('#resume');
const htopContainer = $('.htop-container');
const amstradContainer = $('.amstrad-container');
const htmlContent = $('html');
const body = $('body');

let currentTheme = localStorage.getItem('theme') || 'light';
let currentTime = new Date();

if (currentTime.getHours() >= 20 || currentTime.getHours() <= 7) {
    currentTheme = 'dark';
}

htmlContent.attr('data-bs-theme', currentTheme);

if (currentTheme === 'dark') {
    toggleSwitch.textContent = ''; // Clear the sun icon
    body.addClass('dark-mode');
    $('#navbar').css('background-color', '#333333');
    $('#login').css('background-color', '#205950');
    $('#logout').css('background-color', '#46412e');
    $('#banner1').attr('src', staticBannerNight);
    $('#banner2').attr('src', staticBannerNight2);
    $('#prism-style').attr('href', staticUrlPrismDark);

    if (resume) {
        resume.css('background-color','#0b1b41');
    }
    if (htopContainer) {
        htopContainer.css({ backgroundColor: '#000', boxShadow: '0 0 0.8em #288 inset'});
    }
    if (amstradContainer) {
        amstradContainer.css({ backgroundColor: '#111111', boxShadow: '0 0 1em #00fd97 inset'});
        $('.amstrad-title').css({ backgroundColor: '#111111', color: '#00fd97', textShadow: '0 0 1em #00fd97'});
        $('.amstrad-header').css({ backgroundColor: '#00fd97', color: '#111111'});
        $('.amstrad-row').css({ backgroundColor: '#111111', color: '#00fd97'});
        $('.amstrad-row').hover(function () {
            $(this).css({ backgroundColor: '#00fd97', color: '#111111'});
        }, function () {
            $(this).css({ backgroundColor: '#111111', color: '#00fd97'});
        });
    }
} else {
    body.removeClass('dark-mode');
    htmlContent.attr('data-bs-theme', 'light');
    $('#navbar').css('background-color', '#eef6f5');
    $('#login').css('background-color', '#e0fffa');
    $('#logout').css('background-color', '#fff9e0');
    $('#banner1').attr('src', staticBanner);
    $('#banner2').attr('src', staticBanner2);
    $('#prism-style').attr('href', staticUrlPrism);

    if (resume) {
        resume.css('background-color','#eeeeee');
    }
    if (htopContainer) {
        htopContainer.css({ backgroundColor: '#eee', boxShadow: ''});
    }
    if (amstradContainer) {
        amstradContainer.css({ backgroundColor: '#eee', boxShadow: ''});
        $('.amstrad-title').css({ backgroundColor: '#eee', color: '#111111', textShadow: ''});
        $('.amstrad-header').css({ backgroundColor: '#111111', color: '#eee', border: ''});
        $('.amstrad-row').css({ backgroundColor: '#eee', color: '#111111'});
        $('.amstrad-row').hover(function () {
            $(this).css({ backgroundColor: '#111111', color: '#eee'});
        }, function () {
            $(this).css({ backgroundColor: '#eee', color: '#111111'});
        });
    }
}

toggleSwitch.click(function () {
    $(this).textContent = '';
    body.toggleClass('dark-mode');
    let theme = body.hasClass('dark-mode') ? 'dark' : 'light';
    htmlContent.attr('data-bs-theme', theme);
    localStorage.setItem('theme', theme);

    if (theme === 'dark') {
        $('#navbar').css('background-color', '#333333');
        $('#login').css('background-color', '#205950');
        $('#logout').css('background-color', '#46412e');
        $('#banner1').attr('src', staticBannerNight);
        $('#banner2').attr('src', staticBannerNight2);
        $('#prism-style').attr('href', staticUrlPrismDark);

        if (resume) {
            resume.css('background-color', '#0b1b41');
        }
        if (htopContainer) {
            htopContainer.css({ backgroundColor: '#000', boxShadow: '0 0 0.8em #288 inset'});
        }
        if (amstradContainer) {
            amstradContainer.css({ backgroundColor: '#111111', boxShadow: '0 0 1em #00fd97 inset'});
            $('.amstrad-title').css({ backgroundColor: '#111111', color: '#00fd97', textShadow: '0 0 1em #00fd97'});
            $('.amstrad-header').css({ backgroundColor: '#00fd97', color: '#111111'});
            $('.amstrad-row').css({ backgroundColor: '#111111', color: '#00fd97'});
            $('.amstrad-row').hover(function () {
                $(this).css({ backgroundColor: '#00fd97', color: '#111111'});
            }, function () {
                $(this).css({ backgroundColor: '#111111', color: '#00fd97'});
            });
        }
    } else {
        $('#navbar').css('background-color', '#eef6f5');
        $('#login').css('background-color', '#e0fffa');
        $('#logout').css('background-color', '#fff9e0');
        $('#banner1').attr('src', staticBanner);
        $('#banner2').attr('src', staticBanner2);
        $('#prism-style').attr('href', staticUrlPrism);

        if (resume) {
            resume.css('background-color', '#eeeeee');
        }
        if (htopContainer) {
            htopContainer.css({ backgroundColor: '#eee', boxShadow: ''});
        }
        if (amstradContainer) {
            amstradContainer.css({ backgroundColor: '#eee', boxShadow: '', border: ''});
            $('.amstrad-title').css({ backgroundColor: '#eee', color: '#111111', textShadow: ''});
            $('.amstrad-header').css({ backgroundColor: '#111111', color: '#eee'});
            $('.amstrad-row').css({ backgroundColor: '#eee', color: '#111111'});
            $('.amstrad-row').hover(function () {
                $(this).css({ backgroundColor: '#111111', color: '#eee'});
            }, function () {
                $(this).css({ backgroundColor: '#eee', color: '#111111'});
            });
        }
    }
});