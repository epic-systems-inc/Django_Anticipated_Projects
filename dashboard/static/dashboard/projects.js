$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $("#modal").modal("show");
            },
            success: function(data){
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url: form.attr("action"), // action attribute in the form e.g. project/<pk>/update
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data){ // refers to the status of the HTTP request
                if (data.form_is_valid){                                                 // replace the table body with updated contents
                    $("#anticipated-projects-table tbody").html(data.html_project_list); // html_project_list is a key defined in the view
                    location.reload(); // then reload the page
                    $("#modal").modal("hide"); // close the modal
                }
                else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false; // to avoid the browser performing a full HTTP POST to the server, we cancel the default behavior, returning false in the function
    };

    /* Binding */
    // Update the project
    $("#anticipated-projects-table").on("click", ".js-update-project", loadForm);
    $("#modal").on("submit", ".js-project-update-form", saveForm);
});