#!/bin/bash

for i in r2     r3      a3      r4      a4      d4      r5      a5      d5      r6      a6      d6      r7      a7      d7      r8      a8      d8      r9      a9      d9      r10     a10     d10     r11     a11     d11     r12     a12     d12     r13     a13     d13     r14     a14     d14     r15     a15     d15     r16     a16     d16     r17     a17     d17     r18     a18     d18     r19     a19     d19     r20     a20     d20     r21     a21     d21     r22     a22     d22     r23     a23     d23     r24     a24     d24     r25     a25     d25     r26     a26     d26     r27     a27     d27     r28     a28     d28     r29     a29     d29     r30     a30     d30     r31     a31     d31     r32     a32     d32     r33     a33     d33     r34     a34     d34     r35     a35     d35     r36     a36     d36     r37     a37     d37     r38     a38     d38     r39     a39     d39     r40     a40     d40     r41     a41     d41     r42     a42     d42     r43     a43     d43     r44     a44     d44     r45     a45     d45     r46     a46     d46     r47     a47     d47     r48     a48     d48     r49     a49     d49
do
python3 MI.py $i  &
done
