using namespace std;
#include <stdio.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <assert.h>

#define ALPHA 1.0
#define BETA .0
#define GAMMA 0.

float score;
char sent[1000], doc[1000];
vector<pair <float,string> > x;
char cur[1000];
FILE *f;
int main(int argc, char **argv){
   if (argc == 2) f = fopen(argv[1],"r");
   while (2 == scanf("%*s%s%f",sent,&score)){
       strcpy(doc,sent);
       *strrchr(doc,'.')=0;
       if (strcmp(doc,cur)) {
          //printf("was %s is %s\n",cur,doc);
          int i;
          float sum = 0, w=1;
          sort(x.rbegin(),x.rend());
          for (i=0;i<x.size();i++) {
             sum += w * x[i].first;
             w *= GAMMA;
          }
          if (*cur) {
             float z;
             char d[1000];
             fscanf(f,"%*s%s%f",d,&z);
             if (strcmp(d,cur)) fprintf(stderr,"d %s doc %s\n",d,cur);
             assert(!strcmp(d,cur));
             //printf("f %p z %g\n",f,z);
             printf("%s\t%0.7f\n",x.begin()->second.c_str(),ALPHA*sum+BETA*z);
          }
          x.clear();
          strcpy(cur,doc);
       }
       x.push_back(pair<float,string>(score,sent));
   }
          int i;
          float sum = 0, w=1;
          sort(x.rbegin(),x.rend());
          for (i=0; i<x.size();i++) {
             sum += w * x[i].first;
             w *= GAMMA;
          }
          if (*cur) {
             float z;
             char d[1000];
             fscanf(f,"%*s%s%f",d,&z);
             if (strcmp(d,cur)) fprintf(stderr,"d %s doc %s\n",d,cur);
             assert(!strcmp(d,cur));
             //printf("f %p z %g\n",f,z);
             printf("%s\t%0.7f\n",x.begin()->second.c_str(),ALPHA*sum+BETA*z);
          }
}
