var button = document.getElementById('button');
var headPage = document.getElementById('headPage');
var content = document.getElementById('content');

var change = {
    'vanhoc':'Văn học',
    'phattrienbanthan': 'Phát triển bản thân',
    'kinhte':'Kinh tế'
}
function showContent(res){
    var table = document.getElementById('table__content');
    table.innerHTML="";
    var row; 
    for (var i = 0;i<20;i++){
        row = document.createElement('tr');
        table.appendChild(row);

        var bookCover = document.createElement('td');
        bookCover.innerHTML= '<img src="' + res.result[i].img + '" alt="ảnh bìa" class="content__cover" >';
        row.appendChild(bookCover);

        var name = document.createElement('td');
        name.innerHTML= res.result[i].name;
        row.appendChild(name);

        var author = document.createElement('td');
        author.innerHTML = res.result[i].author;
        row.appendChild(author);

        var type = document.createElement('td');
        type.innerHTML = change[res.result[i].class];
        row.appendChild(type);

        var button = document.createElement('button');
        button.className="btn buttonDetail";
        button.setAttribute('data-toggle','modal');
        button.setAttribute('data-target','#contentDetail');
        button.setAttribute('id','button'+i);
        button.innerHTML="Xem chi tiết";

        var detail = document.createElement('td');
        detail.appendChild(button);
        row.appendChild(button);          
        
    }   

    var seeMoreButtons = document.getElementsByClassName('buttonDetail');

    for (var index = 0; index < seeMoreButtons.length; index++) {
        var b = seeMoreButtons[index];
        b.addEventListener('click', showDetail);
    }

    function showDetail(e) {
        console.log(e.target.id.split("button")[1]);
        console.log(res);
        var title = document.getElementById('detailTitle');
        var body = document.getElementById('detailBody');
        body.innerHTML="";

        title.innerHTML=res.result[parseInt(e.target.id.split("button")[1])].name;

        // row1
        var row1 = document.createElement('div');
        row1.className="row"
        body.appendChild(row1);
        
        //image
        var leftRow =  document.createElement('div');
        leftRow.className="col-sm-5";
        row1.appendChild(leftRow);

        var coverImage = document.createElement('img');
        coverImage.src=res.result[parseInt(e.target.id.split("button")[1])].img;
        coverImage.alt="Ảnh bìa";
        coverImage.className="detailImageCover";
        leftRow.appendChild(coverImage);

        //content
        var rightRow = document.createElement('div');
        rightRow.className="col-sm-7";
        row1.appendChild(rightRow);

        var bookId = document.createElement('div');
        bookId.innerHTML="<strong>Mã sách</strong>: " + res.result[parseInt(e.target.id.split("button")[1])].isbn;
        rightRow.appendChild(bookId);

        var bookType = document.createElement('div');
        bookType.innerHTML="<strong>Thể loại</strong>: " + change[res.result[parseInt(e.target.id.split("button")[1])].class];
        rightRow.appendChild(bookType);
        
        var bookAuthor = document.createElement('div');
        bookAuthor.innerHTML="<strong>Tác giả</strong>: " + res.result[parseInt(e.target.id.split("button")[1])].author;
        rightRow.appendChild(bookAuthor);

        var bookPublisher = document.createElement('div');
        bookPublisher.innerHTML="<strong>Nhà phát hành</strong>: " + res.result[parseInt(e.target.id.split("button")[1])].publisher;
        rightRow.appendChild(bookPublisher);

        //row 2
        var row2 = document.createElement('div');
        row2.className="row";
        body.appendChild(row2);

        var descriptionCover = document.createElement('div');
        descriptionCover.className="col-sm-12";
        row2.appendChild(descriptionCover);

        var description = document.createElement('p');
        description.innerHTML="<strong>Mô tả</strong>: " + res.result[parseInt(e.target.id.split("button")[1])].description;
        descriptionCover.appendChild(description);

    }

}

var text,
    data,
    settings;

$("#watchButton").click(function(){
    text = document.getElementById('headPage-text').value;
    if(text == ""){
        alert("Vui lòng nhập gợi ý vào phần nhập");
    }else{
        headPage.className+=" hidden";
        content.classList.remove('hidden');
        
        data = "{\n\t\"data\":\"" +text + "\"\n}";
        settings = {
            "async": true,
            "crossDomain": true,
            "url": "http://127.0.0.1:5000/search",
            "method": "POST",
            "headers": {
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
                "Postman-Token": "3bde9003-6482-4af5-9cde-510c631414e2"
            },
            "processData": false,
            "data": data
        };
        
        $.ajax(settings).done(function (response) {
            showContent(response);
        });
        
    }
});

$("#continueFinder").click(function(){
    text = document.getElementById('textFinder').value;
    if(text == ""){
        alert("Vui lòng nhập gợi ý vào phần nhập");
    }else{
        data = "{\n\t\"data\":\"" +text + "\"\n}";
        settings = {
            "async": true,
            "crossDomain": true,
            "url": "http://127.0.0.1:5000/search",
            "method": "POST",
            "headers": {
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
                "Postman-Token": "3bde9003-6482-4af5-9cde-510c631414e2"
            },
            "processData": false,
            "data": data
        };
        
        $.ajax(settings).done(function (response) {
            showContent(response);
        });
        
    }
});


