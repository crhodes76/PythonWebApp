$(document).ready(function(){
    $('.primary-button').on('click', function(){
        $.ajax({
            url: '/test_method',
            type: 'POST',
            success:function(data)
            {
                console.log(data)
                alert(data)
            },
            error:function(error){
                console.log(error)
                alert(error)
            }
        })
    })
})