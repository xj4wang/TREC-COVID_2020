#include <stdio.h>
#include <stdlib.h>

char a[1024], b[2014];
int main(int argc, char **argv){
   int N = 4*1024*1024;
   int n;
   float *p = malloc(N*sizeof(float));
   FILE *model = fopen(argv[1],"r");
   if (argc == 3) freopen(argv[2],"r",stdin);
   for (n=0;1 == fscanf(model,"%g",p+n);n++) {
      if (n+1 >= N) {
         N*=2;
         p = realloc(p,N*sizeof(float));
      }
   }
   //printf("n %d\n",n);
   float w = 0;
   int i;
   float x;
   while (1) {
      fread(&i,sizeof(int),1,stdin);
      if (i == -1) {
         printf("%0.7f\n",w);
         w = 0;
         if (!fread(&i,sizeof(int),1,stdin)) break;
      }
      fread(&x,sizeof(float),1,stdin);
      //printf("%d %f\n",i,x);
      w += x * p[i];
   }
}
