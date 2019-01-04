#include <stdlib.h>
#include <stdio.h>


int* append(int* array, int arrayLength, int arrayCon, int elementToBeAdded) {
   if (arrayLength == arrayCon){
      //printf("if statement ran.");
      int* newArray;
      newArray = (int*)malloc(sizeof(int)*(arrayLength + 5));
      int i;

      for (i=0; i <= arrayCon; i++){

         newArray[i] = array[i];

         //printf("for statement ran %i", i);
      }
      //printf("%i", *array);
      //printf("%i", *newArray);

      newArray[i] = elementToBeAdded;
      //arrayCon ++;
      arrayLength += 5;
      free(array);
      return newArray;

   }else{
      array[arrayCon] = elementToBeAdded;
      //arrayCon ++;
      return array;
   }


}

int main(int argc, char *argv[]) {
  int maxIters;
  sscanf(argv[1], "%d", &maxIters); //store the first argument as maxIters
  srand(maxIters); //seed the random number generator with maxIters
  int debug=0;
  if (argc>2) //if there is a second argument (no matter what it is), make "debug" 1
    debug=1;

  int arrayLength=5; //array starts off size 5
  int arrayCon=0; //the number of characters contained in the array
  int* array=(int*)malloc(sizeof(int)*arrayLength); //allocate that much space

  int i;
  for(i=0; i < maxIters; i++) {
    int aRandomNum = rand(); //get a random number

    array=append(array, arrayLength, arrayCon, aRandomNum);
    arrayCon++; //We added an element to the array so update accordingly
    //arrayLength+5; //The array is now 5 bigger, so update variable//this might go in the append function instead

    //if we had a second argument, print out the current contents of the array
    if (debug) {
      int j;
      for (j=0; j<arrayLength; j++)
        printf("%i ",array[j]);
      printf("\n");
    }
  }
  free(array); //we're done with the array, so free it
  return 0;
}
