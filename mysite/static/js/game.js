$(function() {
    $('#game-form').on('submit', function(event) {
        event.preventDefault();
        number = $('#num').val();
        countChild = $('#otherValue').val();
        result = Number(number.value)
        if (number.length > 0 && !isNaN(number) && number >= 1 && countChild >= 0) {
            console.log('click');
            $('#error').text('');
            sendData();
        } else {
            //clear text field
            $('#num').val('');
            $('#error').text('Введено неправильное значение')
            //alert('Введено неправильное значения');
        }
    });

    function sendData() {
        console.log('sendData');
        $.ajax({
            url : "",
            type : "POST",
            data : { number: $('#num').val(),
                     countChild: $('#otherValue').val(),
                     per13div: $('radio13perdiv').val(),
                     per13: $('radio13per').val(),
                     per30: $('radio30per').val(),
                     checkChild: $('checkradioCountChild').val(),
                     checkInv: $('radioChildInv').val(),
                     csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            success : function (json) {
                $('#num').val('');
                console.log(json);
                $('#message').text(json['message'])
                console.log("success");
            },
            error : function(xhr, errmsg, err) {
                console.log(xhr.status + ' ' + xhr.responseText);
            }
        });
    };
});