"""
This type stub file was generated by pyright.
"""
from typing import Any, Callable, Iterable, Protocol, Sequence, TypeVar, Optional, overload, Union, Literal, Tuple, Type
from numpy.random import RandomState
import numpy as np
from numpy import ndarray
from numpy.typing import ArrayLike
from pandas import DataFrame
from joblib import Memory
from scipy.sparse import (
    csr_matrix, 
    csc_matrix,
    coo_matrix,
    lil_matrix,
    bsr_matrix,
    dok_matrix,
    dia_matrix
)


"""Utilities for input validation"""
FLOAT_DTYPES: Tuple[Type[np.float64], Type[np.float32], Type[np.float16]] = ...

_S = TypeVar('_S', bound=Callable[..., Any])
class _JoblibMemoryLike(Protocol):
    def cache(self, func: _S) -> Callable[[_S], _S]:
        pass

_Estimator = Any # TODO
_SparseMatrix = Union[csr_matrix, csc_matrix, coo_matrix, lil_matrix, bsr_matrix, dok_matrix, dia_matrix]

_T = TypeVar('_T', bound=Callable[..., Any])

@overload
def _deprecate_positional_args(func: _T) -> _T: ...

@overload
def _deprecate_positional_args(func: _T=..., *, version: str=...) -> Callable[[_T], _T]:
    """Decorator for methods that issues warnings for positional arguments.

    Using the keyword-only argument syntax in pep 3102, arguments after the
    * will issue a warning when passed as a positional argument.

    Parameters
    ----------
    func : callable, default=None
        Function to check arguments on.
    version : callable, default="1.0 (renaming of 0.25)"
        The version when positional arguments will result in error.
    """
    ...

def assert_all_finite(X: Union[ArrayLike, _SparseMatrix], *, allow_nan: bool = ...) -> None: 
    """Throw a ValueError if X contains NaN or infinity.

    Parameters
    ----------
    X : {ndarray, sparse matrix}

    allow_nan : bool, default=False
    """
    ...

def as_float_array(X: Union[ArrayLike, _SparseMatrix], *, copy: bool =..., force_all_finite: Union[bool, Literal['allow-nan']] = ...) -> ndarray:
    """Converts an array-like to an array of floats.

    The new dtype will be np.float32 or np.float64, depending on the original
    type. The function can create a copy or modify the argument depending
    on the argument copy.

    Parameters
    ----------
    X : {array-like, sparse matrix}

    copy : bool, default=True
        If True, a copy of X will be created. If False, a copy may still be
        returned if X's dtype is not a floating point type.

    force_all_finite : bool or 'allow-nan', default=True
        Whether to raise an error on np.inf, np.nan, pd.NA in X. The
        possibilities are:

        - True: Force all values of X to be finite.
        - False: accepts np.inf, np.nan, pd.NA in X.
        - 'allow-nan': accepts only np.nan and pd.NA values in X. Values cannot
          be infinite.

        .. versionadded:: 0.20
           ``force_all_finite`` accepts the string ``'allow-nan'``.

        .. versionchanged:: 0.23
           Accepts `pd.NA` and converts it into `np.nan`

    Returns
    -------
    XT : {ndarray, sparse matrix}
        An array of type float.
    """
    ...

def check_memory(memory: Union[_JoblibMemoryLike, str, None]) -> Memory:
    """Check that ``memory`` is joblib.Memory-like.

    joblib.Memory-like means that ``memory`` can be converted into a
    joblib.Memory instance (typically a str denoting the ``location``)
    or has the same interface (has a ``cache`` method).

    Parameters
    ----------
    memory : None, str or object with the joblib.Memory interface

    Returns
    -------
    memory : object with the joblib.Memory interface

    Raises
    ------
    ValueError
        If ``memory`` is not joblib.Memory-like.
    """
    ...

def check_consistent_length(*arrays: Union[ArrayLike, ndarray, _SparseMatrix, DataFrame]) -> None:
    """Check that all arrays have consistent first dimensions.

    Checks whether all objects in arrays have the same shape or length.

    Parameters
    ----------
    *arrays : list or tuple of input objects.
        Objects that will be checked for consistent length.
    """
    ...

def indexable(*iterables: Iterable[Any]) -> Tuple[Sequence[Any]]:
    """Make arrays indexable for cross-validation.

    Checks consistent length, passes through None, and ensures that everything
    can be indexed by converting sparse matrices to csr and converting
    non-interable objects to arrays.

    Parameters
    ----------
    *iterables : {lists, dataframes, ndarrays, sparse matrices}
        List of objects to ensure sliceability.
    """
    ...

def check_array(array: Union[ArrayLike, ndarray, DataFrame, _SparseMatrix], 
            accept_sparse: Union[str, bool, Sequence[str], Tuple[str]]=...,
            *, 
            accept_large_sparse:bool =..., 
            dtype: Optional[Union[Literal['numeric'], type, Sequence[type]]] =..., 
            order: Optional[str]=..., 
            copy: bool=..., 
            force_all_finite: Union[bool, Literal['allow-nan']]=..., 
            ensure_2d: bool=..., 
            allow_nd: bool=..., 
            ensure_min_samples: int=..., 
            ensure_min_features: int=..., 
            estimator: Optional[Union[str, _Estimator]]=...) -> Any: # incomplete
    """Input validation on an array, list, sparse matrix or similar.

    By default, the input is checked to be a non-empty 2D array containing
    only finite values. If the dtype of the array is object, attempt
    converting to float, raising on failure.

    Parameters
    ----------
    array : object
        Input object to check / convert.

    accept_sparse : str, bool or list/tuple of str, default=False
        String[s] representing allowed sparse matrix formats, such as 'csc',
        'csr', etc. If the input is sparse but not in the allowed format,
        it will be converted to the first listed format. True allows the input
        to be any format. False means that a sparse matrix input will
        raise an error.

    accept_large_sparse : bool, default=True
        If a CSR, CSC, COO or BSR sparse matrix is supplied and accepted by
        accept_sparse, accept_large_sparse=False will cause it to be accepted
        only if its indices are stored with a 32-bit dtype.

        .. versionadded:: 0.20

    dtype : 'numeric', type, list of type or None, default='numeric'
        Data type of result. If None, the dtype of the input is preserved.
        If "numeric", dtype is preserved unless array.dtype is object.
        If dtype is a list of types, conversion on the first type is only
        performed if the dtype of the input is not in the list.

    order : {'F', 'C'} or None, default=None
        Whether an array will be forced to be fortran or c-style.
        When order is None (default), then if copy=False, nothing is ensured
        about the memory layout of the output array; otherwise (copy=True)
        the memory layout of the returned array is kept as close as possible
        to the original array.

    copy : bool, default=False
        Whether a forced copy will be triggered. If copy=False, a copy might
        be triggered by a conversion.

    force_all_finite : bool or 'allow-nan', default=True
        Whether to raise an error on np.inf, np.nan, pd.NA in array. The
        possibilities are:

        - True: Force all values of array to be finite.
        - False: accepts np.inf, np.nan, pd.NA in array.
        - 'allow-nan': accepts only np.nan and pd.NA values in array. Values
          cannot be infinite.

        .. versionadded:: 0.20
           ``force_all_finite`` accepts the string ``'allow-nan'``.

        .. versionchanged:: 0.23
           Accepts `pd.NA` and converts it into `np.nan`

    ensure_2d : bool, default=True
        Whether to raise a value error if array is not 2D.

    allow_nd : bool, default=False
        Whether to allow array.ndim > 2.

    ensure_min_samples : int, default=1
        Make sure that the array has a minimum number of samples in its first
        axis (rows for a 2D array). Setting to 0 disables this check.

    ensure_min_features : int, default=1
        Make sure that the 2D array has some minimum number of features
        (columns). The default value of 1 rejects empty datasets.
        This check is only enforced when the input data has effectively 2
        dimensions or is originally 1D and ``ensure_2d`` is True. Setting to 0
        disables this check.

    estimator : str or estimator instance, default=None
        If passed, include the name of the estimator in warning messages.

    Returns
    -------
    array_converted : object
        The converted and validated array.
    """
    ...

def check_X_y(X: Union[ArrayLike, ndarray, _SparseMatrix], 
            y: Union[ArrayLike, ndarray, _SparseMatrix], 
            accept_sparse: Union[str, bool, Sequence[str], Tuple[str]]=...,
            *, 
            accept_large_sparse: bool=..., 
            dtype: Optional[Union[Literal['numeric'], type, Sequence[type]]] =..., 
            order: Optional[str]=..., 
            copy: bool=..., 
            force_all_finite: Union[bool, Literal['allow-nan']]=..., 
            ensure_2d: bool=..., 
            allow_nd: bool=..., 
            multi_output: bool=..., 
            ensure_min_samples: int=..., 
            ensure_min_features: int=..., 
            y_numeric: bool=..., 
            estimator: Optional[Union[str, _Estimator]]=...) -> Any:  # incomplete
    """Input validation for standard estimators.

    Checks X and y for consistent length, enforces X to be 2D and y 1D. By
    default, X is checked to be non-empty and containing only finite values.
    Standard input checks are also applied to y, such as checking that y
    does not have np.nan or np.inf targets. For multi-label y, set
    multi_output=True to allow 2D and sparse y. If the dtype of X is
    object, attempt converting to float, raising on failure.

    Parameters
    ----------
    X : {ndarray, list, sparse matrix}
        Input data.

    y : {ndarray, list, sparse matrix}
        Labels.

    accept_sparse : str, bool or list of str, default=False
        String[s] representing allowed sparse matrix formats, such as 'csc',
        'csr', etc. If the input is sparse but not in the allowed format,
        it will be converted to the first listed format. True allows the input
        to be any format. False means that a sparse matrix input will
        raise an error.

    accept_large_sparse : bool, default=True
        If a CSR, CSC, COO or BSR sparse matrix is supplied and accepted by
        accept_sparse, accept_large_sparse will cause it to be accepted only
        if its indices are stored with a 32-bit dtype.

        .. versionadded:: 0.20

    dtype : 'numeric', type, list of type or None, default='numeric'
        Data type of result. If None, the dtype of the input is preserved.
        If "numeric", dtype is preserved unless array.dtype is object.
        If dtype is a list of types, conversion on the first type is only
        performed if the dtype of the input is not in the list.

    order : {'F', 'C'}, default=None
        Whether an array will be forced to be fortran or c-style.

    copy : bool, default=False
        Whether a forced copy will be triggered. If copy=False, a copy might
        be triggered by a conversion.

    force_all_finite : bool or 'allow-nan', default=True
        Whether to raise an error on np.inf, np.nan, pd.NA in X. This parameter
        does not influence whether y can have np.inf, np.nan, pd.NA values.
        The possibilities are:

        - True: Force all values of X to be finite.
        - False: accepts np.inf, np.nan, pd.NA in X.
        - 'allow-nan': accepts only np.nan or pd.NA values in X. Values cannot
          be infinite.

        .. versionadded:: 0.20
           ``force_all_finite`` accepts the string ``'allow-nan'``.

        .. versionchanged:: 0.23
           Accepts `pd.NA` and converts it into `np.nan`

    ensure_2d : bool, default=True
        Whether to raise a value error if X is not 2D.

    allow_nd : bool, default=False
        Whether to allow X.ndim > 2.

    multi_output : bool, default=False
        Whether to allow 2D y (array or sparse matrix). If false, y will be
        validated as a vector. y cannot have np.nan or np.inf values if
        multi_output=True.

    ensure_min_samples : int, default=1
        Make sure that X has a minimum number of samples in its first
        axis (rows for a 2D array).

    ensure_min_features : int, default=1
        Make sure that the 2D array has some minimum number of features
        (columns). The default value of 1 rejects empty datasets.
        This check is only enforced when X has effectively 2 dimensions or
        is originally 1D and ``ensure_2d`` is True. Setting to 0 disables
        this check.

    y_numeric : bool, default=False
        Whether to ensure that y has a numeric type. If dtype of y is object,
        it is converted to float64. Should only be used for regression
        algorithms.

    estimator : str or estimator instance, default=None
        If passed, include the name of the estimator in warning messages.

    Returns
    -------
    X_converted : object
        The converted and validated X.

    y_converted : object
        The converted and validated y.
    """
    ...

def column_or_1d(y: ArrayLike, *, warn: bool=...) -> ndarray:
    """ Ravel column or 1d numpy array, else raises an error.

    Parameters
    ----------
    y : array-like

    warn : bool, default=False
       To control display of warnings.

    Returns
    -------
    y : ndarray

    """
    ...

def check_random_state(seed: Optional[Union[int, RandomState]]) -> RandomState:
    """Turn seed into a np.random.RandomState instance

    Parameters
    ----------
    seed : None, int or instance of RandomState
        If seed is None, return the RandomState singleton used by np.random.
        If seed is an int, return a new RandomState instance seeded with seed.
        If seed is already a RandomState instance, return it.
        Otherwise raise ValueError.
    """
    ...

def has_fit_parameter(estimator: _Estimator, parameter: str) -> bool:
    """Checks whether the estimator's fit method supports the given parameter.

    Parameters
    ----------
    estimator : object
        An estimator to inspect.

    parameter : str
        The searched parameter.

    Returns
    -------
    is_parameter: bool
        Whether the parameter was found to be a named parameter of the
        estimator's fit method.

    Examples
    --------
    >>> from sklearn.svm import SVC
    >>> has_fit_parameter(SVC(), "sample_weight")
    True

    """
    ...

@overload
def check_symmetric(array: ArrayLike, 
        *, 
        tol: float=..., 
        raise_warning: bool=..., 
        raise_exception: bool=...) -> ArrayLike: ...
@overload
def check_symmetric(array: _SparseMatrix, 
        *, 
        tol: float=..., 
        raise_warning: bool=..., 
        raise_exception: bool=...) -> _SparseMatrix:
    """Make sure that array is 2D, square and symmetric.

    If the array is not symmetric, then a symmetrized version is returned.
    Optionally, a warning or exception is raised if the matrix is not
    symmetric.

    Parameters
    ----------
    array : {ndarray, sparse matrix}
        Input object to check / convert. Must be two-dimensional and square,
        otherwise a ValueError will be raised.

    tol : float, default=1e-10
        Absolute tolerance for equivalence of arrays. Default = 1E-10.

    raise_warning : bool, default=True
        If True then raise a warning if conversion is required.

    raise_exception : bool, default=False
        If True then raise an exception if array is not symmetric.

    Returns
    -------
    array_sym : {ndarray, sparse matrix}
        Symmetrized version of the input array, i.e. the average of array
        and array.transpose(). If sparse, then duplicate entries are first
        summed and zeros are eliminated.
    """
    ...

def check_is_fitted(estimator: _Estimator, 
            attributes: Optional[Union[str, Sequence[str], Tuple[str]]]=..., 
            *, 
            msg: Optional[str]=..., 
            all_or_any:Callable[[Iterable[object]], bool]=...) -> None:
    """Perform is_fitted validation for estimator.

    Checks if the estimator is fitted by verifying the presence of
    fitted attributes (ending with a trailing underscore) and otherwise
    raises a NotFittedError with the given message.

    This utility is meant to be used internally by estimators themselves,
    typically in their own predict / transform methods.

    Parameters
    ----------
    estimator : estimator instance
        estimator instance for which the check is performed.

    attributes : str, list or tuple of str, default=None
        Attribute name(s) given as string or a list/tuple of strings
        Eg.: ``["coef_", "estimator_", ...], "coef_"``

        If `None`, `estimator` is considered fitted if there exist an
        attribute that ends with a underscore and does not start with double
        underscore.

    msg : str, default=None
        The default error message is, "This %(name)s instance is not fitted
        yet. Call 'fit' with appropriate arguments before using this
        estimator."

        For custom messages if "%(name)s" is present in the message string,
        it is substituted for the estimator name.

        Eg. : "_Estimator, %(name)s, must be fitted before sparsifying".

    all_or_any : callable, {all, any}, default=all
        Specify whether all or any of the given attributes must exist.

    Returns
    -------
    None

    Raises
    ------
    NotFittedError
        If the attributes are not found.
    """
    ...

def check_non_negative(X: Union[ArrayLike, _SparseMatrix], whom: str) -> None:
    """
    Check if there is any negative value in an array.

    Parameters
    ----------
    X : {array-like, sparse matrix}
        Input data.

    whom : str
        Who passed X to this function.
    """
    ...

def check_scalar(x: object, name: str, target_type: type, *, min_val: Optional[float]=..., max_val: Optional[float]=...) -> None:
    """Validate scalar parameters type and value.

    Parameters
    ----------
    x : object
        The scalar parameter to validate.

    name : str
        The name of the parameter to be printed in error messages.

    target_type : type or tuple
        Acceptable data types for the parameter.

    min_val : float or int, default=None
        The minimum valid value the parameter can take. If None (default) it
        is implied that the parameter does not have a lower bound.

    max_val : float or int, default=None
        The maximum valid value the parameter can take. If None (default) it
        is implied that the parameter does not have an upper bound.

    Raises
    -------
    TypeError
        If the parameter's type does not match the desired type.

    ValueError
        If the parameter's value violates the given bounds.
    """
    ...

def __getattr__(name: str) -> Any: ... # incomplete