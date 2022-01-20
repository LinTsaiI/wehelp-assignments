// 要求一:函式與流程控制
// 在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
function calculate(min, max) {
  let cal = 0
  for(let x = min; x <= max; x++) {
    cal += x;
  }
  console.log(cal);
}

calculate(1, 3);
calculate(4, 8);



// 要求二:Python 字典與列表、JavaScript 物件與陣列
// 正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
function avg(data) {
  let sum = 0;
  for(let i = 0; i < data.count; i++) {
    sum += data.employees[i].salary;
  }
  let mean = sum / data.count;
  console.log(mean);
}

avg({
  "count": 3,
  "employees": [
    {
      "name": "John",
      "salary": 30000
    },
    {
      "name": "Bob",
      "salary": 60000
    },
    {
      "name": "Jenny",
      "salary": 50000
    },
  ]
}); // 呼叫 avg 函式



// 要求三:演算法
// 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
// 不可以使用排序相關的內建函式。
function maxProduct(nums) {
  let numsNew = [];
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      numsNew.push(nums[i] * nums[j]);
    }
  }
  console.log(Math.max(...numsNew));
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1, -2, 0]) // 得到 2

// 另一個寫法：
// function maxProduct(nums) {
//   let numsNew = [];
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = 0; j < i; j++) {
//       let num = nums[i] * nums[j];
//       numsNew.push(num);
//     }
//   }
//   console.log(Math.max(...numsNew));
// }

// 使用 map 改寫：
// function maxProduct(nums) {
//   let numsNew = [];
//   nums.map((n, i) => {
//     for(let j = i + 1; j < nums.length; j++) {
//       numsNew.push(n * nums[j]);
//     }
//   });
//   console.log(Math.max(...numsNew));
// }
// maxProduct([5, 20, 2, 6]) // 得到 120



// 要求四 ( 請閱讀英文 ):演算法
//  Given an array of integers, show indices of the two numbers such that they add up to a specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice.
function twoSum(nums, target) {
  for(let i = 0; i < nums.length; i++) {
    for(let j = 0; j < nums.length; j++) {
      if (i != j && target == nums[i] + nums[j]) {
        return [i, j];
      }
    }
  }
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

// // 另一個寫法：
// function twoSum(nums, target) {
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = 0; j < i; j++) {
//       if (target == nums[i] + nums[j]) {
//         return [i, j];
//       }
//     }
//   }
// }

// let result = twoSum([2, 11, 7, 15], 9);
// console.log(result);

// 使用 for...of 改寫：
// function twoSum(nums, target) {
//   for(x of nums) {
//     for(y of nums) {
//       if(nums.indexOf(x) != nums.indexOf(y) && target == x + y) {
//         return [nums.indexOf(x), nums.indexOf(y)]
//       }
//     }
//   }
// }

// let result = twoSum([2, 11, 7, 15], 9);
// console.log(result);

// 使用 for...in 改寫：
// function twoSum(nums, target) {
//   for (i in nums) {
//     for (j in nums) {
//       if (i != j && target == nums[i] + nums[j]) {
//         return [Number(i), Number(j)]
//       }
//     }
//   }
// }

// let result = twoSum([2, 11, 7, 15], 9);
// console.log(result);



// 要求五 (Optional): 演算法
//  給定只會包含 0 或 1 兩種數字的列表(Python) 或陣列(JavaScript) ，計算連續出現 0 的最大長度。
function maxZeros(nums) {
  let counter = 0;
  let numsNew = [];
  for(let i = 0; i < nums.length; i++) {
    if(nums[i] == 0) {
      counter += 1;
      numsNew.push(counter);
    } else {
      numsNew.push(0);
      counter = 0;
    }
  }
  console.log(Math.max(...numsNew));
}

maxZeros([0, 1, 0, 0])  // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) // 得到 4
maxZeros([1, 1, 1, 1, 1]) // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3
