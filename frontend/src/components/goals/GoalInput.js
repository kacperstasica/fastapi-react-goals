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

  async function goalSubmitHandler(event) {
    event.preventDefault();

    if (enteredGoalText.trim().length === 0) {
      setValidationError('Invalid text - please enter a longer one!');
      return;
    }

    const result = await props.onAddGoal(enteredGoalText);
    
    if (result?.error) {
      setValidationError(result.error);
      return;
    }

    if (result?.success) {
      setEnteredGoalText('');
      setValidationError('');
    }
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
            <div className="validation-warning">
              ⚠️ {validationError}
            </div>
          )}
          <button>Add Goal</button>
        </form>
      </Card>
    </section>
  );
}

export default GoalInput;
