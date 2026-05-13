import { useEffect, useState } from 'react'
import axios from 'axios'

function Dashboard() {
  const [report, setReport] = useState({})

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/weekly/1')
      .then((res) => setReport(res.data))
  }, [])

  return (
    <div>
      <h1>Weekly Report</h1>

      <p>Average Sleep: {report.average_sleep}</p>
      <p>Average Exercise: {report.average_exercise}</p>
    </div>
  )
}

export default Dashboard
