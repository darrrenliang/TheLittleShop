# TheLittleShop
This is a self-study project for practicing OOP concept.

## Description
1. Build a CLI (command line interface) application, which should take input on STDIN and post output on STDOUT.
2. A marketplace platform which allows users to ‘buy’ and ‘sell’ items.

## Requirements

### User
-	Anyone who uses the marketplace
-	Identified by username, which should be unique throughout the platform, but case insensitive.
-	Each user can create any number of listings having any category.

### Listing
#### A listing of an item put up for sale on the marketplace. Only registered users should be allowed to buy or sell items.
#### Listings should have the following fields:
-	Title
-	Description
-	Price
-	Username
-	Creation time
-	Each listing can be associated with only 1 user and 1 category.

### Category
-	Groupings of listings of the same "category". E.g. Electronics, Fashion etc
-	Category reads can be sorted on Price or creation time.

