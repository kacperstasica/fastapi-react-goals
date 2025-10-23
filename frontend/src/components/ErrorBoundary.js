import React from 'react';
import ErrorAlert from './UI/ErrorAlert';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          <ErrorAlert 
            errorText={this.state.error?.message || 'Something went wrong!'} 
          />
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;

