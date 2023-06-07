using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace UnitTestProject1
{

    [TestClass]
    public class FibonacciTests
    {
        private Fibonacci fibonacci;

        [TestInitialize]
        public void Initialize()
        {
            fibonacci = new Fibonacci();
        }

        [TestMethod]
        public void Test_Fibonacci_ForLowerLimit()
        {
            
            int result = fibonacci.getNthNumberFibonacci(0);

            Assert.AreEqual(0, result);
        }

        [TestMethod]
        public void Test_Fibonacci_ForUpperLimit()
        {
           
            int result = fibonacci.getNthNumberFibonacci(40);

            Assert.AreEqual(102334155, result);
        }

        [TestMethod]
        [DataRow(0, 0)]
        [DataRow(1, 1)]
        [DataRow(2, 1)]
        [DataRow(5, 5)]
        public void Test_Fibonacci_ForSpecificNumbers(int n, int expected)
        {
            int result = fibonacci.getNthNumberFibonacci(n);

            Assert.AreEqual(expected, result);
        }

        [TestMethod]
        [DynamicData(nameof(TestCases.GetPositiveTestCases), typeof(TestCases), DynamicDataSourceType.Method)]
        public void Test_Fibonacci_ForPositiveNumbers(int n, int expected)
        {
            int result = fibonacci.getNthNumberFibonacci(n);

            Assert.AreEqual(expected, result);
        }

        [TestMethod]
        [DynamicData(nameof(TestCases.GetNegativeTestCases), typeof(TestCases), DynamicDataSourceType.Method)]
        public void Test_Fibonacci_ThrowsException_ForNegativeNumbers(int n)
        {
            Assert.ThrowsException<System.ArgumentException>(() => fibonacci.getNthNumberFibonacci(n));
        }

    }
}