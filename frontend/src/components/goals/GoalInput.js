import React, { useState } from 'react';

import './GoalInput.css';
import Card from '../UI/Card';

function GoalInput(props) {
  const [enteredGoalText, setEnteredGoalText] = useState('');
  const [validationError, setValidationError] = useState('');

  function updateGoalTextHandler(event) {
    setEnteredGoalText(event.target.value);
    if (validationError) {
      setValidationError('');
    }
  }

  function goalSubmitHandler(event) {
    event.preventDefault();

    if (enteredGoalText.trim().length === 0) {
      setValidationError('Invalid text - please enter a longer one!');
      return;
    }

    props.onAddGoal(enteredGoalText);
    setEnteredGoalText('');
    setValidationError('');
  }

  return (
    <section id='goal-input'>
      <Card>
        <form onSubmit={goalSubmitHandler}>
          <label htmlFor='text'>New Goal</label>
          <input
            type='text'
            id='text'
            value={enteredGoalText}
            onChange={updateGoalTextHandler}
          />
          {validationError && (
            <p style={{ color: 'red', marginTop: '0.5rem' }}>
              {validationError}
            </p>
          )}
          <button>Add Goal</button>
        </form>
      </Card>
    </section>
  );
}

export default GoalInput;
