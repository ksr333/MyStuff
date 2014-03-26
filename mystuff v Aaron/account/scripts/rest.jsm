<script type="text/javascript">
</script>

$(function () {
    $('#charge').click(function () {
     ...
    });

    $('#queryCharges').click(function () {
     ...
    });

    $('#message').text('Charging...');
    $.ajax({
        {
            // The endpoint we’re talking to
            url: 'http://dithers.cs.byu.edu/iscore/api/v1/charges',

           // Method type (an HTTP verb like ‘post’ or ‘get’ data: { ... }, // Object with data fields this request needs
            type: 'post',

            // The type of data we want the server to return
            dataType: 'json',

            // Callback function to invoke if the call works
            success: function (data) { ... },

            // Callback function to invoke if the call fails
            error: function (data) { ... }
        }

    });

});