// jshint ignore: start

function loadFeatured() {
  data = {
    'featured': [
      {
        'name': 'Bob'
      },
      {
        'name': 'Jim'
      }
    ]
  };
  var template = $('#template-featured').html();
  Mustache.parse(template);
  var rendered = Mustache.render(template, data);
  $('#target-featured').html(rendered);
}

loadFeatured();
