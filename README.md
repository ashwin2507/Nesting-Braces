# Nesting-Braces
Programming Languages:
Nesting Depth Braces: 
Write a program that will take an input file called input.txt which will contain a Java program and parse it and output an annotated version.
Your program will track the nesting depth of the braces of the input file and will output an annotated version of the file. 
Your final program will
1. List the nesting depth of curly braces
2. Ignore braces inside quotes or comments

Handle block comments that cross multiple lines of the input file.
/* comment with 
ignored brace { */

Sample INPUT:
-------------------
import blah;
class Foo
{
void Foo()
{
System.out.println("braces are fun! {{{{{"); // ignored
if (condition)
{
// also ignored: { 
int a = 1;
// as is this: }
}
}
} 
//end of program 

Sample annotated OUTPUT:
-------------
0 import blah;
0 class Foo
1 {
1    void Foo()
2    {
2        System.out.println("braces are fun! {{{{{"); // ignored
2        if (condition)
3        {
3            // also ignored: { 
3            int a = 1;
3            // as is this: }
3        }
2    }
1 }
0 // end of program 
