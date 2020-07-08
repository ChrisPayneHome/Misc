n <- 1:100
print(n)


for(i in n){
	if((i %% 3 == 0) & (i %% 5 == 0)){
		replace(i, n, print("Fizzbuzz"))}
	else if(i %% 3 == 0){
		replace(i, n, print("Fizz"))}
	else if(i %% 5 == 0){
		replace(i, n, print("Buzz"))}
	else{
		print(i)}	
}