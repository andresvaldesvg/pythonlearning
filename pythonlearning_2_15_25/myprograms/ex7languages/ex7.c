#include <stdio.h>
#include <string.h>

int main() {
    char favorite_food[50];

    printf("What is your favorite food? ");
    fgets(favorite_food, 50, stdin);
    favorite_food[strcspn(favorite_food, "\n")] = 0; // Remove newline character

    if (strcmp(favorite_food, "Rice Pudding") == 0) {
        printf("Yes so nice!\n");
    } else {
        printf("Yuck!\n");
    }

    printf("Thanks for playing.\n");
    return 0;
}
