
function f = multiply(f1,f2,lA)
% MULTIPLY
%   Taken from MTEX. 
%   Multiply Fourier matrices.

f = zeros(numel(f1),1);
for l = 0:lA  
  ind = deg2dim(l)+1:deg2dim(l+1);  
  f(ind) = reshape(f1(ind),2*l+1,2*l+1) * ...
    reshape(f2(ind),2*l+1,2*l+1);
end

end