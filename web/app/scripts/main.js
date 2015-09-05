// jshint ignore: start

function load_latest(data) {
  var template = $('#template-latest').html();
  Mustache.parse(template);
  var rendered = Mustache.render(template, {'latest': data});
  $('#target-latest').html(rendered);
}

function load_promised(data) {
  var ppl = {};
  data.objects.forEach(function(o) {
    var oid = o.councillor.id;
    if (!ppl[oid]) ppl[oid] = o.councillor;
    ppl[oid].promises = ppl[oid].promises || [];
    ppl[oid].promises.push({
      'id': o.id,
      'url': o.url,
      'text': o.text,
      'date': o.date,
    });
  });
  var land = $.map(ppl, function(value, index) { return [value]; });
  var template = $('#template-promised').html();
  Mustache.parse(template);
  var rendered = Mustache.render(template, {'promised': land});
  $('#target-promised').html(rendered);
}

$.get('/api/comment/', load_latest);
$.get('/api/promise/', load_promised);
