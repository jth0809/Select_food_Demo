const _awaitUnlock = async (mutex) => {
    // 잠금 상태가 아님 -> 즉시 resolve
    if (!mutex._locked) {
        return Promise.resolve()
    }
    return new Promise((resolve) => {
        // 0.1초 후에 다시 확인
        setTimeout(() => {
        _awaitUnlock(mutex).then(() => resolve())
        }, 100)
    })
}
  
class Mutex {
    constructor() {
        this._locked = false;
    }

    async lock() {
        // 잠금 상태가 풀릴 때 까지 대기
        this._locked = true;
        await _awaitUnlock(this);
        this.release();
    }

    // 잠금 해제는 별도의 제약을 주지 않음.
    release() {
        this._locked = false;
    }
}

const mutex = new Mutex();
let PickedOption = 0;

function shuffle(array) {
    return array.sort(() => Math.random() - 0.5);
}

function getPrepMenus(length) {
    let ReturnArr = shuffle(JSON.parse(localStorage.getItem("Menus"))).slice(0, length);
    return shuffle(ReturnArr);
}

async function showPick(Menu1, Menu2) {
    document.getElementById("Option_1").style.backgroundImage = "url(\'" + Menu1["Img"] + "\')";
    document.getElementById("Option_2").style.backgroundImage = "url(\'" + Menu2["Img"] + "\')";

    document.getElementById("Option_1").innerHTML = "<h1>" + Menu1["MenuName"] + "</h1>";
    document.getElementById("Option_2").innerHTML = "<h1>" + Menu2["MenuName"] + "</h1>";

    await mutex.lock();

    if (PickedOption == 1) {
        PickedOption = 0;
        return Menu1;
    }
    else {
        PickedOption = 0;
        return Menu2;
    }
}

function pickOption1() {
    PickedOption = 1;
    mutex.release();
}

function pickOption2() {
    PickedOption = 2;
    mutex.release();
}

async function startPick(Menus, start, end) {
    if (start == end) {
        return Menus[start];
    }

    let mid = Math.floor((start + end) / 2);
    return showPick(await startPick(Menus, start, mid), await startPick(Menus, mid + 1, end));
}

function main(event) {
    const Menus = getPrepMenus(8);
    console.log(Menus);

    startPick(Menus, 0, 7)
    .then((result) => {
        document.getElementById("container").innerHTML = "<h1>" + result["MenuName"] + "</h1>";
        document.getElementById("container").style.backgroundImage = "url(\'" + result["Img"] + "\')";
        document.getElementById("container").style.backgroundSize = "contain";
        console.log(result);
    });
}

window.addEventListener("DOMContentLoaded", main);

document.getElementById("Option_1").addEventListener("click", pickOption1);
document.getElementById("Option_2").addEventListener("click", pickOption2);