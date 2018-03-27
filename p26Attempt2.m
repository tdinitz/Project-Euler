primes=nthPrime(50); %this was manually selected to work for this problem
n=1000;
primes=primes(primes<n); primes=primes(1:end); %cut off 2, 3
cyclics=[]; order=1; orders=[];
for i=1:length(primes)
    current_mod=1;
    for j=1:(primes(i)-1)
        current_mod=mod(current_mod*10,primes(i));
        if current_mod==1
            order=j;
            break
        end
    end
    cyclics=[cyclics;primes(i)];
    orders=[orders;order];
    %if order==(primes(i)-1)
    %    cyclics=[cyclics;primes(i)];
    %end
end
max=0;
answer=0;
%maybe just go through manually
for i=2:n
    prime_factors=factor(i);
    orderNew=zeros(1,length(prime_factors));
    for j=1:length(prime_factors)
        orderNew(j)=orders(find(primes==prime_factors(j)));
    end
    fullOrder=orderNew(1);
    for k=1:length(prime_factors)-1
        fullOrder=lcm(fullOrder,orderNew(k+1));
    end
    if fullOrder>max
        max=fullOrder
        answer=i
    end
end