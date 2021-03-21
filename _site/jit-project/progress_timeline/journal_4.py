from _generate_site.elements import *

page = Page("jit-project/progress-timeline/journal-4.html",
            nav_loc=["JIT Project", "Progress Timeline", "[8] Journal 4"])

page += Title("Journal 4: Weeks 14-15")

page += Paragraph("February 27, 2021 - March 20, 2021")

page += Heading('Goals for this Journal:')
page += OrderedList([
    Paragraph("Make Parameters and Branches work"),
    Paragraph("Generate said Parameters and Branches"),
    Paragraph("Implement If-statements"),
    Paragraph("Implement Comparisons"),
    Paragraph("Implement Blocks"),
    Paragraph("Implement While-statements"),
    Paragraph(f"Create Instruction Emission Optimizations for everything implemented over these two weeks, like {inline_code('xor rax, rax')} over {inline_code('mov rax, 0')}"),
])

page += Heading("Research")

page += Paragraphs(f"""
{bold("Note: all references labelled at the bottom.")}
{bold("Note: I used code snippets instead of screenshots because this is a programming project.")}
{bold("Note: I used pseudocode instead of actual C for the sake of clarity.")}

These were the weeks focused on {bold('control-flow')}. The subject of this journal, therefore, will be branches, comparison,
and loops.

The essence of control-flow is dynamically choosing what code runs based on the state of the program. It sounds fancy,
but it's essentially just if-statements and loops. The if-statement is one fundamental example of control flow:
""")

page += Code("""
if (a > b) {
    foo();
} else {
    bar();
}
""")

page += Paragraphs(f"""
The program in this example can take two paths once it reaches the if-statement. It can either execute 'foo', or it can
execute 'bar'. When the program reaches {inline_code('if (a > b)')}, it dynamically chooses between the first or second path,
depending on whether 'a' is greater than 'b' or not. In other words, the if-statement controls the flow of the program between
two different paths.

The other fundamental control-flow pattern is the while-statement, or while-loop:
""")

page += Code("""
while (a < b) {
    a = a + 1;
}
""")

page += Paragraphs(f"""
For as long as {inline_code('a < b')}, 1 will be added to a. The while-statement directs the flow of the program into the body
of the loop, the {inline_code('{ a = a + 1; }')}, for as long as the condition is true. 

From these two patterns, most other common forms of control-flow can be built. The normal switch statement, with {inline_code('break')}s
after every case:
""")

page += Code("""
switch (a) {
    case 1: {
        print("a is 1");
        break;
    }
    case 2: {
        print("a is 2");
        break;
    }
    default: {
        print("a is something other than 1 or two");
        break;
    }
}
""")

page += Paragraphs(f"""
Such a form could be rewritten as a series of nested if-statements:
""")

page += Code("""
if (a == 1) {
    print("a is 1");
} else {
    if (a == 2) {
        print("a is 1");        
    } else {
        print("a is something other than 1 or two");
    }
}
""")

page += Paragraphs(f"""
The regular for-statement: 
""")

page += Code("""
for (i = 25; i >= 0; i = i - 1) {
    print(i + " seconds left");
}
""")

page += Paragraphs(f"""
This could be replace with the following: 
""")

page += Code("""
i = 25
while (i >= 0) {
    print(i + " seconds left");
    i = i - 1;
}
""")

page += Paragraphs(f"""
in fact, the while statement can be replaced if you use the more primitive goto-statement. The above could be replaced with: 
""")

page += Code("""
i = 25
label cond:
if (i >= 0) {
    print(i + " seconds left");
    i = i - 1;
    goto cond;
} else {
    goto after;
}
label after:
""")

page += Paragraphs(f"""
The goto does exactly what it looks like it does, immediately move the program to corresponding label. Thus, by carefully placing
those goto's, we can create loops, especially by jumping with a goto to a point where the code will naturally return to that same
goto.

But we can do even better. A conditional goto (which only jumps if it's condition it true) could replace all if-statements:
""")

page += Code("""
i = 25
cond = i >= 0
goto after if cond;
label cond:
print(i + " seconds left");
i = i - 1;
goto cond;
label after:
""")

page += Paragraphs(f"""
I've shown that you can reduce for-loops and switch-statements to if-statements and while-loops. I've also shown
that if-statements and while-loops can be reduced to regular and conditional goto's. Therefore, we can reduce for-loops and
switch-statements, and indeed all higher control-flow forms, into the dead simple goto. 

CPU's are designed to be simple in both operation and function. Therefore, there is no direct support for advanced control
flow in assembly. If you want to make an if-statement, you'll have to make it out of goto's. The bulk of my work for 
this period is figuring out how to do reduce advanced control-flow forms into goto's efficiently.

The basis of the system I devised is the concept of "basic blocks", or blocks for short. I did not come up with this term,
rather, I learned of it while researching about SSA form, because blocks are an essential component of SSA form. See the 
reference on LLVMLite for the actual source.

The essence of a block is that it breaks down program flow into its most basic pieces. Code will always start at the top
of a basic block, will always go all the way through in one specific path, and at the end will choose a new basic block to
go to. Additionally, within a basic block, SSA rules must be followed: all values must have a single, defined point of origin.
Let's review what doesn't qualify as valid SSA first:  
""")

page += Code("""
%a = 0 > 1      // assign the true/false value of whether 0 is greater than 1 to the value "a"
%b = 5
%c = 7
%d = %a ? %b : %c   // This is a ternary operator. It'll set %d to %b if %a is true, otherwise it'll set %d to %c (see sources). 
                    // It is illegal because there are two paths to take, either %d = %b or %d = %c   
%c = %a        // illegal because in SSA, you can't reassign a value. Rather, just make a new one with a different name
""")

page += Paragraphs(f"""
Now that we've reviewed that, I can show how we can reduce higher control-flow forms into a basic-block based system.
The following examples will be using almost exactly the same system that I have implemented into my actual code. 
We start with the following code that uses a for-loop to determine whether k is prime: 
""")

page += Code("""
k = 27;
is_prime = true;
for (i = 2; i < k; i++) {
    if (k % i == 0) {
        // btw, the % operator is the modulus operator
        // it'll calculate the remainder when k is divided by i
        // so if k is 7 and i is 2, k % i will be 1.
        // if the modulus is 0, that means that k divides evenly with i       
        is_prime = false;
    }
}
""")

page += Paragraphs(f"""
As I've demonstrated before, we can replace the for-loop with a while-loop. 
""")

page += Code("""
k = 27;
is_prime = true;
i = 2
while (i < k) {
    if (k % i == 0) {       
        is_prime = false;
    }
    i++;
}
""")

page += Paragraphs(f"""
Then we replace the while-loops and if-statements with the equivalent goto's and conditional goto's.  
""")

page += Code("""
k = 27;
is_prime = true;
i = 2
label start;
while_cond = i < k;
goto after_while if while_cond;
mod = k % i;
if_cond = mod != 0;
goto after_if if if_cond;        
is_prime = false;
label after_if:
i++;
goto start;
label after_while;
""")

page += Paragraphs(f"""
We've reached a problem in our quest to convert this for-loop into SSA form. Variables are being assigned multiple times,
and all the goto's make it hard to figure out how to replace variable reassignments with new variables. (Additionally, it
would be impossible to do so because variables are being reassigned an indeterminate number of times. We would have to actually
execute the program to figure out how many times we would have to reassign 'is_prime', for example.)

Let's try a new approach. We start off in a block called "entry". Whenever we reach a point where the program flow could take
multiple paths, we create multiple new blocks, and tell our current block to choose between the new blocks. I'll explain what I 
mean with a simpler example:  
""")

page += Code("""
a = 7;
if (a < 0) {
    print("a is negative");
} else {
    print("a is positive");
}
b = a + 3;
""")

page += Paragraphs(f"""
We start off working in the entry block, and generate the {inline_code('a = 7;')} in that block. 
""")

page += Code("""
block @"entry" {
    %a = int64 7;   // int32 means signed 64 bit integer (uint64 would be unsigned). 
}
""")

page += Paragraphs(f"""
We then reach the if-statement and its split. First, we generate the condition:  
""")

page += Code("""
block @"entry" {
    %a = int64 7;
    %temporary_cond = lt a, 0;   // lt means less than ('<'). 
}
""")

page += Paragraphs(f"""
Then we create 3 new blocks. One is what we execute if the condition is true, one if what we execute when the condition is
false, and the final one is what we come back to after the if-statement. Remember, we cannot jump out of the middle of a 
basic block, so the stuff which comes after an if-statement must be in a new block.   
""")

page += Code("""
block @"entry" {
    %a = int64 7;
    %temporary_cond = lt a, 0;   // lt means less than ('<'). 
}

block @"if_true" {
}

block @"if_false" { 
}

block @"after_if" {
}
""")

page += Paragraphs(f"""
We tell the entry block that it must conditionally branch to if_true if %temporary_cond is true, and if_false otherwise.
We call this final instruction a "terminator" because it terminates a block. A terminator must be some form of branch
to a new block, or a return instruction.   
""")

page += Code("""
block @"entry" {
    %a = int64 7;
    %temporary_cond = lt a, 0;   // lt means less than ('<'). 
} then cbranch(%temporary_cond) {true: @"if_true", false: @"if_false"); // cbranch stands for conditional branch

block @"if_true" {
}

block @"if_false" {     
}

block @"after_if" {
}
""")

page += Paragraphs(f"""
We then visit each branch of the if-statement in turn, and generate the appropriate code.   
""")

page += Code("""
block @"entry" {
    %a = int64 7;
    %temporary_cond = lt a, 0;   // lt means less than ('<'). 
} then cbranch(%temporary_cond) {true: @"if_true", false: @"if_false");

block @"if_true" {
    print("a is negative");
}

block @"if_false" { 
    print("a is positive");
}

block @"after_if" {
}
""")

page += Paragraphs(f"""
We must then terminate those two blocks. We know that each will go to after_if, so we can just emit a regular,
unconditional branch.   
""")

page += Code("""
block @"entry" {
    %a = int64 7;
    %temporary_cond = lt a, 0;   // lt means less than ('<'). 
} then cbranch(%temporary_cond) {true: @"if_true", false: @"if_false");

block @"if_true" {
    print("a is negative");
} then branch @"after_if";

block @"if_false" { 
    print("a is positive");
} then branch @"after_if";

block @"after_if" {
}
""")

page += Paragraphs(f"""
Finally, we can generate the code in the after_if.
""")

page += Code("""
block @"entry" {
    %a = int64 7;
    %temporary_cond = lt a, 0;   // lt means less than ('<'). 
} then cbranch(%temporary_cond) {true: @"if_true", false: @"if_false");

block @"if_true" {
    print("a is negative");
} then branch @"after_if";

block @"if_false" { 
    print("a is positive");
} then branch @"after_if";

block @"after_if" {
    %b = $a + 3;
}
""")

page += Paragraphs(f"""
This example demonstrates the principles of breaking control-flow into basic blocks. To make this a loop, all some code has
to do is make one of the branches point to an earlier block which will lead back to the branch. But what if we want variables
which could have different values? Like in this example: 
""")

page += Code("""
a = 7;
if (a < 0) {
    b = 3;
} else {
    b = 4;
}
c = a + b;
""")

page += Paragraphs(f"""
In normal SSA code, we'd use something called a phi instruction (from LLVMLite). A phi instruction is what gets around the
limitation of SSA that each value can have only one definition, which is very annoying when we have an example like above
where the b in {inline_code('c = a + b;')} has two different definitions which we cannot choose from until the code runs.
The phi node for this b would take the form {inline_code('%b = phi {@if_true: %b.1, @if_false: %b.2}')} where %b.1 is the
b from {inline_code('b = 3')} while %b.2 is the b from {inline_code('b = 4')}. The phi node lets us choose which value to use
depending on which block we have come from.

However, phi nodes are pretty hard to generate on the fly. We need to use a somewhat complicated algorithm involving
a construction known as "dominance frontiers". However, this requires a separate pass over the generated IR, which takes
extra time. Therefore, I came up with a simpler, if less mathematically rigorous system which saves time and memory at the
expense of less precisely defined IR. I think this a good trade off.

The two most important parts of my system are BlockParameter instructions and that I keep track of what values
each variable is currently in. Let's reduce the above code example to my system's block system.

Like before, we generate the stuff before the if-statement and the condition into the first block, and generate the 3 other blocks.
Additionally, whenever we generate a value, we keep track of what variable it would be assigned to in the actual program,
if it is in one.   
""")

page += Code("""
block @"entry" {
    %a ("a") = int64 7;               // the ("a") tells us that %a stores the variable "a"
    %temporary_cond (none) = lt a, 0; // the (none) tells us that %temporary_cond doesn't have a variable associated
}

block @"if_true" {
}

block @"if_false" {     
}

block @"after_if" {
}
""")

page += Paragraphs(f"""
Like before, we generate a cbranch. However, this time, we do a lot of extra work for it with the following code 
({hyperlink('link to code in repo', 'https://github.com/Totillity/ojit/blob/78a9481e51de6525829808f924285e06bb3d74ab/asm_ir_builders.c#L184')}):
""")

page += Code("""
void merge_blocks(IRBuilder* builder, struct BlockIR* to, struct BlockIR* from) {
    if (to->has_vars) {
        FOREACH_INSTR(curr_instr, to->first_instrs) {
            if (curr_instr->base.id == ID_BLOCK_PARAMETER_IR) {
                struct ParameterIR* param = &curr_instr->ir_parameter;
                if (param->var_name == NULL) continue;
                IRValue arg;
                if (!hash_table_get(&from->variables, STRING_KEY(param->var_name), (uint64_t*) &arg)){
                    param->var_name = NULL;
                } else {
                    INC_INSTR(arg);
                }
            } else {
                break;
            }
        }
    } else {
        struct BlockIR* original_block = builder->current_block;
        builder_temp_swap_block(builder, to);
        TableEntry* curr_entry = from->variables.last_entry;
        while (curr_entry) {
            builder_add_parameter(builder, curr_entry->key.cmp_obj);
            IRValue arg = (void*) curr_entry->value;
            INC_INSTR(arg);
            curr_entry = curr_entry->prev;
        }
        builder_temp_swap_block(builder, original_block);
        to->has_vars = true;
    }
}
""")

page += Paragraphs(f"""
Essentially, if the block has never been branched to before, we generate a BlockParameter instruction in it for every variable
in the originating block. Therefore, for blocks if_true and if_false, we'd generate: 
""")

page += Code("""
block @"entry" {
    %a ("a") = int64 7;              
    %temporary_cond (none) = lt a, 0; 
} then cbranch(%temporary_cond) {true: @"if_true", false: @"if_false"); 

block @"if_true" {
    %a.1 ("a") = parameter "a"
}

block @"if_false" {
    %a.2 ("a") = parameter "a"
}

block @"after_if" {
}
""")

page += Paragraphs(f"""
Now it's time to create the two blocks' terminators. Each is still an unconditional branch to after_if like before,
but when if_false generates its branch, the merge_block function I showed above notices that it isn't the first block
which branches to after_if (if_true is the first). Therefore, it deactivates any parameters which have already been generated
in after_if which aren't variables in if_false. This behavior isn't used here, but is needed whenever two alternate paths
generate differently named variables. In that case, we don't want the code which comes after the two paths to be able to
refer to variables which are only defined in one branch, because we didn't necessarily take that branch when the code is actually
executed. 

Anyways, here's the new code. We still just keep a and b in after_if.
""")

page += Code("""
block @"entry" {
    %a.0 ("a") = int64 7;              
    %temporary_cond (none) = lt a.0, 0; 
} then cbranch(%temporary_cond) {true: @"if_true", false: @"if_false"); 

block @"if_true" {
    %a.1 ("a") = parameter "a"
    %b.1 ("b") = 3
} then branch @"after_if"

block @"if_false" {
    %a.2 ("a") = parameter "a"
    %b.2 ("b") = 4     
} then branch @"after_if"

block @"after_if" {
    %a.3 ("a") = parameter "a"
    %b.3 ("b") = parameter "b"
    %c.0 ("c") = %a.3 + %b.3
}
""")

page += Paragraphs(f"""
When we generate code, all we have to do is ensure that a parameter always arrives in that block in a specific register
(for example, specific that %a.3 must always be in RAX). Then it's the branches' job to make sure that is actually the case.
The branches must look at the most recent definition of a particular variable (which is why we store the value's variables)
and tell that value it must be in the same register as the parameter.
Thus, we can use multiple definitions of variables in SSA form.

Don't worry, I haven't forgotten why I went on this whole tangent. Here's the sample we are trying to convert into block-based
IR, for your convenience:
""")

page += Code("""
k = 27;
is_prime = true;
for (i = 2; i < k; i++) {
    if (k % i == 0) {       
        is_prime = false;
    }
}
""")

page += Paragraphs(f"""
As I've shown before, we can convert it into a form with while-loops, which are much easier to use.
""")

page += Code("""
k = 27;
is_prime = true;
i = 2;
while (i < k) {
    if (k % i == 0) {
        is_prime = false;
    }
    i++;
}
""")

page += Paragraphs(f"""
Using our newfound knowledge of blocks, we can translate the sample into the following:
""")

page += Code("""
block @"entry" {
    %k.0 ("k") = int32 27;
    %is_prime.0 ("is_prime") = bool true;
    %i.0 ("i") = 2;
} then branch @"cond";

block @"cond" {
    %k.1 ("k") = parameter "k";
    %is_prime.1 ("is_prime") = parameter "is_prime";
    %i.1 ("i") = parameter "i";
    %.cond.0 = lt %i.1, %k.1;
} then cbranch(%.cond.0) {true: @"loop_body", false: @"after_loop"};

block @"loop_body" {
    %k.2 ("k") = parameter "k";
    %is_prime.2 ("is_prime") = parameter "is_prime";
    %i.2 ("i") = parameter "i";
    %.0 = mod %k.2, %i.2;
    %.cond.1 = eq %.0, int32 0;
} then cbranch(%.cond.1) {true: @"if_true", false: @"after_if"};
    
block @"if_true" {
    %k.3 ("k") = parameter "k";
    %is_prime.3 ("is_prime") = parameter "is_prime";
    %i.3 ("i") = parameter "i";
    %is_prime.4 = bool false;
} then branch @"after_if";

block @"after_if" {
    %k.4 ("k") = parameter "k";
    %is_prime.5 ("is_prime") = parameter "is_prime";
    %i.4 ("i") = parameter "i";
    %i.5 ("i") = add %i.4, int32 1;
} then branch @"cond";

block @"cond" {
    %k.5 ("k") = parameter "k";
    %is_prime.6 ("is_prime") = parameter "is_prime";
    %i.6 ("i") = parameter "i";
    
    ...
""")

page += Paragraphs(f"""
As I said before, now that we have this dead simple representation of the program, it is very easy to convert it into assembly.
We can simply generate the code for each block, string them into a line, and use the JMP instruction or the Jcc instruction
family to jump around.

Let's also go over conditionals real quick. In the x86 and x64 instruction sets, you cannot directly predicate a jump 
based on the contents of a register. As an example, you can't do something like this:
""")

page += Code("""
mov rax, 3          // set rax to 3
mov rcx, 4          // set rcx to 4
lt rax, rcx         // set rax to 1 if rax < rcx, or 0 otherwise
jmp_if rax, 0x47    // if rax is 1, then jump forward 0x47 bytes 
""")

page += Paragraphs(f"""
Those last two instructions, lt and jmp_if, don't exist. Instead, x86 uses a concept called flags. Flags can be imagined as a set of
special registers with the sole purpose of storing whether a particular condition is true or false. There are many flags
in a processor which operates on x86, each of which stores information about something different, but only 5 are important to
us: The Carry Flag, the Parity Flag, the Zero Flag, the Sign Flag, and the Overflow flag. 

Some instructions will set flags, some will ignore them, and others will read from them. An instruction in the first category
is the add instruction. Say we execute {inline_code('mov rax, 3; add rax, 2')}. After this snippet executes, the value in 
rax will clearly be 5. When the add instruction finishes, it will set different flags based on that final value. Since
the result does not change signs compared to the operands, the Overflow Flag is unset (set to 0, no matter its previous value).
Since the result fits in the normal 64 bits, the Carry Flag is Unset. Since the number of bits which are 1 in 5 {inline_code('0000 0101')}
is even, the Parity flag is set. Since the most significant bit of 5 in its 64 bit representation is unset, the Sign Flag is unset.
Finally, since 5 is not 0, the Zero Flag is unset.

You can then do some conditional operations based on these flags. The most common instructions are those of the Jcc family.
JE (Jump Equal), for example, will only jump if the Zero Flag is set. JAE (Jump Above or Equal) will only jump if the Carry
Flag is unset. 

You might ask why JE jumps when the Zero Flag is set. After all, what does an equality check have to do with a zero check?
The answer is the almighty CMP instruction. CMP subtracts two values and sets the flags based on the result, but does not 
store said result. By using this instruction and carefully choosing what Jcc instruction to use, you can make any comparison
between two numbers. For example, take {inline_code('cmp rax, rcx')}. The CMP instruction will subtract the two registers.
If they are equal, then the result will be zero and the Zero flag set. Therefore, if you follow this instruction with a JE
instruction, the JE instruction will in fact be dependent on whether rax and rcx are equal. The other Jcc instructions follow the
same idea.

By using this concept of flags, explained in the Intel Instruction Reference, we can do comparisons and conditional jumps.

There are also a few more optimization opportunities jumps open up. One would be the different varieties of the JMP and
Jcc instructions: some come with a 4-byte offset and others with a 1-byte offset. If we know the jump is to somewhere within
127 bytes on either side (1-byte signed goes from -128 to 127), then we can use the 3x shorter 1-byte form. Additionally,
if we the know that a Jcc is predicated on a SUB instruction, then we know we can skip the CMP since the SUB will have set the
flags already in the exact same way.

Another optimization I've done shows just how obscure x86 optimization can be. The {inline_code('mov rax, 0')} instruction
sets the value of rax to 0. This takes 10 bytes ({inline_code('48 b8 00 00 00 00 00 00 00 00')} if you do it the obvious way,
loading a 64 byte immediate into rax. It can be done in only 7 bytes ({inline_code('48 c7 c0 00 00 00 00')}) if you load 
a 32 byte immediate instead and take advantage of the fact that x86 automatically sign-extends 32 byte immediate to 64 bytes.
The shortest way, however, is to just XOR the register you want to zero out with itself. Since it is a mathematical identity
that a number xor'ed with itself will be zero, this trick will always work. By doing so, you shave this operation down to
only 3 bytes {inline_code('48 31 c0')}.  
""")

page += Heading("Main Accomplishments")
page += OrderedList([
    Paragraph("Implemented Blocks"),
    Paragraph("Implemented and Debugged Block Parameters"),
    Paragraph("Implemented Jumps and Jcc in Assembly"),
    Paragraph("Implemented Conditionals and their Optimizations"),
    Paragraph("Implemented If statements, While Loops, and Comparisons"),
    Paragraph("Implemented simple optimizations for the above"),
])

page += Heading("Reflection")
page += Paragraphs(f"""
The above stuff took far longer than expected, because I did not prepare enough for it. Then again, how can you prepare
for this without actually doing it at least once? However, now that I did get everything to work, it feels very rewarding.
I spent 3 full days trying to make If-statements and block parameters work. Once those were finished, I went on to try and
implement while loops. To my surprise, those 3 days of work on If-statement paid off, and while loops actually worked on the first
try. They were a 5 minute addition. 

I'm now at a point where I feel comfortable working on types, objects, and co. Once I finish that area, I can move on to 
the actual JIT part of the JIT, where it chooses optimizations based on what the program is actually doing at a given time. 
The 5th journal is looking to be packed. 
""")

page += Heading("Sources:")
page += OrderedList([
    Paragraph(f"{hyperlink('x64 Instruction Reference', 'https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #1', 'https://pyokagan.name/blog/2019-09-20-x86encoding/')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #2', 'http://ref.x86asm.net/geek64.html')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #3', 'https://wiki.osdev.org/X86-64_Instruction_Encoding')}"),
    Paragraph(f"{hyperlink('Reference on LLVMLite'), 'https://llvmlite.readthedocs.io/en/latest/user-guide/ir/index.html'}"),
    Paragraph(f"{hyperlink('Ternary Operator in JavaScript, and similar in C, Java C#, etc.'), 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator'}"),
    Paragraph(f"{hyperlink('Ternary Operator in Python'), 'https://docs.python.org/3/reference/expressions.html?highlight=ternary#conditional-expressions'}"),
    Paragraph(f"{hyperlink('Dominance Frontiers', 'https://en.wikipedia.org/wiki/Static_single_assignment_form#Computing_minimal_SSA_using_dominance_frontiers')}"),
    Paragraph(f"{hyperlink('Explanation of Overflow vs Carry Flag', 'http://teaching.idallen.com/dat2343/10f/notes/040_overflow.txt')}"),

])

__pages__ = [page]
