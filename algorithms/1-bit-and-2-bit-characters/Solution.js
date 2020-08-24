/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
  let skip_next = false, curr = null;
  for (const element of bits){
    if (skip_next){
      skip_next = false
      curr = 2
      continue
    }
    if (element === 1){
      skip_next = true;
      curr = 2;
    }else{
      skip_next = false;
      curr = 1;      
    }
  }
  return curr === 1;      
};