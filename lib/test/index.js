const AlfredItem = require('alfred-item');
const shortid = require('shortid');
const id = function() {
    return 0 + Math.random();
    // return shortid.generate();
};
const item = new AlfredItem();

item.addItem(id(), 'test', 'ss');
const args = process.argv.slice(2);
console.log(item);
console.warn('ss', args, process);
