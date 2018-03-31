import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import 'rxjs/Rx';
import { Observable } from 'rxjs/Rx'
// import { Observable } from 'rxjs/observable';
import { config } from './../../../config';

@Injectable()
export class BuyerService {
  headers: Headers;
  options: RequestOptions;
  public user = config.username;
  public password = config.password;

  constructor(private _http: Http) {
    this.headers = new Headers({
      'Content-Type': 'application/x-www-form-urlencoded', /*or whatever type is relevant */
    });
    this.headers.append("Authorization", "Basic " + btoa(this.user + ":" + this.password));
    this.options = new RequestOptions({headers: this.headers});
  }

  private extractData(res: Response) {
    let body = res.json();
    return body || {};
  }

  private handelError(error: any) {
    console.error('post error:', error);
    return Observable.throw(error.statusText);
  }

  postBuyerForm(form_val): Observable<any> {
        return this._http.post(config.WebApiURL + '/users/buyer/', form_val, {headers: this.headers})
            .map(this.extractData)
            .catch(this.handelError);
    }

  getData(tenantId): Observable<any>{
    return this._http.get(config.WebApiURL + '/users/buyer/?tenant='+tenantId, {headers: this.headers})
      .map(this.extractData)
      .catch(this.handelError);
  }
}
