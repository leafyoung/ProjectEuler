fun sumMultsOfPair max x y = 
  let
    fun captured x lOfMs = foldr (fn (v,found) => if v = x then true else found) false lOfMs;

    fun getMultsOfX xMult lOfMs = 
      if xMult >= max then lOfMs
      else if (captured xMult lOfMs) then (getMultsOfX (xMult+x) lOfMs)
           else (getMultsOfX (xMult+x) (lOfMs@[xMult]));

    fun getMultsOfY yMult lOfMs = 
      if yMult >= max then lOfMs
      else if (captured yMult lOfMs) then (getMultsOfY (yMult+y) lOfMs)
           else (getMultsOfY (yMult+y) (lOfMs@[yMult]));

   in
     foldr (fn (z,sum) => sum+z) 0 (getMultsOfX x (getMultsOfY y []))
   end;

print (Int.toString(sumMultsOfPair 1000 3 5));

