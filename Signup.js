import { useState } from 'react'
import axios from 'axios'

function Signup() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSignup = async () => {
    await axios.post('http://127.0.0.1:5000/signup', {
      username,
      password
    })

    alert('Account Created')
  }

  return (
    <div>
      <h1>Signup</h1>

      <input
        placeholder='Username'
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        type='password'
        placeholder='Password'
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={handleSignup}>Signup</button>
    </div>
  )
}

export default Signup
