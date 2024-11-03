# crowdfunding_back_end
A repo to contain my She Codes Crowdfunding back end project

## `README.md` Template Phase 1: API Plan

As your Crowdfunding back end grows, you'll have more and more information to put in the `readme.md` file. For now, you have a rough plan for your project, so let's mark it down!

Below is a template you can use to add your plan to your readme. As usual, {{ double brackets }} indicate places where you should insert your own content. So if your name was Sinead O'Connor, you would swap `Hi, my name is {{ your_name_here }}!` to `Hi, my name is Sinead O'Connor!`

If you're looking for a good way to create your Schema diagram in VS Code, check out [the draw.io integration extension for VS Code](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)!

To make editing tables in Markdown easier, you might enjoy [the Markdown All-In-One extension](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one). With this installed, you can hit tab inside of any "cell" in a table, and the editor will automatically resize all your columns and create a new row if necessary.

```markdown
# Crowdfunding Back End
{{ your name here }}

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------- | ------------ | --------------------- | ---------------------------- |
|     |             |         |         |              |                       |                              |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
```

An example API spec:  
![](./img/table.png)

ERD

User:

One-to-Many with Project: A user (kid) can create multiple projects.
One-to-Many with Pledge: A user can make multiple pledges on different projects.
One-to-Many with Comment: A user can comment on multiple projects.
One-to-Many with Notification: Each user can have multiple notifications.
Project:

Many-to-One with User: Each project has one creator (a user).
One-to-Many with Pledge: A project can receive multiple pledges from different users.
One-to-Many with Comment: A project can have multiple comments.
Many-to-Many with Category via ProjectCategory: A project can belong to multiple categories.
One-to-Many with Reward: A project can have multiple reward tiers.
Pledge:

Many-to-One with User: Each pledge is made by one user.
Many-to-One with Project: Each pledge is associated with one project.
Category:

Many-to-Many with Project via ProjectCategory: A category can contain multiple projects.
ProjectCategory:

Many-to-One with Project: Connects a project to a category.
Many-to-One with Category: Connects a category to a project.
Comment:

Many-to-One with User: Each comment is made by one user.
Many-to-One with Project: Each comment belongs to one project.
Reward:

Many-to-One with Project: Each reward belongs to one project.
Notification:

Many-to-One with User: Each notification is directed to one user.


REST API Endpoints
User Endpoints
    1. POST /api/users/register: Registers a new user.
    2. POST /api/users/login: Authenticates and logs in a user.
    3. GET /api/users/{user_id}/: Retrieves user profile details.
    4. PUT /api/users/{user_id}/: Updates user profile information.
Project Endpoints
    1. POST /api/projects/: Creates a new project. Only allowed if is_kid is True.
    2. GET /api/projects/: Lists all projects, with filters for category, funding status, etc.
    3. GET /api/projects/{project_id}/: Retrieves project details, including comments and pledges.
    4. PUT /api/projects/{project_id}/: Updates project details, only accessible to the project creator.
    5. DELETE /api/projects/{project_id}/: Deletes a project, only accessible to the creator or an admin.
Pledge Endpoints
    1. POST /api/projects/{project_id}/pledges/: Creates a new pledge for a project by a user.
    2. GET /api/projects/{project_id}/pledges/: Lists all pledges for a project.
    3. DELETE /api/projects/{project_id}/pledges/{pledge_id}/: Cancels a pledge (may depend on project status).
Category Endpoints
    1. GET /api/categories/: Lists all project categories.
    2. POST /api/categories/: Creates a new category (admin access).
    3. GET /api/categories/{category_id}/projects/: Lists all projects under a specific category.
Comment Endpoints
    1. POST /api/projects/{project_id}/comments/: Adds a new comment to a project.
    2. GET /api/projects/{project_id}/comments/: Lists all comments for a project.
    3. DELETE /api/comments/{comment_id}/: Deletes a comment (either by comment owner or project owner).
Reward Endpoints
    1. GET /api/projects/{project_id}/rewards/: Lists all rewards for a project.
    2. POST /api/projects/{project_id}/rewards/: Adds a new reward tier (creator access).
    3. DELETE /api/projects/{project_id}/rewards/{reward_id}/: Deletes a reward tier (creator access).
Notification Endpoints
    1. GET /api/users/{user_id}/notifications/: Lists all notifications for a user.
    2. PUT /api/notifications/{notification_id}/: Marks a notification as read.
