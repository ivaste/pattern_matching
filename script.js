
// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
  // Great success! All the File APIs are supported.
} else {
  alert('The File APIs are not fully supported in this browser.');
}

//Global Variables
var reference_files=[];
var remaining=-1;   // remaining texts to load
var string_to_check="";        // String to check
var window_size=4;
var reference_file_list=[];

var btn_solve = document.getElementById('btn_solve');

function enableButton(){
  if (remaining!==0 ||string_to_check.length===0){
    return;
  }
  btn_solve.classList.remove("disabled");
}

// Dropped PATTERN FILE
function handleFileSelect_pattern(evt) {
	evt.stopPropagation();
	evt.preventDefault();
  var files = evt.dataTransfer.files; // FileList object. Is a FileList of File objects.
  var file_to_read=files[0];          // we just care about 1 single file.
  var reader= new FileReader();       // istantiate FileReader
  reader.onload = function (e) {      // function called when file is fully loaded
    string_to_check=e.target.result;  // assign to the global variable the string of the file to check
    console.log(string_to_check);
    enableButton();                   //  try to enable button solve
  };
  reader.readAsText(file_to_read);    // Start reading the file
  document.getElementById('patter_file').innerHTML = file_to_read.name;// Display on the html the name of the file
  
}

// Dropped REFERENCE FILES
function handleFileSelect_texts(evt) {
	evt.stopPropagation();
	evt.preventDefault();
  var files = evt.dataTransfer.files; // FileList object. Is a FileList of File objects.
  remaining=files.length;
  for (var i = 0, file_to_read; file_to_read = files[i]; i++) {
    reference_file_list.push("<li>"+file_to_read.name+"</li>");
    var reader= new FileReader();       // istantiate FileReader
    reader.onload = function (e) {      // function called when file is fully loaded
      remaining-=1;                     // Reduce by 1 the amount of remaining files to read
      reference_file=e.target.result;
      reference_files.push(reference_file);       // Add to the gloabal variable (array of strings) the string of the readed file
      console.log(reference_file);
      //When finished opening all reference_files
      if (remaining===0){
        enableButton(); //Enable button solve.
        console.log(reference_files);
        // Display on the html the list of names of the files
        document.getElementById('ref_files_list').innerHTML = '<ul>' + reference_file_list.join('') + '</ul>';
      }
    };
    reader.readAsText(file_to_read);    // Start reading the file
  }

}

function handleDragOver(evt) {
	evt.stopPropagation();
	evt.preventDefault();
	evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
}


var updateDiv=document.getElementById('solution');
// When CLICK on SOLVE BUTTON
function btn_solve_click(evt){
  if (remaining!==0){
    alert("Reference files not loaded yet");
    return;
  }
  if (string_to_check.length===0){
    alert("File to check not loaded yet");
    return;
  }

  btn_solve.classList.add("disabled");

  console.log("calculating ...");

  //Preprocess string_to_check
  string_to_check=string_to_check.replace("\n", " ");
  string_to_check=string_to_check.toLowerCase();
  string_to_check=string_to_check.split(" ");
  console.log(string_to_check);

  //Create mask for the solution
  var ans=new Array(string_to_check.length);
  for (var i = 0; i < ans.length; ++i) { ans[i] = false; }

  //Insert patterns in the Trie
  var trie={};
  for (var i=0; i<string_to_check.length-window_size;i++){
    var pattern=string_to_check.slice(i,i+window_size).join(" ");
    var n=trie;
    for (let j=0; j<pattern.length;j++){
      var c=pattern[j];

      if (! (c in n)){n[c]={}}
      n=n[c];
    }
    if (! ("pattern" in n)){n["pattern"]=[]}
    n["pattern"].push(i);
  }
  console.log("Trie",trie);

  let occurencies = new Set();
  //for each reference file
  for (var i = 0, reference_file; reference_file = reference_files[i]; i++) {
    var text=reference_file.replace("\n", " ");
    text=text.toLowerCase();  // to lower case

    console.log("Reference Text "+i+": "+text.split(" ").length+" words");

    //For each char in the text, tranverse the trie
    for (var j=0;j<text.length;j++){
      var n=trie;
      k=j;
      while(k<text.length & (text[k] in n)){
        n=n[text[k]];
        k++;
        if ("pattern" in n){
          n["pattern"].forEach(e => {
            occurencies.add(e);
          });
        }
      }
    }

  }

  console.log(occurencies);
  for (let i of occurencies){
    for (let k = i; k < i+window_size; k++) {
          
      ans[k]=true;
    }
  }


  // Build solution
  var solution=[];
  for (let i = 0; i < ans.length; i++) {
    if (ans[i]){
      /*solution.push("<mark>"+string_to_check[i]+"</mark>")*/
      solution.push('<strong style="color: red">');
      solution.push(string_to_check[i]);
      solution.push("</strong>");
    }else{
      solution.push(string_to_check[i]);
    }
  }

  solution=solution.join(" ");

  //Calculate percentage
  var div_solution=document.getElementById('solution')
  var matches=0;
  for (let i = 0; i < ans.length; i++) {
    if (ans[i]) {matches++;}    
  }
  var perc=Math.round(100*matches/ans.length,2);

  //Display percentage
  var p=document.createElement('p');
  p.innerHTML = "<strong>"+perc+"% ("+matches+"/"+ans.length+" words) of document match, with window size="+window_size+"</strong>";
  div_solution.appendChild(p);

  //Display solution
  var newdiv=document.createElement("div");
  newdiv.classList.add("card");
  var newdiv2=document.createElement("div");
  newdiv2.classList.add("card-body");
  newdiv2.innerHTML=solution;
  newdiv.appendChild(newdiv2);
  div_solution.appendChild(newdiv);


}


// Setup the dnd listeners.
var dropZone_pattern = document.getElementById('dropZone_pattern');
dropZone_pattern.addEventListener('dragover', handleDragOver, false);
dropZone_pattern.addEventListener('drop', handleFileSelect_pattern, false);

var dropZone_texts = document.getElementById('dropZone_texts');
dropZone_texts.addEventListener('dragover', handleDragOver, false);
dropZone_texts.addEventListener('drop', handleFileSelect_texts, false);

// Setup button listener.
btn_solve.addEventListener('click',btn_solve_click);