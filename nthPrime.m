function num = nthPrime(n)

currentPrimes=[2,3,5];
modPrimes=[1,5];
imax=3;
max=6;

while length(currentPrimes)<n
    [X,Y]=meshgrid(max*[1:currentPrimes(imax)-1],modPrimes);
    posPrimes=X+Y;
    posPrimes=reshape(posPrimes,[1,prod(size(posPrimes))]);
    for i=1:length(posPrimes)
        if mod(posPrimes(i),currentPrimes(1:imax))
            modPrimes=[modPrimes,posPrimes(i)];
        end
        if mod(posPrimes(i),currentPrimes)
            currentPrimes=[currentPrimes,posPrimes(i)];
        end
    end
    %modPrimes=[1,currentPrimes(imax+1:end)];
    max=max*currentPrimes(imax);
    imax=imax+1;
end

num=currentPrimes;

end

