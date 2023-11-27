// Get all div elements by tag name
var currentDiv = document.getElementById('reload');

// Event listener for the custom HTML tag
currentDiv.addEventListener('mousedown', function () {
    // Get style and class from the element
    var id = this.id;

    // Send an AJAX request to the Django backend
    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        url: '/',  // Adjust the URL to match your Django URL pattern
        data: { 'id': id },
        dataType: 'json',
        success: function (data) {
            console.log('Response from server:', data);
        }
    });
});
;
function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}