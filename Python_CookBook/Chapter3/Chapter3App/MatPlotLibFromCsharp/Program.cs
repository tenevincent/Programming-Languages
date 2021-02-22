using System;
using System.Collections.Generic;
using Python.Runtime;
using System.Linq;




namespace MatPlotLibFromCsharp
{
    class Program
    {

        static void Main(string[] args)
        {

            var python = new PyPlot();

            var xvalues = new List<float>();
            var yvalues = new List<float>();
            for (int i = 0; i < 1; i++)
            {
                xvalues.Add(i);
                yvalues.Add(new Random().Next(20,30)); 
            }
            python.X(xvalues.ToArray());
            python.Y(yvalues.ToArray());

            python.Show();

            Console.WriteLine("Hello World!");
            Console.ReadKey();
        }
    }
}
