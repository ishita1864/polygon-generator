# polygon-ccbd

Polygon Generator

Polygons of varying complexity are used to represent spatial objects like water bodies, forest land, cropland etc. As the shapes of these kinds of objects
are irregular, the polygons that represent them can have large number of vertices. Below map of Bengaluru shows the boundaries for Parks, water
bodies, districts in Bengaluru.

![Screenshot 2023-07-07 at 6 24 02 PM](https://github.com/ishita1864/polygon-ccbd/assets/62196026/91349f38-f59a-49c3-ad74-f3a1bd0de9d0)

The Polygon can be represented as a Well Known Text (WKT) Object.

Aim of this project is to generate random polygons having vertices from 10 upto 500, and save these shapes as WKT in a text file. Each WKT shape will be
delimited by a new line (\n) character. Plot the polygons using a visualization software tool, onto a single canvas.

Additionally, we: 

1. Observe the file sizes and time taken to generate a large number of
polygons.

2. What kind of data distribution can be observed for objects like water bodies, forests, constructed land/buildings, grassland, cultivated
land/agriculture. Can any of these variations be integrated into your solution?
