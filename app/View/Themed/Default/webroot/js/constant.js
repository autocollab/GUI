// defind api
const API_LOGIN = 'https://distributed.webi.vn/api/user/login';
const SOCKET = 'http://10.0.0.35:5000';
// const SOCKET = 'http://192.168.1.202:5000';

// 
function startSending() {
    is_sending = true;
    $('body').css('cursor', 'not-allowed');
}

function endSending() {
    is_sending = false;
    $('body').css('cursor', 'auto');
}



