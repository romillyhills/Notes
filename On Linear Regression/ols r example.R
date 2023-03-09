x<-c(0,1,2,3,4,5,6,7,8,9)
y<-c(6.95,5.22,6.36,7.03,9.71,9.67,10.69,13.85,13.21,14.82)
top<-x
bottom<-x
errors<-x #residual
xbar=mean(x)
ybar=mean(y)
for(i in 1:10){
  top[i]=(x[i]-xbar)*(y[i]-ybar)
  bottom[i]=(x[i]-xbar)^2
}
beta<-sum(top)/sum(bottom)
beta
alpha<-ybar-beta*xbar
alpha
for(i in 1:10){
  errors[i]=y[i]-alpha-beta*x[i]
}
errors
#check with built in linear model
lm(y ~ x)
