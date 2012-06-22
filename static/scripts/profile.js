var User = Backbone.Model.extend({
    initialize: function(params) {
        if (params.target == "me")
            this.url = function() {
                return urls['profile_me'];
            }
        else {
            this.set({id: params.target});
            this.url = function(id) {
                return urls['profile_get'](id);
            }
        }
    },
});

var ProfileView = Backbone.View.extend({
    initialize: function() {
        _.bindAll(this, 'render');
        this.myself = new User({target: 'me'});
        this.myself.on("change", this.render);
        this.myself.fetch();
        this.render();
    },

    render: function() {
        $(this.el).html(templates['tpl-profile']({
            realname: this.myself.get('realname'),
        }));
        return this;
    },
});
