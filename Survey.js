import { useState } from 'react'
import axios from 'axios'

function Survey() {
  const [sleeping, setSleeping] = useState(0)
  const [exercise, setExercise] = useState(0)
  const [study, setStudy] = useState(0)
  const [screen, setScreen] = useState(0)

  const submitSurvey = async () => {
    await axios.post('http://127.0.0.1:5000/habit', {
      user_id: 1,
      sleeping,
      exercise,
      study_hours: study,
      screen_time: screen
    })

    alert('Survey Submitted')
  }

  return (
    <div>
      <h1>Daily Habit Survey</h1>

      <p>How many hours did you sleep?</p>
      <input type='number' onChange={(e) => setSleeping(e.target.value)} />

      <p>Exercise hours?</p>
      <input type='number' onChange={(e) => setExercise(e.target.value)} />

      <p>Study hours?</p>
      <input type='number' onChange={(e) => setStudy(e.target.value)} />

      <p>Screen time?</p>
      <input type='number' onChange={(e) => setScreen(e.target.value)} />

      <button onClick={submitSurvey}>Submit</button>
    </div>
  )
}

export default Survey
