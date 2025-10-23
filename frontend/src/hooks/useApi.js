import { useState, useCallback } from 'react';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost';

export function useApi() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const clearError = useCallback(() => {
    setError(null);
  }, []);

  const request = useCallback(async (endpoint, options = {}) => {
    setIsLoading(true);
    setError(null);

    const controller = new AbortController();
    const signal = controller.signal;

    try {
      const response = await fetch(`${API_URL}${endpoint}`, {
        ...options,
        signal,
        headers: {
          'Content-Type': 'application/json',
          ...options.headers,
        },
      });

      const resData = await response.json();

      if (!response.ok) {
        throw new Error(resData.message || resData.detail || 'Request failed.');
      }

      setIsLoading(false);
      return resData;
    } catch (err) {
      if (err.name === 'AbortError') {
        console.log('Request was cancelled');
        return null;
      }
      
      const errorMessage = err.message || 'Request failed - the server responded with an error.';
      setError(errorMessage);
      setIsLoading(false);
      throw err;
    }
  }, []);

  return { isLoading, error, clearError, request };
}

