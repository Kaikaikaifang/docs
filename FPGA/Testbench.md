Vscode 中借助 [Verilog_testbench](https://marketplace.visualstudio.com/items?itemName=Truecrab.verilog-testbench-instance) 生成 testbench:
1. 在需要生成 testbench 的模块中按下 ctrl + shift + p，选择 testbench 指令
2. 控制台输出生成的 testbench

> 👿 需要注意的是，该插件在 unix 环境下可能存在路径问题，可直接修改原 python 代码解决。

Example

> 分频器 testbench 示例代码

```verilog
//~ `New testbench
`timescale 1ns / 1ps

module freq_div_tb;

  // frequency_divider Parameters
  parameter PERIOD = 50;  // 50 ns period clock (20 MHz)


  // freq_div Inputs
  reg  clk = 0;
  reg  rst_n = 0;

  // frequency_divider Outputs
  wire out8;
  wire out16;
  wire out256;

  /*iverilog */
  initial begin
    $dumpfile("freq_div.vcd");  //生成的vcd文件名称
    $dumpvars(0, freq_div_tb);  //tb模块名称
  end
  /*iverilog */

  initial begin
    // 
    forever #(PERIOD / 2) clk = ~clk;
  end

  initial begin
    #(PERIOD * 2) rst_n = 1;
  end

  freq_div u_freq_div (
      .clk  (clk),
      .rst_n(rst_n),

      .out2  (out2),
      .out8  (out8),
      .out16 (out16),
      .out256(out256)
  );

  initial begin
    #10000 $finish;
  end

endmodule

```