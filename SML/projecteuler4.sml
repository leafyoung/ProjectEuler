fun reverseString x = foldl (fn (letter,newstr) => (str letter)^newstr) "" (explode x);
fun isPalindrome x = if (reverseString x) = x then true else false;
fun largestPalindrome 999 999 largest = if isPalindrome (Int.toString (999*999)) then 999*999 else largest
  | largestPalindrome x 999 largest =
    if isPalindrome (Int.toString(x*999)) andalso (x*999) > largest then (largestPalindrome (x+1) (x+1) (x*999))
    else (largestPalindrome (x+1) (x+1) largest)
  | largestPalindrome x y largest =
    if isPalindrome (Int.toString(x*y)) andalso (x*y) > largest then (largestPalindrome x (y+1) (x*y))
    else (largestPalindrome x (y+1) largest)

