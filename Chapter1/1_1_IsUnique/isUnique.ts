const isUniqueSet = (s: string): boolean => {
  let setty: Set<string> = new Set();
  for (let i = 0; i < s.length; i++) {
    if (setty.has(s[i])) {
      return false;
    } else if (!setty.has(s[i])) {
      setty.add(s[i]);
    }
  }

  return true;
};

const noSet = (s: string): boolean => {
  let listy: Array<string> = s.split("");
  listy.sort();
  for (let i = 0; i < listy.length - 1; i++) {
    if (listy[i] === listy[i + 1]) {
      return false;
    }
  }

  return true;
};

console.log(isUniqueSet("hello"));
console.log(noSet("hello"));
