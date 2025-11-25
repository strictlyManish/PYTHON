const f = (n) =>{
    fact = 1;

    for(let i = 1;i<=n;i++){
        fact *= i
    }

    return fact
};


console.log(f(5))