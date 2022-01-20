// 要求三：JavaScript 建立載入更多的按鈕 (Optional)
// 在景點下方建立一個載入更多的按鈕，點擊就可以顯示額外 8 個景點資訊。
const url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
let container = document.getElementById('flex-container')

// 取得圖片第一張圖片網址與景點標題的list
function getData() {
  return (
    fetch(url)
      .then(response => response.json())
      .then(data => {
        let results = data.result.results;
        let attractions = { 'titleList': [], 'imgList': [] };
        for (let i in results) {
          let img = results[i].file.replaceAll('https', ' https').split(' ')
          attractions['imgList'].push(img[1])
          let title = results[i].stitle
          attractions['titleList'].push(title)
        }
        return attractions;
      })
      .catch(error => console.log('Error:', error))
  )
}

// 新增一個圖片+title的<div>區塊
// <div class='item' >
//   <img class='img' src ='imgURL'>
//   <div class='title'>title</div>
// </div >
function add_item(imgURL, title) {
  let item = document.createElement('div');   // 建立外層<div></div>
  item.className = 'item'   // <div class='item'></div>
  let img = document.createElement('img');   // 建立<img />
  img.className = 'img'   // <img class='img' />
  img.src = imgURL   // <img class='img' src='imgURL' />
  let titleText = document.createElement('div');   // 建立<div></div>
  titleText.className = 'title'   // <div class='title></div>
  titleTextNode = document.createTextNode(title)
  titleText.appendChild(titleTextNode)   // <div class='title'>title</div>
  item.appendChild(img)
  item.appendChild(titleText)
  return item;
}

// 初次載入顯示8張圖片
function load() {
  getData()
    .then(attractions => {
      let imgURLList = attractions.imgList;   // 同attractions['imgList']
      let titleList = attractions.titleList;   // 同attractions['titleList']
      for (let i = 0; i < 8; i++) {
        let itemBlock = add_item(imgURLList[i], titleList[i]);
        container.appendChild(itemBlock)
      }
    })
    .catch(error => console.log('Error:', error))
}


// 按下按鍵再顯示下8張圖片
let clicked = 0;   // 紀錄Load More被按下的次數，按下前為0
function loadMore() {
  clicked += 1   // 每執行一次loadMore()按鍵被按次數+1
  // console.log(clicked)
  let currentItems = 8 * clicked   // 載入下8張圖片前，當前的圖片數目
  getData()
    .then(attractions => {
      let imgURLList = attractions['imgList'];
      let titleList = attractions['titleList'];
      // 若剩下還未顯示的張數大於8張，則一次顯示8張
      if (titleList.length - currentItems >= 8) {
        for (let i = 8*clicked; i < 8*(clicked+1); i++) {
          let itemBlock = add_item(imgURLList[i], titleList[i])
          container.appendChild(itemBlock)
        }
      } else {
        // 若剩下的張數不足8張，則一張一張顯示直到沒有圖片
        for (let i = 8*clicked; i < titleList.length; i++) {
          let itemBlock = add_item(imgURLList[i], titleList[i])
          container.appendChild(itemBlock)
        }
        // 當圖片全部顯示則Load More按鍵消失
        document.getElementById('btn').hidden = true;
      }
    })
    .catch(error => console.log('Error:', error))
}


load();
let btn = document.getElementById('btn');
btn.addEventListener('click', loadMore);   // 當按下Load More按鍵，執行load8()函數，load8()執行8次add_item()