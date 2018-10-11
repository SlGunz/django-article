/**
 * Panel class that allow show and hide object, by adding 'hidden' CSS class attribute value
 */
function Panel(panelId) {
    const CLASS_NAME_HIDE = 'hidden'
    var panel = document.getElementById(panelId);

    if (panel == null){
        return null;
    }
    
    var isLocked = false;
    var isHidden = function () {                    
        if (!isLocked && panel.classList.contains(CLASS_NAME_HIDE)) {
            return true;
        }
        return isLocked;
    }
    this.hide = function () {
        if (isHidden()) {
            return;
        }
        panel.classList.add(CLASS_NAME_HIDE);
    }
    this.show = function () {
        if (!isHidden()) {
            return;
        }
        panel.classList.remove(CLASS_NAME_HIDE);
    }
    this.showAndLock = function() {
        this.show();
        isLocked = true;
    }
    this.hideAndUnlock = function(){
        isLocked = false;
        this.hide();
    }
    this.verticalBorder = function () {
        if (panel.offsetTop > panel.offsetHeight) {
            return panel.offsetTop;
        }
        return panel.offsetTop + panel.offsetHeight;
    }
}