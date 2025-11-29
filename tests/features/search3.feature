Feature: Search3
 Given I open the Rozetka home page
 When I search for 'Iphone 17'
 When I sort products by price 'desc'
 Then should sort products by price 'desc'
