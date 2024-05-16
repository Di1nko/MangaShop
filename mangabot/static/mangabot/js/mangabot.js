$(document).ready(function() {
    $('#manga-form').on('submit', function(e) {
        e.preventDefault(); // Предотвращаем стандартную отправку формы

        var topic = $('#topic').val();
        var csrftoken = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            url: '/api/generate', // Убедитесь, что URL корректен
            data: {
                topic: topic,
                csrfmiddlewaretoken: csrftoken
            },
            success: function(response) {
                // Обработка успешного ответа
                if (response.error) {
                    alert(response.error); // Показываем сообщение об ошибке
                } else {
                    // Отображаем ответ в элементе response
                    $('.response').html(response.text);
                }
            },
            error: function(xhr, status, error) {
                // Обработка ошибки запроса
                alert("Произошла ошибка при отправке запроса.");
            }
        });
    });
});