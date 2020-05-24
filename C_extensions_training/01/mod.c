#include <Python.h>


static PyObject *mod_met(PyObject *self, PyObject *args){
	int a=0, b=0, c=0;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){
		return NULL;
	}
	int s=a+b+c;
	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++){
			s+=PyLong_AsLong(PyList_GetItem(d, i));
		}
	}

	return Py_BuildValue("i", s);
}


static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Function ..."},
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};


PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
