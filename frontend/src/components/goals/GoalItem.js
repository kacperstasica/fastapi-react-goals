import React from 'react';

import './GoalItem.css';

function GoalItem(props) {
  return (
    <li className="goal-item" onClick={props.onDelete.bind(null, props.id)}>
      <span className="goal-text">{props.text}</span>
      <span className="goal-delete-hint">✕ Click to delete</span>
    </li>
  );
}

export default GoalItem;
