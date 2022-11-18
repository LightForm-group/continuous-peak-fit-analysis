function odf_symm = symmetrise_ODF(odf, CS, SS)

% SYMMETRISE_ODF
%   A function for properly symmetrising the ODF. 
%   Since odf.SS=specimenSymmetry('orthorhombic')
%   only crops the ODF at the moment.

    f_hat = odf.components{1}.f_hat;
    qss = quaternion(SS);
    qcs = quaternion(CS);

    L = dim2deg(numel(f_hat));
    A = ones(1, L+1);
    
    if length(qcs)>1  % symmetrise crystal symmetry
        c = ones(1,length(qcs));
        f_hat = multiply(gcA2fourier(qcs,c,A),f_hat,length(A)-1);
    end
    
    if length(qss)>1  % symmetrise specimen symmetry
        c = ones(1,length(qss));
        f_hat = multiply(f_hat,gcA2fourier(qss,c,A),length(A)-1);
    end
    
    f_hat(1) = real(f_hat(1));
    f_hat = f_hat ./ f_hat(1);
    
    odf_symm = FourierODF(f_hat, CS, SS);

end