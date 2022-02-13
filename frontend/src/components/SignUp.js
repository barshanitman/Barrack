import React from 'react'
import './SignUp.css'
import Login from './Login/Login'

const SignUp = () => {

  return (

    <div>
      <body>
        <div className='hero'>
          <div className='form-box'>
            <div className='button-box'>
              <div id='btn'>
              </div>
              <button type='button' className='toggle-btn'>
                Login
              </button>
              <button type='button' className='toggle-btn'>
                Register
              </button>

            </div>
            <Login/>
            <form id='register' className='input-group'>
              
              <input type='email' className='input-field' placeholder='abc@example.com' required/>
              <input type='password' className='input-field' placeholder='enter password' required/>

            </form>

          </div>
          
        </div>
      </body>
    </div>

   
  
  
  
  )



}

export default SignUp