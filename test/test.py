import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1

    # A=0, B=0
    dut.ui_in.value = 0b00
    await ClockCycles(dut.clk, 1)
    assert (dut.uo_out.value & 0b11) == 0b00

    # A=0, B=1
    dut.ui_in.value = 0b01
    await ClockCycles(dut.clk, 1)
    assert (dut.uo_out.value & 0b11) == 0b01

    # A=1, B=0
    dut.ui_in.value = 0b10
    await ClockCycles(dut.clk, 1)
    assert (dut.uo_out.value & 0b11) == 0b01

    # A=1, B=1
    dut.ui_in.value = 0b11
    await ClockCycles(dut.clk, 1)
    assert (dut.uo_out.value & 0b11) == 0b10

    dut._log.info("HALF ADDER TEST PASSED")
