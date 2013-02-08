$(function() {
  $('#pub_date').datepicker({ dateFormat: "dd/mm/yy"});
});

$.fn.serializeObject = function()
{
    /*
     * jQuery doesn't have the ability to serialize objects so we'll use
     * this little script to do that (useful to convert form data to json).
     */ 
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

//Backbone.Tastypie.csrfToken = $('meta[name="csrf-token"]').attr('content');
Backbone.Tastypie.csrfToken = $.cookie('csrftoken');
Backbone.Tastypie.apiKey = {
    username: USER,
    key: API_KEY
};
