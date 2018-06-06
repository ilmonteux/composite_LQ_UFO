M$Restrictions = {
   LQQR[i_, j_] :> 0 /; NumericQ[i] && NumericQ[j] && i =!= j,
   LUDL[i_, j_] :> 0 /; NumericQ[i] && NumericQ[j] && i =!= j,
   LUUL[i_, j_] :> 0 /; NumericQ[i] && NumericQ[j] && i =!= j,
   LDDL[i_, j_] :> 0 /; NumericQ[i] && NumericQ[j] && i =!= j
};
