fun smallestMultiple curr = 
  let 
     fun testDivs x 20 = true
       | testDivs x d = if (x mod d) = 0 then (testDivs x (d+1)) else false;
  in
     if (testDivs curr 11) then curr else smallestMultiple (curr+2)
  end;
