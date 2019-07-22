import 'rxjs/Rx';
import { Inject, Injectable } from '@angular/core';
import { config } from './../config';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Component, OnInit } from '@angular/core';
import { SESSION_STORAGE, StorageService } from 'angular-webstorage-service';
import { FormBuilder,FormGroup, Validators } from '@angular/forms'

// export const MY_AWESOME_SERVICE_STORAGE =
//     new InjectionToken<StorageService>('MY_AWESOME_SERVICE_STORAGE');


const STORAGE_KEY = 'tenant';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
@Injectable()
export class LoginComponent implements OnInit {
  createForm:FormGroup; 

  headers: Headers;
  options: RequestOptions;
  public user = config.username;
  public password = config.password;
  data: any = null;
  endpoint = '/users/login/';
  tenant_id = null;
  constructor(private fb:FormBuilder,private _http: Http, @Inject(SESSION_STORAGE) private storage: StorageService) {
    this.createForm=fb.group({
      username:['',[Validators.email,Validators.required]],
      password:['',Validators.required]
    });
  }

  ngOnInit() {
    this.headers = new Headers({
      'Content-Type': 'application/x-www-form-urlencoded', /*or whatever type is relevant */
    });
    this.headers.append("Authorization", "Basic " + btoa(this.user + ":" + this.password));
  }
  LogIn(){
    console.log(this.createForm.value['username'])
    console.log(this.createForm.value['password'])

  }

  onSubmit = function(my_form: any){
    console.log(my_form, my_form.password);
        // this._service.getForm(this.endpoint, my_form)
        //     .subscribe(
        //     data => {
        //       console.log("data posted", data);
        //     });
    this.login(my_form.username, my_form.password)
  };



  login = function(username, password){
        return this._http.get(config.WebApiURL + this.endpoint + '?username=' + username + '&password=' + password,
          {headers: this.headers})
            .subscribe((response) => {
        console.log("API sent", response._body);
        this.tenant_id = response._body;
        this.storage.set(STORAGE_KEY, this.tenant_id);
        console.log("Local Memory: "+ this.storage.get(STORAGE_KEY));
      });
  };
}
