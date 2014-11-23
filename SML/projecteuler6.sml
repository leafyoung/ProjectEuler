fun sumSquaresUnder 0 = 0
  | sumSquaresUnder 1 = 1
  | sumSquaresUnder x = (x*x) + (sumSquaresUnder (x-1));

fun squareSumUnder 0 = 0
  | squareSumUnder 1 = 1
  | squareSumUnder x = 
    let 
      fun calcSumUnder 1 sum = sum+1
        | calcSumUnder x sum = calcSumUnder (x-1) (sum+x);
      val sum = calcSumUnder x 0;
    in 
      sum*sum
    end;

