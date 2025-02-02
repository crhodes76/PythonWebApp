$(document).ready(function(){
    var theDataObject = {};
    $('.primary-button').on('click', function(){
        var ai_question = $('#chatBotQuestionInput').val();
        var property_1 = "TEST1";
        var property_2 = "TEST2";
        var property_3 = "TEST3";
        theDataObject.ai_question = ai_question;
        theDataObject.property_1 = property_1;
        theDataObject.property_2 = property_2;
        theDataObject.property_3 = property_3;
        console.log('The question is ' + ai_question);
        console.log(ai_question);
        $.ajax({
            url: '/gemini_query',
            type: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({ theDataObject }),
            success:function(data)
            {
                console.log('Status');
                console.log(data.status);
                console.log('Data');
                console.log(data);
                if(data.status === 'success'){
                    var gemini_response = data.data.key1;
                    console.log(gemini_response)
                    $('#geminiResponse').text(gemini_response);
                    $('.date-time-response').text(data.dateTime);
                }
            },
            error:function(error){
                console.log(error)
                //alert(error)
            }
        })
    })
})