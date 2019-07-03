import { Inject, Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import 'rxjs/Rx';
import { Observable } from 'rxjs/Rx'
import { config } from './../config';
import { SESSION_STORAGE, StorageService } from 'angular-webstorage-service';

const STORAGE_KEY = 'tenant';

@Injectable()
export class CommonService {
  headers: Headers;
  options: RequestOptions;
  public user = config.username;
  public password = config.password;
  public tenant_id = this.storage.get('tenant');

  constructor(private _http: Http, @Inject(SESSION_STORAGE) private storage: StorageService) {
    this.headers = new Headers({
      'Content-Type': 'application/x-www-form-urlencoded', /*or whatever type is relevant */
    });
    this.headers.append("Authorization", "Basic " + btoa(this.user + ":" + this.password));
    this.options = new RequestOptions({headers: this.headers});
    // this.tenant_id = console.log("TENANT ID :  " + this.tenant_id);
    console.log("TENANT ID :  " + this.tenant_id);
  }

  private extractData(res: Response) {
    let body = res.json();
    return body || {};
  }

  private handelError(error: any) {
    console.error('post error:', error);
    return Observable.throw(error.statusText);
  }

  postForm(endpoint, form_val): Observable<any> {
    console.log("common service to post with tenant_id : %s", this.tenant_id);
    console.log(form_val);
    form_val.tenant = this.tenant_id;
    return this._http.post(config.WebApiURL + endpoint, form_val, {headers: this.headers})
        .map(this.extractData)
        .catch(this.handelError);
    }

  getData(endpoint, filter): Observable<any>{
    console.log("common service to get with tenant_id: %s", this.tenant_id);
    let url_string = config.WebApiURL + endpoint + '?tenant=' + this.tenant_id;
    for (let key in filter){
      url_string = url_string + "&" + key + "=" + filter[key];
    }
    console.log("url_string is: %s", url_string);
    return this._http.get(url_string, {headers: this.headers})
      .map(this.extractData)
      .catch(this.handelError);
  }
}
