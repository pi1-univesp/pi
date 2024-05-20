class LoginModel {
  constructor(email, password) {
    this.email = email;
    this.password = password;
  }

  authenticate() {
    const validCredentials = {
      email: 'johndoe@example.com',
      password: 'securepassword'
    };
    return (
      this.email === validCredentials.email &&
      this.password === validCredentials.password
    );
  }
}
