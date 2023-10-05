Name: Kanishk Singh
ID: SE21UCAM005
Branch: Computation and Mathematics

Note: 
1. To run the executable, go to executable folder and run it as ./procc2 or ./procc2 --1 , here 1 can replace any time period

2.The Program has been wtitten in Rust Programming Language. To view the source code go into procc2/src/ there is the sourcecode in main.rs
To compile the program themselves evaluator needs to install "Cargo" on their system and then use "cargo run" or "cargo run --1" in the procc2 folder

However an executable has been provided in a sperate folder for the evaluators convinience

Reasons for choosing Rust Programming language for this project:
As we have learnt that /proc file system holds very crucial information about the system and while manipulating files here we have to be careful,
Now we as humans can be careful because we know where the sensetive data is, But a program is indiscriminant, On many occasions languages like C/C++
access data which they are not supposed to which can be fatal for the program in some cases. That is why I have used Rust, it is a low level system Programming
language which is famous for its memory safety, it can't access memory locations which haven't been explicitly programmed, The advance error handling also helps in
debugging the code while the unique handling of variable made this language a suitable choice for this project.
