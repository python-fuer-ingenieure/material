// Wir schreiben ganz gewöhnlichen C-Code, include geht also auch
#include <math.h>

unsigned int heatSim(float *u, float a,
                     unsigned int xSamples, unsigned int ySamples,
                     float dx, float dy,
                     float dt, unsigned int steps) {
  // Wir gehen davon aus, dass das Temperaturgitter schon auf
  // Null initialisiert ist
  // Zähle Schleifendurchgänge als Rückgabewert
  unsigned int loopCount = 0;
  
  for (int ti = 0; ti < steps; ti++) {
    for (int xi = 0; xi < xSamples; xi++) {
      for (int yi = 0; yi < ySamples; yi++) {
        loopCount++;

        // Zugriff auf zweidimensionales Array mit
        //manueller Pointer-Arithmetik
        // Python u[xi,yi] entspricht in C u[xi*ySamples + yi]
        if (xi == 0) {
          u[xi*ySamples + yi] = u[1*ySamples + yi];
        } else if (xi == xSamples - 1) {
          // Achtung: negative Indizes u[-1,yi] gehen nicht
          u[xi*ySamples + yi] = u[(xi-1)*ySamples + yi];
        } else if (yi == 0) {
          u[xi*ySamples + yi] = 0;
        } else if (yi == ySamples - 1) {
          u[xi*ySamples + yi] = 50;
        } else if (pow(xi*dx - 0.5, 2)
                 + pow(yi*dy - 0.5, 2)
                 < pow(0.1, 2)) {
          u[xi*ySamples + yi] = 50;
        } else {
          u[xi*ySamples + yi] += a*dt*(
            (u[(xi+1)*ySamples + yi] + u[(xi-1)*ySamples + yi]
           - 2*u[xi*ySamples + yi])/(dx*dx)
           + (u[xi*ySamples + yi+1] + u[xi*ySamples + yi-1]
           - 2*u[xi*ySamples + yi])/(dy*dy)
          );
        }
      }    
    }
  }

  return loopCount;
}
