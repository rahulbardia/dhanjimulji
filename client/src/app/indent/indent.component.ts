import { Inject, Injectable } from '@angular/core';
import 'rxjs/Rx';
import { CommonService } from "./../shared/common.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';
import { SESSION_STORAGE, StorageService } from 'angular-webstorage-service';

@Component({
  selector: 'app-supplier-inventory',
  templateUrl: './indent.component.html',
  styleUrls: ['./indent.component.css']
})
@Injectable()
export class IndentComponent implements OnInit {
  data: any = null;
  endpoint = '/indent/indents/';
  rows = [1,2,3];
  indentOrderForm = {};
  constructor(private http: Http, private _service: CommonService, @Inject(SESSION_STORAGE) private storage: StorageService) {
  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any, my_order_form: any){
    console.log("indent form value", my_form, my_order_form, this.form);
        this._service.postForm(this.endpoint, my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  submit_forms = function () {
    let indent_form = document.getElementById('indent_form').onsubmit;
    let order_form = document.getElementById('order_form');
    // let form1 = document.getElementById('order_form').elements;
  };
  get_data = function(){
    // console.log("Get data called tenant" + this.tenant_id);
    // console.log("Local Memory RAHUL: "+ this.storage.get('tenant'));
        this._service.getData(this.endpoint, this.tenant_id)
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };

}
