import 'package:http/http.dart' as http;
import 'package:html/parser.dart' as parser;
import 'package:html/dom.dart';

void main() {
  // Get user input for the search term
  print("Enter the search term: ");
  String searchTerm = stdin.readLineSync();

  // URL of the website to scrape
  final url = 'https://boycott.thewitness.news/search/$searchTerm';

  // Send a GET request to the URL
  http.get(Uri.parse(url)).then((response) {
    // Create a Document object to parse the HTML content
    Document document = parser.parse(response.body);

    // Find the relevant content within the HTML based on class name
    Element alertDiv = document.querySelector('.m-a5d60502.mantine-Alert-wrapper');

    // Check if the alertDiv exists
    if (alertDiv != null) {
      // Extract the text content of the alertDiv
      String resultMessage = alertDiv.text.trim();

      // Check if the specified string is present in the result message
      if (resultMessage.contains('We were unable to find anything for that search.')) {
        print('not boycott');
      } else {
        print('boycott');
      }
    } else {
      print('boycott');
    }
  });
}