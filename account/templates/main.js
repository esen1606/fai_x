const content = [document.getElementById("content"), document.getElementById("content2"), document.getElementById("content3")]

function changePage(pageNumber) {
    content.map(item=> item!==pageNumber?item.style.display.none: '')
  }
  