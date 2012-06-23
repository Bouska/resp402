/* Copyright 2011, hast. All rights reserved.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or (at
 * your option) any later version.
 */


var User = Backbone.Model.extend({
    initialize: function(params) {
        if (params.target == 'me')
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
        this.myself.on('change', this.render);
        this.myself.fetch();
        this.courses = new Backbone.Collection();
        this.courses.bind('all', this.render, this);
        this.courses.url = urls['course_all'];
        this.courses.fetch();
        this.render();
    },

    render: function() {
        $(this.el).html(templates['tpl-profile']({
            realname: this.myself.get('realname'),
            courses: this.courses.toJSON(),
        }));
        return this;
    },
});
