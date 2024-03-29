# book-club
A social media app in which different users all over the world can discuss certain topics or ideas about books. 

This web app isn't necessarily limited to books as the user can create whatever discussion they choose to but for the sake of themes I chose to create a discussion center around books.

# Creation

This app was created using primarily Python and the Django back-end web-framework. 

Other frontend markup like HTML, CSS and JavaScript was also used whenever convenient or necessary.

Using Django Models and the built in db.sqlite database, a table was created to hold data for each indivudal user, each chat-room any specific user creates and each book any specific user has read.

Using Django views and modelforms, various CRUD functionality was added in which users could create, edit, remove or update any chat-room or book they wish.

Using Python/Django channels and web-sockets, consumers were created to set the general logic of the chat-room and creating an asynchronous chat-room. Users would connect to each room, recieve messages from the frontend as well as send messages to the frontend and then eventually disconnect when they choose to.

All messages are stored in the database using the database_sync_to_async() function. This can be seen by the superuser in the Django Admin panel.

JavaScript was used to recieve and send the messages from the frontend. HTML, CSS and Bootstrap was used to design the overrall layout of the webapp.
