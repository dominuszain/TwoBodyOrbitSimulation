// code of zain ul abideen
clear; clc;

// setting trivial values for constants.
g = 1; m1 = 10; m2 = 10;

t = [0 : 0.01 : 150]

// setting up the differential equations.
function [dxdt]=f(t, x)
    dxdt = [x(5,:); x(6,:); x(7,:); x(8,:);
    g .* m2 .* (x(3,:) - x(1,:)) ./ (((x(3,:) - x(1,:)) .^ 2 + ((x(4,:) - x(2,:)) .^ 2))) .^ (3 ./ 2);
    g .* m2 .* (x(4,:) - x(2,:)) ./ (((x(3,:) - x(1,:)) .^ 2 + ((x(4,:) - x(2,:)) .^ 2))) .^ (3 ./ 2);
    g .* m1 .* (x(1,:) - x(3,:)) ./ (((x(3,:) - x(1,:)) .^ 2 + ((x(4,:) - x(2,:)) .^ 2))) .^ (3 ./ 2);
    g .* m1 .* (x(2,:) - x(4,:)) ./ (((x(3,:) - x(1,:)) .^ 2 + ((x(4,:) - x(2,:)) .^ 2))) .^ (3 ./ 2);]
endfunction

// setting up the initial conditions.
to = 0
xo = [0; 0; 10; 10; 1; 0.5; 1; 0]
// xo = [x1; y1; x2; y2; vx1; vy1; vx2; vy2]

// solving the differential equations.
x = ode(xo, to, t, f)

//scatter(x(1,:), x(2,:), 'o')
//scatter(x(3,:), x(4,:), 'x')

// multiple column vectors can be animated this way.
comet([x(1,:)', x(3,:)'], [x(2,:)', x(4,:)'])

// see relevant paper for more details.
