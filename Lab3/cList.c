#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int arrayLength = 5;

int* append(int* array, int arrayChar, int elementToBeAdded) {
	if (arrayLength == arrayChar){

		int* newArray;
		newArray = (int*)malloc((arrayLength * 2)*sizeof(int));
		int i;

		for (i=0; i < arrayChar; i++){
			newArray[i] = array[i];
		}
		newArray[i] = elementToBeAdded;
		arrayLength = arrayLength *2;

		free(array);
		return newArray;

	} else{
		array[arrayChar] = elementToBeAdded;
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
	int arrayChar=0; //the number of characters contained in the array
	int* array=(int*)malloc(sizeof(int)*arrayLength); //allocate that much space

	int i;
	for(i=0; i < maxIters; i++) {

		int aRandomNum = rand(); //get a random number

		array=append(array, arrayChar, aRandomNum);
		arrayChar++;

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
