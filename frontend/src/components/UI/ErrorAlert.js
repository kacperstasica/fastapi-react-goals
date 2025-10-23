import React from 'react';

import './ErrorAlert.css';

function ErrorAlert(props) {
  return (
    <section className='error-alert'>
      <div>
        <h2>Something went wrong!</h2>
        <p>{props.errorText}</p>
      </div>
      {props.onClear && (
        <button onClick={props.onClear} style={{ marginLeft: 'auto' }}>
          ✕
        </button>
      )}
    </section>
  );
}

export default ErrorAlert;
