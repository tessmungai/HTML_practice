import 'dart:io';

void main() {
  try {
    stdout.write("Enter a number: ");
    String input = stdin.readLineSync()!;
    int number = int.parse(input);

    if (number > 10) {
      print("Your number is greater than 10");
    } else if (number < 10) {
      print("Your number is less than 10");
    } else {
      print("Your number is equal to 10");
    }
  } on FormatException catch (e) {
    print("Error: Please enter a valid number. ($e)");
  }
}