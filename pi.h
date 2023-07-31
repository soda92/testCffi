#ifdef BUILD_LIB
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __declspec(dllimport)
#endif
#define PASCAL __stdcall
float EXPORT PASCAL pi_approx(int n);