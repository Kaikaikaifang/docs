# iVerilog

1. 仿真
```bash
iverilog -o simulation/iverilog/freq_div.vvp -y ./src testbench/freq_div_tb.v
```
2. 生成波形文件
```bash
vvp simulation/iverilog/freq_div.vvp -vcd
```
3. 查看波形
