// 要求二：JavaScript 取得網路上的資料並顯示在網頁畫面中
fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
  .then(response => response.json())
  .then(data => {
    let attractions = data.result.results
    for (let i in attractions) {
      let img_list = attractions[i].file.replaceAll('https', ' https').split(' ')   // 取得圖片網址的array，第[0]個為''
      let img_block = document.createElement('img')   // 建立<img />
      img_block.setAttribute('src', img_list[1])   // 設定<img src='img_list[1]' />，取得第一張圖片的網址
      img_block.setAttribute('class', 'img')
      document.getElementsByClassName('item')[i].appendChild(img_block)   // 將<img src='img[0]' />附加到<div class='item'>之中
      let title_block = document.createElement('div')   // 建立<div></div>
      title_block.setAttribute('class', 'title')   // 設定<div class='title'></div>，作為放入標題文字的區塊
      let title_text = document.createTextNode(attractions[i].stitle)   // 建立text node，文字為attractions array中的stitle
      title_block.appendChild(title_text)   // 將text node文字放入<div class='title'></div>中
      document.getElementsByClassName('item')[i].appendChild(title_block)   // 將<div class='title'>attractions[i].stitle</div>附加到<div class='item'>之下
    }
  })
  .catch(error => console.log('Error:', error))



// 方法二：<img class='img' alt='scenery' /> 及 <div class='title'></div> 需先存在HTML file中
// fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
//   .then(response => response.json())
//   .then(data => {
//     let attractions = data.result.results
//     for (let i = 0; i < attractions.length; i++) {
//       let img = attractions[i].file.replaceAll('https', ' https').split(' ')
//       title = document.createTextNode(attractions[i].stitle)
//       document.getElementsByClassName('img')[i].src = img[1]
//       document.getElementsByClassName('title')[i].appendChild(title)
//     }
//   })
//   .catch(error => console.log('Error:', error))



// 練習：使用 innerHTML 改寫
// fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
//   .then(response => response.json())
//   .then(data => {
//     let attractions = data.result.results
//     for (let i in attractions) {
//       let img_list = attractions[i].file.replaceAll('https', ' https').split(' ')   // 取得圖片網址的array，第[0]個為''
//       let img_block = document.createElement('img')   // 建立<img />
//       img_block.setAttribute('src', img_list[1])   // 設定<img src='img_list[1]' />，取得第一張圖片的網址
//       img_block.setAttribute('class', 'img')
//       document.getElementsByClassName('item')[i].appendChild(img_block)   // 將<img src='img[0]' />附加到<div class='item'>之中
//       let title_block = document.createElement('div')   // 建立<div></div>
//       title_block.setAttribute('class', 'title')   // 設定<div class='title'></div>，作為放入標題文字的區塊
//       title_block.innerHTML = attractions[i].stitle   // 將標題文字塞到<div class='title'></div>中
//       document.getElementsByClassName('item')[i].appendChild(title_block)   // 將<div class='title'>attractions[i].stitle</div>附加到<div class='item'>之下
//     }
//   })
//   .catch(error => console.log('Error:', error))
