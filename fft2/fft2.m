clc;clear;
A = imread("pic1.png"); B = imread ("pic2.png");

fftA = fft2(A); magA = abs(fftA); phA = angle(fftA);
fftB = fft2(B); magB = abs(fftB); phB = angle(fftB);

nfftA = magA .* exp(1i*phB);
new_A = uint8(ifft2(nfftA));

nfftB = magB .* exp(1i*phA);
new_B = uint8(ifft2(nfftB));
figure;
subplot(2,2,1); imshow(A); title('pic1');
subplot(2,2,2); imshow(B); title('pic2');
subplot(2,2,3); imshow(new_A); title('|magA| ∠ phB');
subplot(2,2,4); imshow(new_B); title('|magB| ∠ PhA');
