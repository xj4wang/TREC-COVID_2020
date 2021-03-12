#include <time.h>
#include <stdio.h>
#include <stdlib.h>

char buf[1000000];
int main(int argc, char **argv) {
   int N = atoi(argv[1]);
   int n = atoi(argv[2]);
   char *v = calloc(N,1);
   time_t t = time(&t);
   srand(t);
   int i;
   for (i=0;i<n;i++) v[rand()%N]=1;
   for (i=0;gets(buf);i++) {
      if (v[i]) printf("%s\n",buf);
   }
}
