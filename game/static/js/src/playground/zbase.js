class AcGamePlayground {
    constructor(root) {
        this.root = root;
        this.$playground = $(`<div>游戏界面</div>`);
        this.hide();
        this.root.$ac_game.append(this.$playground);

        this.start();
    }

    start() {
    }

    //update() {
    //}

    show() { //打开plauground界面
        this.$playground.show();
    }

    hide() { //关闭playground界面
        this.$playground.hide();
    }
}
