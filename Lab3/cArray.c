#include <stdlib.h>
#include <stdio.h>

/**
 * append() takes in a pointer to an array, the length of that array, and the
 * element to be added to the array.  In cArray, we can assume the array is
 * already full of integers, necessitating a new array which is one bigger, to
 * be filled with all the old integers, and then the new element added.  The
 * old array should be freed, and the pointer to the new array returned.
 */
int* append(int* array, int arrayLength, int elementToBeAdded) {
   int* newArray = (int*)malloc((sizeof(int)) * (arrayLength + 1));
   int i;
   for (i=0; (i < arrayLength); i++){
      newArray[i] = array[i];
   }
   newArray[i] = elementToBeAdded;

   free(array);
   return newArray;
}

int main(int argc, char *argv[]) {
  int maxIters;
  sscanf(argv[1], "%d", &maxIters); //store the first argument as maxIters
  srand(maxIters); //seed the random number generator with maxIters
  int debug=0;
  if (argc>2) //if there is a second argument (no matter what it is), make "debug" 1
    debug=1;

  int arrayLength=0; //array starts off size 0
  int* array=(int*)malloc(sizeof(int)*arrayLength); //allocate that much space

  int i;
  for(i=0; i < maxIters; i++) {
    int aRandomNum = rand(); //get a random number
    //replace the array with the new array which is one bigger by calling
    //append()
    array=append(array,arrayLength,aRandomNum);
    arrayLength++; //The array is now 1 bigger, so update variable

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
