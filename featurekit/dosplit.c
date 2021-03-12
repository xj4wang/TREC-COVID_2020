#include <stdio.h>

char buf[500000];
char x[1000];
int n;
FILE *f;

main(){
   for(n=0;gets(buf);n++) {
      if (n%50000 == 0) {
         if (f) fclose(f);
         sprintf(x,"svm.test.%03d",n/50000);
         f = fopen(x,"w");
         if (!f) {perror(x); exit(1); }
      }
      fprintf(f,"%s\n",buf);
   }
}
