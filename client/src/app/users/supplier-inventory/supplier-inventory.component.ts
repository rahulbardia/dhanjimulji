import 'rxjs/Rx';
import { Inject, Injectable } from '@angular/core';
import { CommonService } from "./../../shared/common.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';
import { SESSION_STORAGE, StorageService } from 'angular-webstorage-service';

@Component({
  selector: 'app-supplier-inventory',
  templateUrl: './supplier-inventory.component.html',
  styleUrls: ['./supplier-inventory.component.css']
})

@Injectable()
export class SupplierInventoryComponent implements OnInit {
  data: any = null;
  endpoint = '/users/supplierinventory/';
  constructor(private http: Http, private _service: CommonService, @Inject(SESSION_STORAGE) private storage: StorageService) {
  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
        this._service.postForm(this.endpoint, my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(){
    console.log("Get data called with tenant: " + this.storage.get("tenant"));
    //  TODO: update storage tenant to this.tenant_id(currently throwing error)
        this._service.getData(this.endpoint, this.storage.get("tenant"))
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}

