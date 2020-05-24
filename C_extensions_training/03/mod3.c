#include <Python.h>

int Euklides(int a, int b)
{
    if(b==0)
        return a;
    else
        return Euklides(b, a%b);
}

static PyObject *mod_met(PyObject *self, PyObject *args){
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "O", &d)){
		return NULL;
	}
    PyObject *key, *value;
    Py_ssize_t pos = 0;
    while(PyDict_Next(d, &pos, &key, &value))
    {
        int nwd = Euklides(PyLong_AsLong(PyTuple_GetItem(key, 0)),  PyLong_AsLong(PyTuple_GetItem(key, 1)));
        PyDict_SetItem(d, key, PyLong_FromLong(nwd));
    }

	return d;
}


static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."},
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod3",
        NULL,
        -1,
        mod_metody
};


PyMODINIT_FUNC PyInit_mod3(void){
        return PyModule_Create(&modmodule);
}
