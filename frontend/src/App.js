import React, { useState, useEffect } from 'react';

import GoalInput from './components/goals/GoalInput';
import CourseGoals from './components/goals/CourseGoals';
import ErrorAlert from './components/UI/ErrorAlert';
import LoadingSpinner from './components/UI/LoadingSpinner';
import { useApi } from './hooks/useApi';

function App() {
  const [loadedGoals, setLoadedGoals] = useState([]);
  const { isLoading, error, clearError, request } = useApi();

  useEffect(() => {
    const fetchGoals = async () => {
      try {
        const data = await request('/goals');
        if (data) {
          setLoadedGoals(data.goals);
        }
      } catch (err) {
        // Error is already handled by useApi hook
        console.error('Failed to fetch goals:', err);
      }
    };

    fetchGoals();
  }, [request]);

  async function addGoalHandler(goalText) {
    try {
      const data = await request('/goals', {
        method: 'POST',
        body: JSON.stringify({ text: goalText }),
      });

      if (data) {
        setLoadedGoals((prevGoals) => [
          {
            id: data.goal.id,
            text: data.goal.text,
          },
          ...prevGoals,
        ]);
      }
    } catch (err) {
      // Error is already handled by useApi hook
      console.error('Failed to add goal:', err);
    }
  }

  async function deleteGoalHandler(goalId) {
    try {
      const data = await request(`/goals/${goalId}`, {
        method: 'DELETE',
      });

      if (data) {
        setLoadedGoals((prevGoals) => 
          prevGoals.filter((goal) => goal.id !== goalId)
        );
      }
    } catch (err) {
      // Error is already handled by useApi hook
      console.error('Failed to delete goal:', err);
    }
  }

  return (
    <div>
      {error && <ErrorAlert errorText={error} onClear={clearError} />}
      <GoalInput onAddGoal={addGoalHandler} />
      {isLoading && <LoadingSpinner />}
      {!isLoading && (
        <CourseGoals goals={loadedGoals} onDeleteGoal={deleteGoalHandler} />
      )}
    </div>
  );
}

export default App;
