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
  tenant_id = this.storage.get('tenant');

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
    console.log("common service to post");
        console.log(form_val);
        return this._http.post(config.WebApiURL + endpoint, form_val, {headers: this.headers})
            .map(this.extractData)
            .catch(this.handelError);
    }

  getData(endpoint, tenantId): Observable<any>{
    console.log("common service to get");
    // this.tenant_id = console.log("TENANT ID :  " + this.tenant_id);
    // console.log("TENANT ID 2:  " + this.tenant_id);
    return this._http.get(config.WebApiURL + endpoint + '?tenant=' + tenantId, {headers: this.headers})
      .map(this.extractData)
      .catch(this.handelError);
  }
}
