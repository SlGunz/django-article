window.addEventListener('DOMContentLoaded', function () {
    const HIDE_HEAD_ON = 200,
        SHOW_HEAD_ON = 200;
    var topPanel = new Panel('topToolbar'),
        bottomPanel = new Panel('bottomToolbar');
    var didScroll = false,
        didMouseMove = false;

    function onCreate() {
        if (typeof bottomPanel.showAndLock === 'function'){
            bottomPanel.showAndLock();
        }      
        onScrollPage();

        window.addEventListener('scroll', function (event) {
            if (!didScroll) {
                didScroll = true;
                setTimeout(onScrollPage, 250);
            }
        }, false);

        window.addEventListener('mousemove', function (event) {
            if (!didMouseMove) {
                didMouseMove = true;
                //get mouse position on document crossbrowser
                if (!event) { event = window.event; }
                setTimeout(function () { onMousemove(event.clientX, event.clientY) }, 200);
            }
        }, false);

    }

    function onScrollPage() {
        var sy = scrollY();
        if (sy >= HIDE_HEAD_ON) {
            topPanel.hideAndUnlock();
        }
        else {
            topPanel.showAndLock();
        }
        didScroll = false;
    }

    function onMousemove(x, y) {
        if (y < topPanel.verticalBorder() + SHOW_HEAD_ON) {
            topPanel.show();
        } else {
            topPanel.hide();
        }

        didMouseMove = false;
    }

    function scrollY() {
        return window.pageYOffset || document.documentElement.scrollTop;
    }

    onCreate();
})