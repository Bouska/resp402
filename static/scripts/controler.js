var ZoidRouter = Backbone.Router.extend({
    routes: {
        'profile': 'profile',
        'courses': 'course_list',
        '*url': 'default',
    },

    profile: function() {
        var view = new ProfileView({el: $('#content')});
    },

    course_list: function() {
    },

    default: function(url) {
        this.navigate('/profile', {trigger: true});
    },
});

$(document).ready(function() {
    // template compilation
    templates = {};
    _($('*[type="text/x-handlebars-template"]')).each(function(t) {
        templates[t.id] = Handlebars.compile($(t).html());
        Handlebars.registerPartial(t.id, $(t).html());
    });

    // start application
    var router = new ZoidRouter;
    Backbone.history.start();
});
