#include <stdio.h>
#include <time.h>

int main() {
    time_t current_time;
    struct tm *time_info;
    char time_string[9];  // To hold the time string (HH:MM:SS)

    time(&current_time);
    time_info = localtime(&current_time);

    strftime(time_string, sizeof(time_string), "%H:%M:%S", time_info);
    printf("Current time: %s\n", time_string);

    return 0;
}
