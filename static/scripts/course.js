/* Copyright 2011, hast. All rights reserved.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or (at
 * your option) any later version.
 */

var Course = Backbone.Model.extend({
    url: function() { return urls['course_get'](this.get('slug')); },
});

var CourseView = Backbone.View.extend({
    initialize: function(params) {
        _.bindAll(this, 'render');
        this.model = new Course({slug: params.slug});
        this.model.on('change', this.render);
        this.model.fetch();
        this.render();
    },

    render: function() {
        $(this.el).css('padding', '10px 20px 10px 20px');
        $(this.el).html(templates['tpl-course'](this.model.toJSON()));
        return this;
    },
});
