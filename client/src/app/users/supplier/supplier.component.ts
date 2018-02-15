import { Component, OnInit } from '@angular/core';
import { Http, Response, Headers } from '@angular/http';

@Component({
  selector: 'app-supplier',
  templateUrl: './supplier.component.html',
  styleUrls: ['./supplier.component.css']
})
export class SupplierComponent implements OnInit {
  public api_url = 'http://127.0.0.1:8000/indent/transport';

  constructor(private http: Http) {
  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
    // let payload = JSON.stringify(my_form.serializeBody());
    // let payload = my_form.getRawValue();
    console.log("Successfully submitted form!", my_form.value);
  };

  get_data = function() {
    console.log("Send API");
    let username: string = 'rahul';
    let password: string = 'bacardi1!';
    let headers: Headers = new Headers();
    headers.append("Authorization", "Basic " + btoa(username + ":" + password));
    // headers.append("Content-Type", "application/json");
    // headers.append('Access-Control-Allow-Origin', '*');
    headers.append("crossDomain", "True");
    headers.append("contentType", "application/x-www-form-urlencoded");
    headers.append("charset", "UTF-8");
    headers.append("success", "function(data) { console.log('rah'+data)}");
    headers.append("error", "function(xhr) {console.log(xhr)}");
    headers.append('Access-Control-Allow-Origin', '*');
    console.log("Headers : ", headers);
    let data = null;

    this.http.get(this.api_url, {headers: headers})
      .subscribe((response) => {
        data = response.json();
      });
  }
}
