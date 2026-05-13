import { useEffect, useState } from 'react'
import axios from 'axios'

function Admin() {
  const [stats, setStats] = useState({})

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/admin/stats')
      .then((res) => setStats(res.data))
  }, [])

  return (
    <div>
      <h1>Admin Dashboard</h1>

      <p>Total Users: {stats.total_users}</p>
      <p>Total Surveys: {stats.total_surveys}</p>
    </div>
  )
}

export default Admin
