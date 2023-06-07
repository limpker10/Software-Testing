using System.Collections.Generic;

public static class TestCases
{
    public static IEnumerable<object[]> GetPositiveTestCases()
    {
        yield return new object[] { 17, 1597 };
        yield return new object[] { 14, 377 };
        yield return new object[] { 10, 55 };
    }

    public static IEnumerable<object[]> GetNegativeTestCases()
    {
        yield return new object[] { -1 };
        yield return new object[] { -5 };
        yield return new object[] { -10 };
    }
}
