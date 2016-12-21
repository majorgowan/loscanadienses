get_sugg <- function(transac, rules) {
  sugg <- NULL
  ncodpers <- rownames(as(transac,"matrix"))
  lhs <- rules@lhs
  rhs <- rules@rhs
  for (i in 1:length(lhs)) {
    if (has_rule(transac,lhs[i])) {
      sugg <- rbind(sugg,as(rhs[i],"matrix"))
    }
  }
  cs <- colSums(sugg)
  return(paste(ncodpers, 
               paste(names(cs)[order(cs,decreasing=T)],collapse=' '),
               sep=','))
}

all_sugg_to_file <- function(trans, rules, myfile) {
  fileConn <- file(myfile, "w")
  write('ncodpers,added_products',fileConn)
  ntrans <- length(trans)
  for (i in 1:ntrans) {
    sugg <- get_sugg(trans[i],rules)
    write(sugg,fileConn,append=TRUE)
  }
  close(fileConn)
}

all_sugg_to_df <- function(trans, rules) {
  suggs <- NULL
  ntrans <- length(trans)
  for (i in 1:ntrans) {
    sugg <- get_sugg(trans[i],rules)
    suggs <- c(suggs,sugg)
  }
  return(data.frame(ncodpers=suggs))
}


has_rule <- function(transac, lhs) {
  rrr <- as(lhs,"matrix")
  ttt <- as(transac,"matrix")
  for (i in 1:length(ttt)) {
    if (rrr[i]) {
      if (!ttt[i]) {
        return(FALSE)
      }
    }
  }
  return(TRUE)
}