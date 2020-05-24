#include <Python.h>
#include <stdlib.h>
#include <time.h>



void counting(double *tab, double* sizes, double n)
{
    for(int i=0; i<n; i++)
	{
	    double x = (double)(rand()) / (double)(RAND_MAX+1.);
	    double y = (double)(rand()) / (double)(RAND_MAX+1.);
	    for(int j=0;j<10;j++)
	    {
	        if(x<=sizes[j] && y<=sizes[j])
	        {
                tab[j]++;
	        }
	    }
	}
}

static PyObject *mod_met(PyObject *self, PyObject *args){
	int N;
	if(!PyArg_ParseTuple(args, "i", &N))
	{
		return NULL;
	}
	srand(time(NULL));
	PyObject *list = PyList_New(10);
	double sizes[] = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1};
	double procenty[] = {0., 0., 0., 0., 0., 0., 0., 0., 0.,0.};

	counting(procenty, sizes, N);

	for(int i=0;i<10;i++)
	    PyList_SetItem(list, i, PyFloat_FromDouble(procenty[i]/N*100));

	return list;
}


static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."},
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod2",
        NULL,
        -1,
        mod_metody
};


PyMODINIT_FUNC PyInit_mod2(void){
        return PyModule_Create(&modmodule);
}
