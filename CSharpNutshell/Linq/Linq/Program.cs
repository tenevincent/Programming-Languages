using ConsoleDump;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
 


namespace Linqs
{
    class Program
    {
        static void Main(string[] args)
        {
            
            string[] names = { "Tom", "Dick", "Harry", "Tene", "Tina" };
            List<string> vornamen = new List<string>();
            vornamen.Add("Tom");
            vornamen.Add("Harry");
            vornamen.Add("Tene");
            vornamen.Add("Timan");
            vornamen.Add("Carian");


            var results = vornamen.Where( name => name.EndsWith("n"));
            results.Dump();

            "The results are...".Dump();
            results.Dump();


            IEnumerable<string> filteredNames = names.Where(n => n.StartsWith("T"));
            "The filtered objects are...".Dump();
            filteredNames.Dump();

         

            Console.ReadKey();

        }
    }
}
