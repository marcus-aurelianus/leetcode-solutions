/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  const res = [];

  nums.sort(function (a,b){return a-b;});
  
  for (let i=0;i<nums.length;i++){
      if (nums[i] > 0){
          break;
      }
          
      if (i > 0 && nums[i] === nums[i - 1]){continue;}
          
      let target = -nums[i];
      let start = i + 1, end = nums.length - 1;
      while (start < end){
          let s = nums[start] + nums[end];
          if (s < target){
              start += 1;
          }else if (s > target){
              end -= 1;
          }else{
              console.log(i,start,end);
              res.push([nums[i], nums[start], nums[end]])
              while (start < end && nums[start] === nums[start + 1]){start += 1;}
              while (start < end && nums[end] === nums[end - 1]){end -= 1;}    
              start+=1;
              end-=1;
          }
      }
  }
  return res;
};