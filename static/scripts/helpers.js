/* Copyright 2011, hast. All rights reserved.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or (at
 * your option) any later version.
 */


function rdump_(obj, indent, depth) {
    if (depth > 10)
        return 'max depth';

    var str = '';
    for (key in obj)
        if (typeof obj[key] == 'object')
            str += indent + key + ':\n' + rdump_(obj, indent + '   ', depth + 1);
        else 
            str += indent + key + ': ' + obj[key] + '\n';
    return str;
}

function dump_(obj) {
    var str = '';
    for (key in obj)
        str += key + ': ' + obj[key] + '\n';
    return str;
}

function dump(obj) {
    return dump_(obj);
}

function recurloop(func, delay, times, count) {
    if (count == undefined)
        var count = 0;
    if (count < times) {
        func();
        setTimeout(function() { recurloop(func, delay, times, count + 1); }, delay);
    }
}