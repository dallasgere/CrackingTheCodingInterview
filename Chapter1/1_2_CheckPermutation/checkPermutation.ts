const checkPermutation = (s: string, t: string): boolean => {
  /**
   * This is my solution
   *
   * time complexity: O(n log(n)) due to sorting
   * space complexity: O(n)
   *
   * Questions:
   * 1. is this case sensitive or not
   * 2. is whitespace significant
   */

  if (s.length != t.length) {
    return false;
  }

  s = s.toLocaleLowerCase().split("").sort().join("");
  t = t.toLocaleLowerCase().split("").sort().join("");
  return s === t;
};

console.log(checkPermutation("hello", "ollhe"));
console.log(checkPermutation("dallas", "taylor"));
