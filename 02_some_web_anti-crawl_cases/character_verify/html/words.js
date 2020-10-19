var fontSize = 18; //font size
var fonts = fontSize + 'px Arial';


function randNumber(min, max) {
    // get random number
    var res = parseInt(Math.random() * (max - min) + min);
    return res;
}

function randColor(min, max) {
    // get random color
    var r = randNumber(min, max);
    var g = randNumber(min, max);
    var b = randNumber(min, max);
    var colorRes = `rgb(${r}, ${b}, ${b})`;
    return colorRes;
}

var strs = [];  // Canvas verify char
var fontSize = randNumber(28, 40); // font size
var fonts = fontSize + 'px Arial';


function cvasInterfere(cvas, width, height) {
    // line
    for (var i = 0; i < 3; i++) {
        cvas.beginPath();
        cvas.moveTo(randNumber(0, width), randNumber(0, height));
        cvas.lineTo(randNumber(0, width), randNumber(0, height));
        cvas.strokeStyle = randColor(180, 260);
        cvas.closePath();
        cvas.stroke();
    }
    // dot
    for (var i = 0; i < 80; i++) {
        cvas.beginPath();
        cvas.arc(randNumber(0, width), randNumber(0, height), 1, 0, 2 * Math.PI);
        cvas.closePath();
        cvas.fillStyle = randColor(150, 260);
        cvas.fill();
    }
}

$(function () {
    var wordsCanvas = document.getElementById('wordsCanvas');
    var cvas = wordsCanvas.getContext('2d');
    var letter = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890";
    var width = wordsCanvas.width; var height = wordsCanvas.height;
    // bg color
    cvas.fillStyle = randColor(120, 230);
    cvas.fillRect(0, 0, width, height);
    for (var i = 0; i < 6; i++) {
        // get random character from letter
        var single = letter[randNumber(0, letter.length)];
        cvas.font = fonts;
        cvas.textBaseline = 'top';
        cvas.fillStyle = randColor(80, 180);
        cvas.save();
        cvas.translate(30 * i + 15, 15);
        cvas.fillText(single, -15 + 5, -15);
        cvas.restore();
        strs.push(single)
    }

    // draw line and dot
    cvasInterfere(cvas, width, height)
})

function verifys() {
    // verify function
    var codeStr = strs.join('').toLowerCase();
    var inputCode = document.getElementById('code').value.toLowerCase();
    if (inputCode == codeStr) {
        alert('验证码：' + inputCode + '，通过验证。');
    } else {
        alert('很遗憾，未通过验证');
    }
}


