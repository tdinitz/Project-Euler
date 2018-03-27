primes=nthPrime(50); %this was manually selected to work for this problem
n=1000;
primes=primes(primes<n); primes=primes(3:end); %cut off 2, 3
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
for i=1:length(cyclics)
    if orders(i) > max
        max=orders(i)
        answer=cyclics(i)
    end
    for j=(i+1):length(cyclics)
        if cyclics(i)*cyclics(j)>n
            break
        end
        %if lcm(cyclics(i)-1,cyclics(j)-1)>max
        if lcm(orders(j),orders(i))>max
            %max=lcm(cyclics(i)-1,cyclics(j)-1);
            max=lcm(orders(j),orders(i))
            answer=cyclics(i)*cyclics(j)
        end
        for k=(j+1):length(cyclics)
            if cyclics(i)*cyclics(j)*cyclics(k)>n
                break
            end
            if lcm(lcm(orders(j),orders(i)),orders(k))>max
                %max=lcm(cyclics(i)-1,cyclics(j)-1);
                max=lcm(lcm(orders(j),orders(i)),orders(k))
                answer=cyclics(i)*cyclics(j)*cyclics(k)
            end
            for h=(k+1):length(cyclics)
                if cyclics(i)*cyclics(j)*cyclics(k)*cyclics(h)>n
                    break
                end
                if lcm(lcm(lcm(orders(j),orders(i)),orders(k)),orders(h))>max
                    %max=lcm(cyclics(i)-1,cyclics(j)-1);
                    max=lcm(lcm(lcm(orders(j),orders(i)),orders(k)),orders(h))
                    answer=cyclics(i)*cyclics(j)*cyclics(k)*cyclics(h)
                end
            end
        end
    end
end

