module tt_um_half_adder (
    input  wire [7:0] ui,
    output wire [7:0] uo,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Half Adder
    // ui[0] = A
    // ui[1] = B
    // uo[0] = Sum
    // uo[1] = Carry

    assign uo[0] = ui[0] ^ ui[1];  // Sum
    assign uo[1] = ui[0] & ui[1];  // Carry

    assign uo[7:2] = 6'b0;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
