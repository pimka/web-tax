$(function() {
    $('#game-form').on('submit', function(event) {
        event.preventDefault();
        number = $('#num').val();
        result = Number(number.value)
        if (number.length > 0 && !isNaN(number) && number >= 1 && number <= 100) {
            console.log('click');
            $('#error').text('');
            prev_tries = $('#prev_tries').text();
            prev_tries += $('#num').val() + ' ';
            $('#prev_tries').text(prev_tries);
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
                     prev_tries: $('#prev_tries').text(),
                     csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            success : function (json) {
                $('#num').val('');
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