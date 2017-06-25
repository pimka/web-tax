$(function() {
    $('#game-form').on('submit', function(event) {
        event.preventDefault();
        number = $('#num').val();
        countChild = $('#otherValue').val();
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
        console.log('number', number);
        console.log('countChild', countChild);
        console.log('per13div', $('#radio13perdiv').prop('checked'));
        console.log('per13', $('#radio13per').prop('checked'));
        console.log('per30', $('#radio30per').prop('checked'));
        console.log('checkChild', $('#checkradioCountChild').prop('checked'));
        console.log('checkInv', $('#radioChildInv').prop('checked'));
        $.ajax({
            url : "",
            type : "POST",
            data : { number: $('#num').val(),
                     countChild: $('#otherValue').val(),
                     per13div: $('#radio13perdiv').is(':checked'),
                     per13: $('#radio13per').is(':checked'),
                     per30: $('#radio30per').is(':checked'),
                     checkChild: $('#checkradioCountChild').is(':checked'),
                     checkInv: $('#radioChildInv').is(':checked'),
                     csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            success : function (json) {
                $('#num').val('');
                $('#otherValue').val('');
                console.log(json);
                $('#message').text(json['message'])
                if (json['result'] !== 'none') {
                    $('#button').prop('disabled', true);
                }
                console.log("success");
            },
            error : function(xhr, errmsg, err) {
                console.log(xhr.status + ' ' + xhr.responseText);
            }
        });
    };
});