$(function(){
	get_listing(get_location());
});

function get_listing(path)
{
	if(path == '') path = '.';
	$.get('/FileList?path='+path, function(data){
		var directory = '', files = '', ul = '<ul>', eul = '</ul>';;

		html = '<h1>'+path+'</h1>';
		html += '<div class="back"><a href="javascript: history.back();">Ein Verzeichnis hinauf</a></div>';

		data.forEach(function(entry){
			if(entry.isDirectory)
				directory += '<li><img src="/static/img/dir.png" alt="dir"><a href="?path='+get_path(entry.name)+'">'+entry.name+'</a></li>';
			else
				files += '<li><img src="/static/img/file.png" alt="file">'+entry.name+'</li>';
		});
		
		html += ul+directory+eul;
		html += ul+files+eul;

		$('#filelist').html(html);
	});
}

function get_path(path)
{
	var current = get_location();
	
	if(current == '' || current == '.')
		return path;
	else
		return current+'/'+path;		
}

function get_location()
{
	var raw = window.location.search.replace("?", "");
    var split = raw.split("&");

    var current = '.';

    split.forEach(function(element){
        var parameters = element.split("=");
        if(parameters[0] == 'path' && parameters[1] != undefined)
        {
            current = parameters[1];
            return;
        }
    });

	return current;
}
