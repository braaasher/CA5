add <- function(x,y) {
  return(x+y)
}
subtract <- function(x,y) {
  return(x-y)
}
multiply <- function(x,y) {
  return(x*y)
}
divide <- function(x,y) {
  return(x/y)
}
square <- function(x) {
  return(x^2)
}
cube <- function(x) {
  return(x^3)
}
expon <- function(x,y) {
  return(x^y)
}
squareroot <- function(x) {
  return(sqrt(x))
}
pi <- function(x) {
  return(x*3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745)
}
factorial <- function(x) {
    if (x == 0) return (1)
    else  return (x * factorial(x-1))
}


