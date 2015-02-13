/**
 * Created by Sam Keller on 1/11/2015.
 */
var output = '';
var text = '';
var csvText = '';
var csvarray = [];

function readSingleFile(event) {
    output = document.getElementById("output");
    var file = event.target.files[0];
	var type = file.name;
	var ext = type.substring((type.length)-4, (type.length));
	if(ext == '.csv')
	{
        if(file){
			var reader = new FileReader();
			reader.onload = function(e) {
				  var contents = e.target.result.split('\n');
				  parseString(contents);
			}
			reader.readAsText(file);
		}
		else {
		  	alert("Failed to load file");
		}
	}
	else{
		alert("You loaded a file with a "+ext+" extension!  This program only accepts .csv files.");
		document.getElementById('txt').innerHTML = '';
	}
}

function parseString(blob) {
    var headers = blob[0];
    var splitHeader = headers.split(',');
    var headerArray = new Array();
    for (var i = 0; i < splitHeader.length; i++) {
        headerArray[i] = splitHeader[i].trim();
        csvText += splitHeader[i].trim();
        if (i != splitHeader.length - 1) {
            csvText += ',';
        }
    }
    csvText += '\n';
    for (var i = 1; i < blob.length - 1; i++) {
        headers = blob[i];
        headers = headers.split(',');
        var temp = {};
        for (var j = 0; j < headers.length; j++) {
            var value = headers[j].trim();
            if (j != headers.length - 1)//because of last line empty in csv
            {
                csvText += value;
                csvText += ',';
            }
            else {
                csvText += value;
            }
            var field = headerArray[j];
            temp[field] = value;
        }
        csvText += '\n';
        text += JSON.stringify(temp,null,'\t');
        text += '\n';
        csvarray.push(temp);
    }
    var txtArea = document.createElement('textarea');
    txtArea.style.width = '400px';
    txtArea.style.height = '400px';
    txtArea.value = text;
    txtArea.readOnly = true;
    output.appendChild(txtArea);
}

