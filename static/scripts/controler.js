/* Copyright 2011, hast. All rights reserved.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or (at
 * your option) any later version.
 */


/*******************************************************************************
 * Menu management
 */

var MenuItem = Backbone.Model.extend({
    // translate the data from the server into the model used here
    parse: function(data) {
        var res = {
            loaded: true,
            title: data.name,
            categories: data.holds,
            links: [],
        };
        for (i in data.items) {
            var item = data.items[i];
            res.links.push({url: '#/' + item.type + '/' + item.slug,  
                                name: item.name});
        }
        return res;
    },

    url: function() { return urls['category_get'](this.get('id')); },
});

var MainMenu = new MenuItem({
    id: 0,
    loaded: true,
    title: 'Home',
    toplink: '#profile',
    categories: [
        {id: '1', name: 'Courses'}],
    links: [
        {url: '#boards', name: 'General Forums'},
        {url: '#wall', name: 'Wall'},
        {url: '#help', name: 'Help'},
        {url: 'https://github.com/ekatsah/resp402', name: 'Sources'},
        {url: '/logout', name: 'Logout'},],
});

var MenuItemView = Backbone.View.extend({
    initialize: function(params) {
        _.bindAll(this, 'render', 'load');
        this.menu_id = params.id;
        this.indent = params.indent;
        this.count = 0;
        this.el.id = 'menuitem_' + this.menu_id;
        if (this.menu_id != 0) {
            this.model = new MenuItem({id: this.menu_id, loaded: false});
            this.model.on("change", this.render);
            this.model.fetch();
        } else
            this.model = MainMenu;
        this.render();
    },

    events: {
        'click .link': 'load',
    },
    
    load: function(e) {
        var category = e.currentTarget.id.substring(14, 20);
        $(this.el).trigger('load', [ category, this.indent ]);
    },

    render: function() {
        $(this.el).addClass('left');
        if (this.model.get('loaded'))
            $(this.el).html(templates['tpl-menu-item'](this.model.toJSON()));
        else
            $(this.el).html(templates['tpl-menu-item']({
                id: this.menu_id,
                title: 'Loading..',
                links: [{name: 'Loading..'}]}));
        return this;
    },
});

var MenuView = Backbone.View.extend({
    initialize: function(params) {
        _.bindAll(this, 'render', 'load', 'toggle');
        this.visibility = false;
        $(this.el).bind('load', this.load);
        $(this.el).append((new MenuItemView({
            id: 0, 
            el: document.createElement('dl'),
            indent: 0
        })).el);
    },
    
    load: function(e, category, indent) {
        $('#menu dl:gt(' + indent + ')').remove();
        $(this.el).append((new MenuItemView({
            id: category, 
            el: document.createElement('dl'),
            indent: indent + 1,
        })).el);
    },

    toggle: function() {
        if (this.visibility) {
            this.visibility = false;
            $(this.el).slideUp(100);
            $('#header').delay(90).addClass('shadow');
        } else {
            this.visibility = true;
            $('#header').delay(90).removeClass('shadow');
            $(this.el).slideDown(100);
        }
    },
});


/*******************************************************************************
 * Main loop, url entry
 */

var ZoidRouter = Backbone.Router.extend({
    routes: {
        'profile': 'profile',
        'courses': 'course_list',
        'course/:id': 'course_view',
        'group/:id': 'group_view',
        '*url': 'default',
    },

    profile: function() {
        new ProfileView({el: $('#content')});
    },

    course_list: function() {
    },

    course_view: function(slug) {
    },

    group_view: function(slug) {
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
    
    // Create the first item in the menu
    var menu = new MenuView({el: '#menu'});
    $("#header").click(menu.toggle);
});
