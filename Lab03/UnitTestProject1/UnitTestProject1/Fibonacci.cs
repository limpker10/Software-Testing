using System;

public class Fibonacci
{
    public int getNthNumberFibonacci(int n)
    {
        int current = 1, prev = 0;

        if (n < 0) { throw new ArgumentException("El número no puede ser negativo.", nameof(n)); }
        
        if (n == 0) { return 0; }

        for (int i = 2; i <= n; i++)
        {
            int temp = current;
            current = prev + current;
            prev = temp;
        }

        return current;
    }
    //public uint getNthNumberFibonacci(uint n)
    //{
    //    uint current = 1, prev = 0;

    //    if (n == 0) { return 0; }

    //    for (uint i = 2; i <= n; i++)
    //    {
    //        uint temp = current;
    //        current = prev + current;
    //        prev = temp;
    //    }

    //    return current;
    //}
}
