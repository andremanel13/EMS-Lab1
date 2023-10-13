% Steinhart-Hart model coefficients
A = 1.120446846e-3;
B = 2.365502706e-4;
C = 0.7086713122e-7;

% Thermistor function coefficients
R0 = 10e3;
Beta = 3965;
T0 = 25 + 273.15;

% Range for T
T = linspace(0.1, 50, 1000);

% Steinhart-Hart Equation rearranged for R
R_steinhart = exp(1./(A + B*log(T + 273.15) + C*(log(T + 273.15)).^3));

% Thermistor function
R_thermistor = R0 * exp(Beta * ((1./(T + 273.15)) - (1/T0)));

% Adjust the scale of R for better visualization
R_steinhart_scaled = R_steinhart / max(R_steinhart) * 50000;
R_thermistor_scaled = R_thermistor / max(R_thermistor) * 50000;

% Plotting
figure;
plot(T, R_steinhart_scaled, 'LineWidth', 2, 'DisplayName', 'Steinhart-Hart Equation');
hold on;
plot(T, R_thermistor_scaled, 'LineWidth', 2, 'DisplayName', 'Thermistor Function');
xlabel('T (°C)');
ylabel('R (Ω)');
title('Steinhart-Hart Equation and Thermistor Function');
grid on;
ylim([0, 50000]); % Set y-axis limits
legend;