using namespace std;
#include <stdio.h>
#include <string.h>
#include <string>
#include <map>

float score;
char sent[1000], doc[1000];
map<string, float> x;
map<string, string> s;
int main(int argc, char **argv){
   while (2 == scanf("%*s%s%f",sent,&score)){
       strcpy(doc,sent);
       *strrchr(doc,'.')=0;
       if (x.find(doc) == x.end() || x[doc] < score) {
           x[doc] = score;
           s[doc] = sent;
       }
       //printf("%s %s %0.7f %0.7f\n",sent,doc,score,x[doc]);
   }
   for( map<string,float>::const_iterator it = x.begin(); it != x.end(); ++it ) {
       string key = it->first;
       float value = it->second;
       printf("%s\t%0.7lf\n",s[key].c_str(),value);
   }
}
