A = imread("image.png");

X = [1,0,-1;2,0,-2;1,0,-1];
Y = [1,2,1;0,0,0;-1,-2,-1];

G_x = conv2(X, rgb2gray(A));
G_y = conv2(Y, rgb2gray(A));
G = sqrt(G_x.^2 + G_y.^2);
G = uint8(G);

figure;
subplot(1,2,1);
imshow(A)
title("Original Image");
subplot(1,2,2);
imshow(G);
title("Filtered Image");
