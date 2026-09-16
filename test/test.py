import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Start")

    # Start clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Enable
    dut.ena.value = 1

    # Reset
    dut.ui.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 2)

    dut.rst_n.value = 1

    # Test 00
    dut.ui.value = 0b00
    await ClockCycles(dut.clk, 1)
    assert (dut.uo.value & 0b11) == 0b00

    # Test 01
    dut.ui.value = 0b01
    await ClockCycles(dut.clk, 1)
    assert (dut.uo.value & 0b11) == 0b01

    # Test 10
    dut.ui.value = 0b10
    await ClockCycles(dut.clk, 1)
    assert (dut.uo.value & 0b11) == 0b01

    # Test 11
    dut.ui.value = 0b11
    await ClockCycles(dut.clk, 1)
    assert (dut.uo.value & 0b11) == 0b10

    dut._log.info("HALF ADDER TEST PASSED")
