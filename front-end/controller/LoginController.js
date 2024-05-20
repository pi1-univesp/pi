import  LoginModel  from '../model/LoginModel'; 
  
  class  LoginController {
  
    constructor() {
      this.user = null;
    }
  
    login(email, password) {
      const userModel = new LoginModel(email, password);
      if (userModel.authenticate()) {
        this.user = userModel; 
        return true; 
      }
      return false; 
    }
    
  }
  