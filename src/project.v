module tt_um_half_adder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Half Adder
    // ui_in[0] = A
    // ui_in[1] = B

    // Sum = A XOR B
    assign uo_out[0] = ui_in[0] ^ ui_in[1];

    // Carry = A AND B
    assign uo_out[1] = ui_in[0] & ui_in[1];

    // Unused output pins
    assign uo_out[7:2] = 6'b000000;

    // Bidirectional pins unused
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

endmodule
