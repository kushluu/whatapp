import React, { useState } from 'react';
import './login.css'
import axios from 'axios'
import { useLocation, Link } from 'react-router-dom';

const Login = () => {
  const [emailid, setEmailId] = useState('');
  const [password, setPassword] = useState('');
  const history = useLocation();


  const handleLogin = () => {

    const postData = {
      email_id: emailid,
      password : password,
      
    };
    axios.post('http://127.0.0.1:8001/user/login', postData)
      .then((response) => {
        <Link to="/dashboard"/>

      })
      .catch((error) => {
        console.error('POST Error:', error);
      });
      <Link to="/dashboard"/>

    console.log('OTP:', setPassword);
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <input
        type="text"
        placeholder="enter email address"
        value={emailid}
        onChange={(e) => setEmailId(e.target.value)}
      />
      <br/>
      <input
        type="password"
        placeholder="enter password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <br/>
      <button className='login-btn' onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
