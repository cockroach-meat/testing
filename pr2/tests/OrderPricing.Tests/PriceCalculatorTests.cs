using Microsoft.VisualStudio.TestTools.UnitTesting;
using OrderPricing;

namespace OrderPricing.Tests;

[TestClass]
public class PriceCalculatorTests
{
    [TestMethod]
    public void RegularOrder_1000WithoutLoyalty_TotalIs1300()
    {
        // Arrange: данные и ожидание, рассчитанное по требованиям.
        decimal subtotal = 1000m;
        decimal expected = 1300m;

        // Act: один вызов проверяемого поведения.
        decimal actual = PriceCalculator.CalculateTotal(subtotal, false, false);

        // Assert: сравнение ожидания и результата.
        Assert.AreEqual(expected, actual);
    }

    [TestMethod]
    public void RegularOrder_Below0_ThrowsException()
    {
        decimal subtotal = -1m;

        Assert.ThrowsException<ArgumentOutOfRangeException>(() => PriceCalculator.CalculateTotal(subtotal, false, false));
    }

    [TestMethod]
    public void RegularOrder_0WithoutLoyality_TotalIs300()
    {
        decimal subtotal = 0m;

        Assert.AreEqual(PriceCalculator.CalculateTotal(subtotal, false, false), 300);
    }

    [TestMethod]
    public void RegualOrder_100000WithoutLoyality_TotalIs100300()
    {
        decimal subtotal = 100_000m;

        Assert.AreEqual(PriceCalculator.CalculateTotal(subtotal, false, false), 100_300m);
    }

    [TestMethod]
    public void RegularOrder_100001WithoutLoyality_ThrowsException()
    {
        decimal subtotal = 100_001m;

        Assert.ThrowsException<ArgumentOutOfRangeException>(() => PriceCalculator.CalculateTotal(subtotal, false, false));
    }

    // Добавьте собственные тесты. Исходный модуль менять нельзя.
}
