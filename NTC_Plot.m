% Given values
A = 1.120446846e-3;
B = 2.365502706e-4;
C = 0.7086713122e-7;

% Range for T
T = linspace(0.1, 50, 1000); % Adjust the range as needed

% Steinhart-Hart Equation rearranged for R
R = exp((1./(A + B*log(T+273.15) + C*(log(T+273.15)).^3)));

% Adjust the scale of R for better visualization
R_scaled = R / max(R) * 50000;

% Plotting
figure;
plot(T, R_scaled, 'LineWidth', 2);
xlabel('T (°C)');
ylabel('R (Ω)');
title('Steinhart-Hart Equation');
grid on;
ylim([0, 50000]); % Set y-axis limits
