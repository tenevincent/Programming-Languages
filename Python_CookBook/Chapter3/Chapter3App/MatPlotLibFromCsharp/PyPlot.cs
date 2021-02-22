using System;
using System.Collections.Generic;
using System.Text;
using Python.Runtime;


namespace MatPlotLibFromCsharp
{
    public class PyPlot
    {
        private float[] YValues { get;   set; }

        private float[] XValues { get;   set; }

        public PyPlot()
        {

        }

        public PyPlot X(float[] values)
        {
            XValues = values;
            return this;
        }

        public PyPlot Y(float[] values)
        {
            YValues = values;
            return this;
        }

        public object Show()
        {
            using (Py.GIL())
            {
                dynamic mpl = Py.Import("matplotlib");
                dynamic plt = Py.Import("matplotlib.pyplot");

                plt.plot(XValues, YValues);
                plt.show();
            }

            return null;
        }
    }
}
