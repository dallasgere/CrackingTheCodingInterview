const isUnique = (s: string): boolean => {
  let setty: Set<string> = new Set();
  for (let i = 0; i < s.length; i++) {
    if (setty.has(s[i])) {
      return false;
    }
  }

  return true;
};

console.log(isUnique("hello"));
