s = tf('s');
P_pitch = (1.151*s + 0.1774) / (s^3 + 0.739*s^2 + 0.921*s);

% Open-loop impulse response
figure;
impulse(P_pitch);
title('Open-loop Impulse Response');
xlabel('Time');
ylabel('Amplitude');

% Bode plot
figure;
bode(P_pitch);
title('Bode Plot');

% Open-loop step response
t = 0:0.01:10;
figure;
step(0.2 * P_pitch, t);
axis([0 10 0 0.8]);
ylabel('Pitch Angle (rad)');
xlabel('Time');
title('Open-loop Step Response');

% Poles and zeros
poles = pole(P_pitch);
zeros = zero(P_pitch);
disp('Poles:');
disp(poles);
disp('Zeros:');
disp(zeros);