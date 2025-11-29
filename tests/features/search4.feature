Feature: Search4
 Given I open the Rozetka home page
 When I search for 'Iphone 16'
 When I sort products by price 'asc'
 Then should sort products by price 'asc'
