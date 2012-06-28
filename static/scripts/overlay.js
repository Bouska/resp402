/* Copyright 2011, hast. All rights reserved.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or (at
 * your option) any later version.
 */

var Overlay = Backbone.View.extend({
    initialize: function(params) {
        _.bindAll(this, 'keycheck', 'close', 'show', 'render', 'refresh', 'make');
        this.overlay = document.createElement('div');
        this.overlay.id = 'overlay';
        this.visible = false;
        $(this.overlay).html(templates['tpl-overlay']());
        $(this.el).append(this.overlay);
        this.render();
    },

    events: {
        'click #overlay_close': function() { this.close() },
        'click #grey': function() { this.close() },
        'keypress': function(e) { this.keycheck(e) },
    },

    keycheck: function(e) {
        if (this.visible && e.keyCode == 27)
            this.close();
    },

    close: function() {
        this.visible = false;
        this.render();
    },

    show: function() {
        this.visible = true;
        this.render();
    },

    render: function() {
        if (this.visible) {
            $(this.overlay).css('display', 'block');
            this.refresh();
        } else
            $(this.overlay).css('display', 'none');
    },

    refresh: function() {
        var l, t;
        l = Math.max($(window).width() / 2 - $('#overlay_box').width() / 2, 3);
        t = Math.max($(window).height() / 2 - $('#overlay_box').height() / 2, 3);
        $('#overlay_box').css('top', t);
        $('#overlay_box').css('left', l);
        if ($('#overlay_box').width() > $('#grey').width())
            $('#grey').width($('#overlay_box').width() + 6);
        if ($('#overlay_box').height() > $('#grey').height())
            $('#grey').height($('#overlay_box').height() + 6);
    },
    
    make: function(title, template_name) {
        $('#overlay_title').html(title);
        $('#overlay_content').html(templates[template_name]());
        this.show();
    }
});

/*

$(window).resize(function() {
    if ($('#front').css('display') == 'block')
        overlay_refresh();
});

function overlay_reset() {
    $('#overlay_title').html('');
    $('#overlay_content').html('');
    $('#grey').css('width', '100%');
    $('#grey').css('height', '100%');
}

function overlay_title(title) { $('#overlay_title').html(title); }
function overlay_content(thing) { $('#overlay_content').html(thing); }
function overlay_append(thing) { $('#overlay_content').append(thing); }
function overlay_prepend(thing) { $('#overlay_content').prepend(thing); }

function overlay_form() {
    $(arguments).each(function (idx, form) {
        var hform = document.createElement('form');
        hform.id = form["id"];
        hform.method = 'post';
        if (form['enctype'])
            hform.enctype = form['enctype'];
        hform.action = form['url'];
        $(hform).append('<input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken"/>');
        $(hform).append('<table class="vtop">'+ form['content'] +'</table>');
        $(hform).append('<center><input type="submit" value="' + form['submit'] + '" id="' +
                       form['id'] + '_submit"/></center>');
        overlay_append('<div id="' + form["id"] + '_pre">');
        overlay_append(hform);
        overlay_append('<div id="' + form["id"] + '_app">');
    });
}
*/