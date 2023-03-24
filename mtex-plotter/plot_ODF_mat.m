% --- plot_ODF_mat.m ---
% reads ODF.mat file
% plots pole figures of ODF using pole_figure_plot.m
% Saves pole figures image

%% import odf variable from file
filepath = "/Users/user/Desktop/Diamond_2022/034_Ti64_TIFUN-T4_TD_Deform_910C_1mms-1/fourier-peak-analysis-texture/alpha/";
load(strcat(filepath, "ODF.mat"));

%% plot pole figures
pole_figure_plot('alpha', odf, odf.CS, 0.5, 3, ...
strcat(filepath, "ODF_test"));