import './Login.css'

const Login =() => {

    return (<div>

            <form id='login' className='input-group'>
              <input type='email' className='input-field' placeholder='abc@example.com' required/>
              <input type='password' className='input-field' placeholder='enter password' required/>
              <button type='submit' className='submit-btn'>Log in</button>
            </form>
    </div>)


}

export default Login;