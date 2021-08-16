$(document).ready(function () {
    $('#add_link').click(function (){
        $.ajax({
            url: "main_shop:add-cart" + $(this).data('id'),
            type: 'post',
            success: function (response){
                $
            }
        })

    })
})