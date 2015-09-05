// jshint ignore: start

function loadFeatured(data) {
  console.log(data);
  var template = $('#template-featured').html();
  Mustache.parse(template);
  var rendered = Mustache.render(template, {'featured': data});
  $('#target-featured').html(rendered);
}

function expandQuote(e) {
  return false;
}

$.get('/api/comment/', loadFeatured);
