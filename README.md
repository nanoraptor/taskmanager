# Task Manager

A simple and fast CLI based Task tracker that will convert and organize your tasks into a map that you could chase.

#### ***<b>This is a work in progress. so, some functionalities may not be available</b>***

#### <b> Currently it can do these:</b>

+ add tasks
+ update tasks
+ list tasks
+ delete tasks

#### <b>Usage:</b>

<p>
  <p>You can see the usage by typing 'help'</p>
  <p>To add a task: go into add mode and type the name of the task</p>
  <p>To delete a task: go into delete mode and enter the id of the task</p>
  <p>To update a task: go into update mode and enter the id of the task followed by the updated task name</p>
  <p>To list a task: go into list mode</p>
</p>

#### <b>Storage Format:</b>
>
> All your tasks are saved locally in a .JSON file. You can configure the location of the .JSON file and also change it manually by reading the docs if you want to.

<p>It stores the tasks in the preferred .json file.
</p>
<p>Each task is assigned with a unique id</p>
<p>Each line in the .json file contains: "unique_id _ task_name"</p>
<p>** Note that each line ends with a newline character</p>
